# Math Modeling Skill

面向数学建模竞赛的 Codex Skill，提供建模、编程、论文、科研图、DOCX、LaTeX、PDF、Excel 和论文检索工具。

当前规则采用轻量协作模式：

- 项目 `AGENTS.md` 优先。
- 不强制 `STATUS/TASKS/DECISIONS`、Handoff、预算审批、固定 owner、模型路由或逐轮审核。
- `M1/P1/P2/W1/W2` 仅为可选核查标签。
- 原始题目和官方代码只读；正式论文仍须遵守当届模板、AI 标注、人工核验和 PDF MD5 要求。

## 安装

将本目录放入 Codex 的 Skills 目录，或在支持 Skill 的 Agent 中直接加载 `SKILL.md`。

```bash
npx skills add https://github.com/xiaomacoltai/math-modeling-skill --skill math-modeling
```

## 使用

```text
使用数学建模 Skill 完成这道题。
只做建模分析，输出题目分析报告和术语表格。
根据现有模型实现代码并运行，保留真实结果。
根据真实结果生成 Word 论文。
```

## 阶段

| 阶段 | 入口 | 主要交付 |
|---|---|---|
| 建模 | `references/roles/建模手/SKILL.md` | 题目分析报告、术语表格 |
| 编程 | `references/roles/编程手/SKILL.md` | 代码、结果、图、复现说明 |
| 论文 | `references/roles/论文手/SKILL.md` | Word；按需 LaTeX/PDF |

## 工具

- `tools/figure/`：数据剖析与出版级科研图
- `tools/docx/`：Word、公式和模板
- `tools/latex/`：LaTeX 模板、编译与 PDF 校验
- `tools/pdf/`：PDF 读取、表单和渲染
- `tools/xlsx/`：Excel 读写和公式重算
- `tools/paper_search/`：OpenAlex 与可选 AnySearch 检索

`dsh-plugin/` 是 LEGACY/ARCHIVE ONLY 的旧兼容包，不用于新项目，也不作为当前协作入口。

## 验证

```bash
python -m unittest discover -s tests -v
```
