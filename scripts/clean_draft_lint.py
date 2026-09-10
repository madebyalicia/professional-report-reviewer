#!/usr/bin/env python3
"""Limited explicit-numbering/wording scan; not a semantic or quality review."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

RESIDUE_WARNING_PATTERNS = [
    ("editorial_residue", re.compile(pattern))
    for pattern in (
        r"原稿",
        r"原报告",
        r"本版(?:报告|修改|删除|保留)",
        r"本次修改",
        r"修改说明",
        r"修改反馈",
        r"审查意见",
        r"审查结论",
        r"编辑说明",
        r"修订说明",
        r"尚不能成立的原结论",
        r"下一步证据",
        r"待补证据",
        r"保留可核验事实",
        r"仅保留可核验",
        r"为什么修改",
        r"修改前",
        r"修改后",
        r"(?i)\b(?:reviewer(?:'s)? (?:note|comment|instruction)|editorial note|revision rationale|evidence still needed|unsupported original conclusion)\b",
    )
]

HEADING_WARNING_PATTERNS = [
    re.compile(r"(?:必须|需要|应当|应该).{0,12}(?:统一口径|补充证据|验证机制|删除|保留|改写)"),
    re.compile(r"(?:如何|怎样).{0,12}(?:修改|验证|保留|删除|改写)"),
]

# These phrases are not automatically wrong, but clusters of them often signal
# that reviewer caveats or generic operating advice leaked into a clean report.
# Keep them as warnings so a human/agent must apply the semantic contribution
# gate instead of deleting defensible analysis by regex.
REPLACEMENT_FILLER_WARNING_PATTERNS = [
    re.compile(pattern)
    for pattern in (
        r"(?:现有|当前)(?:材料|信息|证据).{0,10}(?:不能|无法)(?:证明|支持)",
        r"(?:更稳健|更谨慎|更合理)的结论",
        r"(?:应|需要)(?:当)?区分",
        r"(?:只能|仅能)(?:作为|说明|表明)",
        r"仍(?:然)?(?:取决于|依赖于)",
        r"战略权重.{0,8}(?:较低|更低|有限)",
        r"(?:形成|建立)(?:传播|营销|反馈|运营)?闭环",
        r"(?:提升|增强|扩大)(?:品牌)?(?:知名度|影响力|曝光度)",
    )
]

NUMBER_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)(?=\s|[、.．]|$)")
CHINESE_RE = re.compile(r"^\s*(?:第([一二三四五六七八九十百〇零两]+)章|([一二三四五六七八九十百〇零两]+)、)")


def chinese_number(text: str) -> int:
    digits = dict(zip("零〇一二两三四五六七八九", (0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9)))
    value = current = 0
    for char in text:
        if char in digits:
            current = digits[char]
        elif char in "十百":
            value += (current or 1) * {"十": 10, "百": 100}[char]
            current = 0
    return value + current


def heading_number(block: dict[str, object]) -> tuple[int, ...] | None:
    text = str(block["text"])
    chinese = CHINESE_RE.match(text)
    if chinese:
        # Only explicit styled/Markdown headings are checked. Chinese lists in
        # body text cannot safely be distinguished from headings by punctuation.
        return (chinese_number(chinese.group(1) or chinese.group(2)),) if block["level"] is not None else None
    match = NUMBER_RE.match(text) if block["level"] is not None else None
    return tuple(map(int, match.group(1).split("."))) if match else None


def docx_blocks(path: Path) -> list[dict[str, object]]:
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
        style_names: dict[str, str] = {}
        if "word/styles.xml" in zf.namelist():
            styles = ET.fromstring(zf.read("word/styles.xml"))
            for style in styles.findall(f"{W}style"):
                style_id = style.get(f"{W}styleId", "")
                name = style.find(f"{W}name")
                style_names[style_id] = name.get(f"{W}val", "") if name is not None else style_id

    blocks: list[dict[str, object]] = []
    body = root.find(f"{W}body")
    if body is None:
        return blocks
    table_number = 0
    for node in body:
        if node.tag == f"{W}p":
            text = "".join(item.text or "" for item in node.iter(f"{W}t")).strip()
            if not text:
                continue
            pstyle = node.find(f"{W}pPr/{W}pStyle")
            style_id = pstyle.get(f"{W}val", "") if pstyle is not None else ""
            style = style_names.get(style_id, style_id)
            level = None
            match = re.search(r"(?:heading|标题)\s*([1-9])", style, re.I)
            if match:
                level = int(match.group(1))
            blocks.append({"text": text, "level": level, "where": f"paragraph {len(blocks) + 1}"})
        elif node.tag == f"{W}tbl":
            table_number += 1
            for cell_number, cell in enumerate(node.iter(f"{W}tc"), start=1):
                text = "".join(item.text or "" for item in cell.iter(f"{W}t")).strip()
                if text:
                    blocks.append({
                        "text": text,
                        "level": None,
                        "where": f"table {table_number}, cell {cell_number}",
                    })
    return blocks


def text_blocks(path: Path) -> list[dict[str, object]]:
    blocks: list[dict[str, object]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        text = raw.strip()
        if not text:
            continue
        level = None
        markdown_heading = re.match(r"^(#{1,6})\s+(.*)$", text)
        if markdown_heading:
            level = len(markdown_heading.group(1))
            text = markdown_heading.group(2).strip()
        blocks.append({"text": text, "level": level, "where": f"line {line_number}"})
    return blocks


def lint(blocks: list[dict[str, object]]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for block in blocks:
        text = str(block["text"])
        for kind, pattern in RESIDUE_WARNING_PATTERNS:
            match = pattern.search(text)
            if match:
                findings.append({
                    "severity": "warning",
                    "kind": kind,
                    "where": block["where"],
                    "match": match.group(0),
                    "text": text[:180],
                })
        for pattern in REPLACEMENT_FILLER_WARNING_PATTERNS:
            match = pattern.search(text)
            if match:
                findings.append({
                    "severity": "warning",
                    "kind": "possible_replacement_filler",
                    "where": block["where"],
                    "match": match.group(0),
                    "text": text[:180],
                })
        if block["level"] is not None:
            for pattern in HEADING_WARNING_PATTERNS:
                match = pattern.search(text)
                if match:
                    findings.append({
                        "severity": "warning",
                        "kind": "editor_facing_heading",
                        "where": block["where"],
                        "match": match.group(0),
                        "text": text[:180],
                    })

    expected_by_parent: dict[tuple[int, ...], int] = {}
    active: tuple[int, ...] = ()
    for heading in blocks:
        number = heading_number(heading)
        if number is None:
            continue
        parent = number[:-1]
        expected = expected_by_parent.get(parent, 1)
        wrong_parent = bool(parent) and active[:len(parent)] != parent
        if number[-1] != expected or wrong_parent:
            detail = "active numbered parent missing/mismatched" if wrong_parent else "expected " + ".".join(map(str, (*parent, expected)))
            findings.append({
                "severity": "error",
                "kind": "heading_sequence",
                "where": heading["where"],
                "match": ".".join(map(str, number)),
                "text": f"{detail}, found {heading['text']}",
            })
        expected_by_parent[parent] = number[-1] + 1
        active = number
    return findings


def substantive_character_count(blocks: list[dict[str, object]]) -> int:
    """Count visible letters and numbers; ignore whitespace and punctuation."""
    return sum(len(re.findall(r"[\w\u3400-\u9fff]", str(block["text"]), re.UNICODE)) for block in blocks)


def load_blocks(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".docx":
        return docx_blocks(path)
    if path.suffix.lower() in {".md", ".markdown", ".txt"}:
        return text_blocks(path)
    raise ValueError("supported formats: .docx, .md, .markdown, .txt")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--source", type=Path, help="Source for length comparison only; does not measure content preservation")
    parser.add_argument(
        "--allow-material-reduction",
        action="store_true",
        help="Deprecated compatibility flag; cannot grant deletion approval or certify preservation",
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable findings")
    args = parser.parse_args()

    if not args.file.exists():
        parser.error(f"file not found: {args.file}")
    try:
        blocks = load_blocks(args.file)
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    findings = lint(blocks)
    scope_metrics = None
    if args.source:
        try:
            source_blocks = load_blocks(args.source)
        except (FileNotFoundError, ValueError) as exc:
            parser.error(str(exc))
        source_chars = substantive_character_count(source_blocks)
        revised_chars = substantive_character_count(blocks)
        ratio = revised_chars / source_chars if source_chars else 1.0
        scope_metrics = {
            "source_characters": source_chars,
            "revised_characters": revised_chars,
            "ratio": round(ratio, 4),
            "meaning_preservation_assessed": False,
        }
        if ratio < 0.8:
            findings.append({
                "severity": "warning",
                "kind": "length_reduction_review",
                "where": "whole document",
                "match": f"{ratio:.1%}",
                "text": (
                    "Text length is below 80% of source; inspect actual coverage and approved changes. "
                    "This is not a retention score or minimum-length requirement. Do not pad text."
                ),
            })
    limits = "Selected explicit heading numbers and wording only; no semantic, authorization, factual, natural-language, or layout certification. Word-generated automatic numbering and body lists are not checked."
    status = "issues_found" if any(item["severity"] == "error" for item in findings) else "review_candidates" if findings else "limited_scan_passed"
    if args.json:
        print(json.dumps({"file": str(args.file), "status": status, "limitations": limits, "scope_metrics": scope_metrics, "findings": findings}, ensure_ascii=False, indent=2))
    elif findings:
        if scope_metrics:
            print(
                "LENGTH ONLY "
                f"source={scope_metrics['source_characters']} "
                f"revised={scope_metrics['revised_characters']} "
                f"ratio={scope_metrics['ratio']:.1%}"
            )
        for item in findings:
            print(f"{item['severity'].upper()} {item['kind']} | {item['where']} | {item['text']}")
        print(f"LIMITS: {limits}")
    else:
        if scope_metrics:
            print(
                "LENGTH ONLY "
                f"source={scope_metrics['source_characters']} "
                f"revised={scope_metrics['revised_characters']} "
                f"ratio={scope_metrics['ratio']:.1%}"
            )
        print(f"PASS limited format/wording scan: {args.file}")
        print(f"LIMITS: {limits}")
    return 1 if any(item["severity"] == "error" for item in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
