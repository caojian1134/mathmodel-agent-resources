# MathModel Agent Resources

> 数学建模竞赛 AI-Agent、Skills、求解工具、算法、模板与赛题资源导航。

[![Projects](https://img.shields.io/badge/projects-32-2563eb)](./CATALOG.md)
[![Language](https://img.shields.io/badge/language-中文-16a34a)](#项目目录)
[![License](https://img.shields.io/badge/catalog-MIT-f59e0b)](./LICENSE)
[![Last reviewed](https://img.shields.io/badge/reviewed-2026--09--06-64748b)](./docs/evaluation-method.md)

这个仓库是一份面向数学建模学习者和参赛队的**项目总结目录**，汇总 32 个公开项目，覆盖 CUMCM、MCM/ICM 等场景中的数学建模 Agent、竞赛 Skill、智能优化工具、算法代码、LaTeX 模板和历年赛题。

This is a curated directory—not a mirror—of open-source resources for AI-assisted mathematical modeling competitions.

## 这个仓库做什么

- 给出 32 个项目的原始地址、类别和一句话定位；
- 帮助使用者区分“完整竞赛工作流”“单项 Skill”“求解工具”“模板”和“赛题库”；
- 记录本次检查时的 commit、`SKILL.md` 数量和根目录许可证状态；
- 提醒参赛者核对当届规则、披露 AI 使用并人工验证结果；
- 接受社区补充、纠错和更新。

本仓库**不重新上传或重新授权第三方源码**。项目名称、代码、文档和商标归各自作者所有；使用前请访问原仓库核对最新版本及许可证。

## 快速选择

| 需求 | 建议先看 |
|---|---|
| 需要完整比赛流程与状态管理 | `handsomeZR/mathmodel-skill`、`Hjdd14/math-modeling`、`xuec699/math-modeling-skills` |
| 需要多角色/多阶段 Skill 组合 | `chengziyue1222/math-model-agent`、`zhnnky329/MathModeling-skills`、`yushui2022/MathModel-Skill` |
| 研究开放式数学建模 Agent | `ModelingAgent`、`LLM-MM-Agent` |
| 运筹优化与求解器协作 | `ORLM`、`solver-in-the-loop`、`ReSocratic`、`LLM4OPT` |
| Python/MATLAB 算法示例 | `MathematicalModelingAlgorithm`、`fanjufei/CUMCM` |
| CUMCM/MCM 排版模板 | `CUMCM2026-Template`、`CUMCMThesis`、`jayxin/cumcm`、`MCM-Template`、`icmmcm` |
| 历年国赛题目与附件 | `CosmicLinks/cumcm-problems` |

## 项目目录

### A. 数学建模 Agent（2）

1. [qiancheng0/ModelingAgent](https://github.com/qiancheng0/ModelingAgent) — 面向真实开放式问题的数学建模 Agent，组织问题分析、模型构建、计算与结果表达。
2. [usail-hkust/LLM-MM-Agent](https://github.com/usail-hkust/LLM-MM-Agent) — 将开放式数学建模拆分为分析、形式化、计算求解和报告生成等阶段的 Agent 框架。

### B. 竞赛 Skills、Agent 与 Starter（16）

3. [chengziyue1222/math-model-agent](https://github.com/chengziyue1222/math-model-agent) — 由审题、选模、求解、数据分析、绘图和检查等多个 Skill 组成的竞赛工作流。
4. [Escap1ng/math-modeling-skill](https://github.com/Escap1ng/math-modeling-skill) — 轻量数学建模竞赛 Skill，适合查看基本流程骨架。
5. [lg66lgnb-sketch/math-modeling-skill](https://github.com/lg66lgnb-sketch/math-modeling-skill) — 强调编号提问、角色分工、质量门和结果冻结的 CUMCM/MCM 工作流。
6. [VectorAC/math-modeling-skill](https://github.com/VectorAC/math-modeling-skill) — 教学辅助型 Skill，强调交互门、阶段审阅和比赛类型切换。
7. [XiaoMaColtAI/math-modeling-skill](https://github.com/XiaoMaColtAI/math-modeling-skill) — 包含建模手、编程手、写作角色及文档、图形和数据工具的综合 Skill。
8. [Zhengxuejun/mathematical-modeling-agent](https://github.com/Zhengxuejun/mathematical-modeling-agent) — 面向数学建模任务的 Agent/Skill 实现。
9. [yushui2022/MathModel-Skill](https://github.com/yushui2022/MathModel-Skill) — 为 Claude、Codex、Trae 等宿主组织数据、建模、代码、写作和质量审计 Skill。
10. [jihe520/MathModelAgent](https://github.com/jihe520/MathModelAgent) — 按启动、分析建模、代码可视化、绘图、写作和核验划分的技能组。
11. [zhnnky329/MathModeling-skills](https://github.com/zhnnky329/MathModeling-skills) — 大规模多角色 Skill 集，涵盖数据、模型、Python/MATLAB、图表和一致性检查。
12. [Gunp-666/MCM-AI-Starter-Kit](https://github.com/Gunp-666/MCM-AI-Starter-Kit) — 面向 MCM/ICM 的 AI 辅助起步资源。
13. [dreamnight16/MCM-Resource](https://github.com/dreamnight16/MCM-Resource) — MCM 竞赛相关工具和准备资源集合。
14. [woodfishhhh/EZ_math_model](https://github.com/woodfishhhh/EZ_math_model) — 综合型数学建模 Skill 包，集成数据、文档、绘图、检索和运行工具；功能多，安装前应重点审计脚本。
15. [handsomeZR-netizen/mathmodel-skill](https://github.com/handsomeZR-netizen/mathmodel-skill) — 10 阶段流程、共享决策日志、竞赛特化和分层反馈机制。
16. [Hjdd14/math-modeling](https://github.com/Hjdd14/math-modeling) — 强调题目解析、并行方案、代码交付、图表证据和独立验证。
17. [xuec699-sudo/math-modeling-skills](https://github.com/xuec699-sudo/math-modeling-skills) — 提供 Manual/Autopilot、模型依赖 DAG、结果冻结和质量门控。
18. [cha3343954211/math-modeling-skill](https://github.com/cha3343954211/math-modeling-skill) — 面向 Hermes Agent 的数学建模竞赛 Skill，也可作为通用流程参考。

### C. Agent 支撑、优化与评测（6）

19. [AgenticDataBench/AgenticDataBench](https://github.com/AgenticDataBench/AgenticDataBench) — 用于评价数据分析 Agent 能力的基准和任务资源。
20. [ishmael233/LLM4OPT](https://github.com/ishmael233/LLM4OPT) — 大语言模型与优化问题相关项目、方法和资源目录。
21. [oashua/MathAgent](https://github.com/oashua/MathAgent) — 数学推理与 Agent 规划相关实现；使用前需结合代码和项目说明判断适用边界。
22. [Cardinal-Operations/ORLM](https://github.com/Cardinal-Operations/ORLM) — 面向运筹学和数学规划的语言模型及配套工具。
23. [yangzhch6/ReSocratic](https://github.com/yangzhch6/ReSocratic) — 通过交互式推理处理优化建模问题，并包含相关评测资源。
24. [agentic-or-benchmark/solver-in-the-loop](https://github.com/agentic-or-benchmark/solver-in-the-loop) — 将优化求解器反馈纳入 Agent 推理与验证闭环。

### D. 算法代码（2）

25. [Giyn/MathematicalModelingAlgorithm](https://github.com/Giyn/MathematicalModelingAlgorithm) — 数学建模常用算法的 Python 示例代码。
26. [fanjufei/CUMCM](https://github.com/fanjufei/CUMCM) — MATLAB 基础、优化、评价、预测和分类方法的竞赛教程入口。

### E. 排版模板（5）

27. [langonginc/CUMCM2026-Template](https://github.com/langonginc/CUMCM2026-Template) — 面向 2026 CUMCM 的 LaTeX 模板候选。
28. [latexstudio/CUMCMThesis](https://github.com/latexstudio/CUMCMThesis) — 常用 CUMCM LaTeX 模板项目。
29. [jayxin/cumcm](https://github.com/jayxin/cumcm) — 结构清晰、正文分文件组织的 CUMCM LaTeX 模板。
30. [vladzhdanov/MCM-Template](https://github.com/vladzhdanov/MCM-Template) — MCM/ICM LaTeX 模板。
31. [harveymuddcollege/icmmcm](https://github.com/harveymuddcollege/icmmcm) — Harvey Mudd College 维护的 ICM/MCM 模板资源。

### F. 历年赛题与附件（1）

32. [CosmicLinks/cumcm-problems](https://github.com/CosmicLinks/cumcm-problems) — 按年份整理的 CUMCM 1992–2025 赛题原文与配套数据；请核对上游版权与许可证后使用。

完整字段、快照 commit 和许可证观察结果见 [CATALOG.md](./CATALOG.md) 与 [data/projects.csv](./data/projects.csv)。

## 使用这些项目时的推荐流程

1. 先确认比赛、题目、截止时间和当届官方规则；
2. 只选择一套主流程 Skill，避免多个编排器互相覆盖；
3. 根据题型选择确定性工具，例如 SciPy、CVXPY、OR-Tools、Pyomo、SALib 或 Mesa；
4. 保留原始数据、模型假设、代码版本、随机种子和结果清单；
5. 使用基线、敏感性分析、边界测试和独立复算核验结果；
6. 按官方要求披露 AI 工具、用途、关键交互和人工修改情况。

## 重要边界

- 收录不代表推荐、认证、安全或比赛合规；
- `SKILL.md` 可以要求 Agent 执行命令、访问网络或修改文件，安装前必须人工审阅；
- 没有许可证的公开仓库不等于可以任意复制、修改或再发布；
- 第三方模板可能落后于当届页数、匿名、字体和提交要求；
- AI 输出不能替代模型有效性证明、代码复现和人工结论核验；
- 比赛进行期间，不得违反禁止队外交流、公开讨论赛题等规定。

## 贡献

欢迎通过 Issue 或 Pull Request：

- 补充新的数学建模 Agent/Skill；
- 修正项目描述、失效链接或许可证状态；
- 报告供应链、安全和比赛合规风险；
- 提供可复现的最小验收结果。

提交前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)。收录方法见 [docs/evaluation-method.md](./docs/evaluation-method.md)。

## 许可与致谢

本仓库原创的目录、说明和维护脚本采用 [MIT License](./LICENSE)。该许可**不覆盖**链接到的第三方项目；第三方内容继续受其原许可证和版权约束。

感谢所有上游项目维护者。若项目作者希望更正描述、补充许可证信息或移除条目，请提交 Issue。
