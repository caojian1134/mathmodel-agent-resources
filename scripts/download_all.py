#!/usr/bin/env python3
"""Download and validate the 32 pinned upstream GitHub archives."""

from __future__ import annotations

import argparse
import csv
import hashlib
import http.client
import json
import os
import shutil
import sys
import time
import urllib.error
import urllib.request
import zipfile
import zlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "downloads.csv"
USER_AGENT = "mathmodel-agent-resources-downloader/1.0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def valid_zip(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size == 0:
        return False
    try:
        with zipfile.ZipFile(path) as archive:
            return archive.testzip() is None and bool(archive.infolist())
    except (OSError, zipfile.BadZipFile, zlib.error):
        return False


def download_one(row: dict[str, str], destination: Path, retries: int) -> dict[str, str | int]:
    target = destination / row["archive_file"]
    if valid_zip(target):
        return {
            **row,
            "status": "existing-valid",
            "bytes": target.stat().st_size,
            "sha256": sha256(target),
        }

    if target.exists():
        invalid = target.with_suffix(target.suffix + f".invalid-{int(time.time())}")
        target.replace(invalid)

    partial = target.with_suffix(target.suffix + ".part")
    error = ""
    for attempt in range(1, retries + 1):
        if partial.exists():
            partial.unlink()
        try:
            request = urllib.request.Request(row["archive_url"], headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=120) as response, partial.open("wb") as output:
                shutil.copyfileobj(response, output, length=1024 * 1024)
            if not valid_zip(partial):
                raise zipfile.BadZipFile("downloaded file failed ZIP validation")
            os.replace(partial, target)
            return {
                **row,
                "status": "downloaded-valid",
                "bytes": target.stat().st_size,
                "sha256": sha256(target),
            }
        except (
            OSError,
            TimeoutError,
            urllib.error.URLError,
            http.client.HTTPException,
            zipfile.BadZipFile,
        ) as exc:
            error = f"attempt {attempt}: {exc}"
            time.sleep(min(2**attempt, 15))

    return {**row, "status": "failed", "bytes": 0, "sha256": "", "error": error}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=ROOT / "project-archives")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--list-only", action="store_true")
    args = parser.parse_args()

    with MANIFEST.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 32:
        raise RuntimeError(f"expected 32 manifest entries, found {len(rows)}")

    if args.list_only:
        for row in rows:
            print(f'{int(row["id"]):02d} {row["repository"]} -> {row["archive_file"]}')
        return 0

    destination = args.destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, str | int]] = []
    workers = max(1, min(args.workers, 8))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(download_one, row, destination, args.retries): row for row in rows}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(f'[{result["status"]}] {result["repository"]}', flush=True)

    results.sort(key=lambda item: int(str(item["id"])))
    report = destination / "download-report.csv"
    fields = [
        "id", "name", "repository", "pinned_ref", "archive_file", "archive_url",
        "status", "bytes", "sha256", "license_spdx", "redistribution", "error",
    ]
    with report.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    failed = [item for item in results if item["status"] == "failed"]
    summary = {
        "expected": 32,
        "valid": len(results) - len(failed),
        "failed": len(failed),
        "bytes": sum(int(item.get("bytes", 0)) for item in results),
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    (destination / "download-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
