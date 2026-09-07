"""Offline regressions for archive validation and download recovery."""

import importlib.util
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "download_all.py"
SPEC = importlib.util.spec_from_file_location("download_all", SCRIPT)
downloader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(downloader)


def archive_bytes(*, corrupt=False):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("example.txt", "small synthetic test payload")
    payload = bytearray(stream.getvalue())
    if corrupt:
        # Keep the ZIP directory intact but set the first DEFLATE block to
        # the reserved BTYPE=3. Reading it raises zlib.error, not BadZipFile.
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            info = archive.infolist()[0]
            offset = info.header_offset + 30 + len(info.filename.encode()) + len(info.extra)
        payload[offset] = (payload[offset] & ~6) | 6
    return bytes(payload)


class ArchiveTests(unittest.TestCase):
    def test_corrupt_deflate_is_invalid(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "archive.zip"
            target.write_bytes(archive_bytes(corrupt=True))
            self.assertFalse(downloader.valid_zip(target))

    def test_corrupt_cached_zip_is_preserved_and_replaced(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            target = destination / "archive.zip"
            target.write_bytes(archive_bytes(corrupt=True))
            row = {"archive_file": target.name, "archive_url": "https://example.invalid/archive.zip"}
            with patch.object(downloader.urllib.request, "urlopen", return_value=io.BytesIO(archive_bytes())):
                result = downloader.download_one(row, destination, retries=1)
            self.assertEqual(result["status"], "downloaded-valid")
            self.assertTrue(downloader.valid_zip(target))
            self.assertEqual(len(list(destination.glob("*.invalid-*"))), 1)

    def test_corrupt_download_retries_without_network(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            row = {"archive_file": "archive.zip", "archive_url": "https://example.invalid/archive.zip"}
            responses = [io.BytesIO(archive_bytes(corrupt=True)), io.BytesIO(archive_bytes())]
            with patch.object(downloader.urllib.request, "urlopen", side_effect=responses) as request:
                with patch.object(downloader.time, "sleep"):
                    result = downloader.download_one(row, destination, retries=2)
            self.assertEqual(result["status"], "downloaded-valid")
            self.assertEqual(request.call_count, 2)
            self.assertFalse((destination / "archive.zip.part").exists())


if __name__ == "__main__":
    unittest.main()
