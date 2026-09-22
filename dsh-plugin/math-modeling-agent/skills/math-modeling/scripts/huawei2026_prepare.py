#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

FILES = {
    "附件1": ("附件1：“华为杯”第二十三届中国研究生数学建模竞赛下载试题及上传论文操作手册.pdf", "bd3f6c4456f8f57b309a3aace33644e1a9f877883cda64bf7d014c4e9e7adec4"),
    "附件2": ("附件2：“华为杯”第二十三届中国研究生数学建模竞赛论文格式规范.docx", "46d2e2a87e90608ace764203d5326d7c7e41f01a5eb79986724a6f159fd70e16"),
    "附件3": ("附件3：“华为杯”第二十三届中国研究生数学建模竞赛论文模板.doc", "195b06cf670ec1aeb796bfd07e6d3e98e36d16db119308dcf4d0756319fe2e29"),
    "附件4": ("附件4：“华为杯”第二十三届中国研究生数学建模竞赛人工智能工具及输出使用规定.docx", "5922c1f92530c88eab3214e67de981aeda195c27d5b583ddc2380ee24db0e539"),
}

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def find_one(source: Path, prefix: str) -> Path:
    matches = sorted(p for p in source.iterdir() if p.is_file() and p.name.startswith(prefix))
    if len(matches) != 1:
        raise SystemExit(f"expected one {prefix} file in {source}; found {len(matches)}")
    return matches[0]

def write_if_missing(path: Path, text: str) -> None:
    if not path.exists():
        path.write_text(text, encoding="utf-8")

def main() -> None:
    ap = argparse.ArgumentParser(description="Prepare a 2026 Huawei Cup project from the four official attachments.")
    ap.add_argument("project_root", type=Path)
    ap.add_argument("--source-dir", type=Path, required=True)
    args = ap.parse_args()

    root = args.project_root.resolve()
    src = args.source_dir.resolve()
    official = root / "official" / "2026"
    dirs = [
        official, root/"paper"/"template", root/"paper"/"working", root/"paper"/"sections",
        root/"paper"/"checkpoints", root/"paper"/"export", root/"submission"/"locked",
        root/"attachments", root/"ai_usage"/"prompts", root/"ai_usage"/"templates",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    located = {}
    manifest = []
    for prefix, (canonical, expected) in FILES.items():
        p = find_one(src, prefix)
        got = digest(p)
        if got != expected:
            raise SystemExit(f"SHA256 mismatch for {p.name}: {got}; expected {expected}")
        dst = official / canonical
        shutil.copy2(p, dst)
        located[prefix] = dst
        manifest.append(f"{expected}  {canonical}")
    (official/"SHA256SUMS.txt").write_text("\n".join(manifest)+"\n", encoding="utf-8")

    shutil.copy2(located["附件3"], root/"paper"/"template"/"官方论文模板.doc")
    working = root/"paper"/"working"/"论文工作稿.doc"
    if not working.exists():
        shutil.copy2(located["附件3"], working)

    write_if_missing(root/"ai_usage"/"usage.csv", "time,member,tool,model,developer,release_date,purpose,output_file,adopted,human_modification,human_verification,commit\n")
    write_if_missing(root/"ai_usage"/"templates"/"code_header_python.txt", "# 本程序及代码是在人工智能工具辅助下完成的。\n# AI工具名称：<工具名>\n# 版本/型号：<版本或模型>\n# 开发机构/公司：<机构/公司>\n# 版本发布日期：<YYYY-MM-DD>\n# 人工核验说明：<如何检查、修改与验证>\n")
    write_if_missing(root/"ai_usage"/"templates"/"code_header_matlab.txt", "% 本程序及代码是在人工智能工具辅助下完成的。\n% AI工具名称：<工具名>\n% 版本/型号：<版本或模型>\n% 开发机构/公司：<机构/公司>\n% 版本发布日期：<YYYY-MM-DD>\n% 人工核验说明：<如何检查、修改与验证>\n")
    write_if_missing(root/"ai_usage"/"templates"/"data_analysis_annotation.txt", "AI辅助说明：本节（或上述/下述）数据分析参考了 <AI工具名称>（版本/型号：<...>；开发机构/公司：<...>；版本发布日期：<YYYY-MM-DD>）的辅助输出。参赛队已对数据处理逻辑、参数、计算结果和最终表述进行人工核验与修改。\n")
    print(f"prepared official 2026 Huawei Cup structure under {root}")

if __name__ == "__main__":
    main()
