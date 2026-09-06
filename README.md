# MathModel Agent Resources

> A curated, classified, and download-verified collection of **32 AI agents, skills, optimization tools, algorithms, templates, and problem archives** for mathematical modeling.

[English](./README.md) | [中文](./README_CN.md)

[![Projects](https://img.shields.io/badge/projects-32-2563eb)](./CATALOG.md)
[![Verified downloads](https://img.shields.io/badge/downloads-32%2F32_verified-16a34a)](./DOWNLOADS.md)
[![Catalog license](https://img.shields.io/badge/catalog_license-MIT-f59e0b)](./LICENSE)
[![Last reviewed](https://img.shields.io/badge/reviewed-2026--09--06-64748b)](./docs/evaluation-method.md)

![MathModel Agent Resources social preview](./assets/social-preview.png)

This repository is a practical discovery and download hub for AI-assisted mathematical modeling. It covers CUMCM, MCM/ICM, open-ended modeling, operations research, data analysis, reproducible computation, and contest-paper preparation.

It is more than a bookmark list: every downloadable entry is pinned to a reviewed commit, and all 32 archives were downloaded and checked as valid ZIP files on **2026-09-06**.

## Why this directory exists

The rapid growth of agents and `SKILL.md`-based workflows has made it difficult to answer three basic questions:

1. Which project fits my task?
2. Is it an agent, a workflow skill, a solver tool, an algorithm collection, or only a template?
3. Can I still obtain the exact version that was reviewed?

This directory addresses those questions with:

- a classified catalog of 32 public projects;
- a task-oriented [selection guide and comparison matrix](./docs/project-selection-guide.md);
- pinned source commits and machine-readable metadata;
- one-click and batch download options;
- file-size and SHA-256 verification records;
- explicit safety, licensing, reproducibility, and contest-compliance boundaries.

## Start here

| What you need | Recommended starting point |
|---|---|
| A complete contest workflow with checkpoints | `handsomeZR/mathmodel-skill`, `Hjdd14/math-modeling`, `xuec699/math-modeling-skills` |
| A multi-role or multi-skill toolkit | `chengziyue1222/math-model-agent`, `zhnnky329/MathModeling-skills`, `yushui2022/MathModel-Skill` |
| Research on open-ended modeling agents | `ModelingAgent`, `LLM-MM-Agent` |
| Operations research and solver feedback | `ORLM`, `solver-in-the-loop`, `ReSocratic`, `LLM4OPT` |
| Python or MATLAB algorithm examples | `MathematicalModelingAlgorithm`, `fanjufei/CUMCM` |
| CUMCM or MCM/ICM LaTeX templates | `CUMCM2026-Template`, `CUMCMThesis`, `jayxin/cumcm`, `MCM-Template`, `icmmcm` |
| Historical CUMCM problems and attachments | `CosmicLinks/cumcm-problems` |

These are navigation suggestions, not quality rankings or endorsements. See the [full comparison guide](./docs/project-selection-guide.md) before choosing a project.

## Download all 32 projects

```powershell
git clone https://github.com/caojian1134/mathmodel-agent-resources.git
cd mathmodel-agent-resources
python scripts/download_all.py --destination project-archives --workers 4
```

On Windows, you can also run:

```powershell
.\scripts\download_all.ps1 -Destination .\project-archives
```

The downloader reads [`data/downloads.csv`](./data/downloads.csv), skips archives that already pass validation, and produces size and SHA-256 reports. Individual pinned ZIP links are available in the [Download Center](./DOWNLOADS.md).

### Verified snapshot

- Verified on: **2026-09-06**
- Valid archives: **32/32**
- Failed archives: **0**
- Total size: **1,368,959,922 bytes (about 1.275 GiB)**
- Checksums: [`data/verified-downloads-2026-09-06.csv`](./data/verified-downloads-2026-09-06.csv)

Archives are downloaded directly from the original GitHub repositories. This repository does not relicense third-party code. Some upstream projects do not declare a clear license; review the upstream repository before using, modifying, or redistributing its content.

## The 32 projects at a glance

| Group | Count | Examples |
|---|---:|---|
| Open-ended modeling agents | 2 | ModelingAgent, LLM-MM-Agent |
| Contest skills, agents, and starter kits | 16 | math-model-agent, MathModel-Skill, MCM-AI-Starter-Kit |
| Agent support, optimization, and benchmarks | 6 | AgenticDataBench, ORLM, solver-in-the-loop |
| Algorithm collections | 2 | MathematicalModelingAlgorithm, CUMCM |
| Typesetting templates | 5 | CUMCMThesis, MCM-Template, icmmcm |
| Problem archives | 1 | cumcm-problems |

For all project links and descriptions, see [`CATALOG.md`](./CATALOG.md). For snapshot commits, observed licenses, and `SKILL.md` counts, see [`data/projects.csv`](./data/projects.csv).

## A responsible modeling workflow

1. Confirm the contest, problem, deadline, and current official rules.
2. Choose one primary orchestration workflow; avoid combining multiple agents without a clear ownership boundary.
3. Use deterministic tools such as SciPy, CVXPY, OR-Tools, Pyomo, SALib, or Mesa when appropriate.
4. Preserve source data, assumptions, code versions, random seeds, and output manifests.
5. Validate results with baselines, sensitivity analysis, boundary tests, and independent recomputation.
6. Disclose AI use, important interactions, and human revisions when the contest requires it.

## Important boundaries

- Inclusion does not mean endorsement, certification, security approval, or contest compliance.
- A `SKILL.md` file may instruct an agent to run commands, access the network, or modify files. Review it before installation.
- A public repository without a license is not automatically reusable or redistributable.
- Third-party templates may not match the latest page, anonymity, font, or submission requirements.
- AI output does not replace model validation, reproducible code, or human responsibility.
- Never discuss a live contest problem publicly when its rules prohibit external communication.

## Contributing

Corrections, new projects, reproducible evaluations, and maintenance help are welcome. Please read [`CONTRIBUTING.md`](./CONTRIBUTING.md), our [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md), and the [evaluation method](./docs/evaluation-method.md), then open an Issue or Pull Request.

If this directory saves you time, consider starring it so that more modeling teams can discover it. Stars are appreciated, but evidence-backed corrections and contributions are even more valuable.

## License and acknowledgements

Original catalog text and maintenance scripts in this repository are released under the [MIT License](./LICENSE). This license does **not** cover linked third-party projects; their original licenses and copyrights remain in force.

Thanks to all upstream maintainers. Project authors are welcome to correct a description, clarify licensing, or request removal through an Issue.
