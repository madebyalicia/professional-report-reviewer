#!/usr/bin/env python3
"""Deterministic scanner regressions; these do not test model review behavior."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

SPEC = importlib.util.spec_from_file_location("clean_draft_lint", Path(__file__).with_name("clean_draft_lint.py"))
lint_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lint_module)


def blocks(*items):
    return [{"text": text, "level": level, "where": f"item {i}"} for i, (level, text) in enumerate(items)]


class ScannerRegression(unittest.TestCase):
    def test_product_version_is_not_editorial_residue(self):
        self.assertEqual(lint_module.lint(blocks((None, "本版本新增语音中断功能。"))), [])

    def test_english_editorial_note_is_candidate_not_automatic_error(self):
        findings = lint_module.lint(blocks((None, "Reviewer note: revise the original claim.")))
        self.assertTrue(any(f["kind"] == "editorial_residue" for f in findings))
        self.assertTrue(all(f["severity"] == "warning" for f in findings))

    def test_chinese_heading_gap(self):
        findings = lint_module.lint(blocks((1, "一、市场"), (1, "三、结论")))
        self.assertTrue(any(f["kind"] == "heading_sequence" for f in findings))

    def test_chinese_chapter_sequence(self):
        self.assertEqual(lint_module.lint(blocks((1, "第一章 市场"), (1, "第二章 结论"))), [])

    def test_third_level_gap(self):
        findings = lint_module.lint(blocks((1, "1 市场"), (2, "1.1 用户"), (3, "1.1.1 测试"), (3, "1.1.3 结论")))
        self.assertTrue(any(f["match"] == "1.1.3" for f in findings))

    def test_valid_nested_numbering_and_document_title(self):
        self.assertEqual(lint_module.lint(blocks((1, "报告标题"), (2, "1 市场"), (3, "1.1 用户"), (4, "1.1.1 测试"), (4, "1.1.2 结论"), (3, "1.2 竞品"), (2, "2 建议"))), [])

    def test_wrong_parent_and_duplicate(self):
        findings = lint_module.lint(blocks((1, "1 市场"), (2, "1.1 用户"), (1, "2 建议"), (3, "1.1.1 旧父级"), (1, "2 重复")))
        self.assertGreaterEqual(sum(f["kind"] == "heading_sequence" for f in findings), 2)

    def test_body_list_not_misclassified_as_heading(self):
        self.assertEqual(lint_module.lint(blocks((None, "一、检查素材"), (None, "三、这是引用中的一个项目"))), [])

    def test_markdown_loading_detects_chinese_gap(self):
        with tempfile.TemporaryDirectory(prefix="report-lint-test-") as temp:
            path = Path(temp) / "headings.md"
            path.write_text("# 一、市场\n# 三、结论\n", encoding="utf-8")
            findings = lint_module.lint(lint_module.load_blocks(path))
            self.assertTrue(any(f["kind"] == "heading_sequence" for f in findings))

    def test_docx_loading_checks_table_residue_and_heading_sequence(self):
        namespace = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        document = f'''<w:document xmlns:w="{namespace}"><w:body>
          <w:p><w:pPr><w:pStyle w:val="H1"/></w:pPr><w:r><w:t>一、市场</w:t></w:r></w:p>
          <w:p><w:pPr><w:pStyle w:val="H1"/></w:pPr><w:r><w:t>三、结论</w:t></w:r></w:p>
          <w:tbl><w:tr><w:tc><w:p><w:r><w:t>Reviewer note: revise this cell.</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
        </w:body></w:document>'''
        styles = f'<w:styles xmlns:w="{namespace}"><w:style w:styleId="H1"><w:name w:val="Heading 1"/></w:style></w:styles>'
        with tempfile.TemporaryDirectory(prefix="report-lint-test-") as temp:
            path = Path(temp) / "minimal.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", document)
                archive.writestr("word/styles.xml", styles)
            findings = lint_module.lint(lint_module.load_blocks(path))
            self.assertTrue(any(f["kind"] == "heading_sequence" for f in findings))
            self.assertTrue(any(f["kind"] == "editorial_residue" and "table" in f["where"] for f in findings))

    def run_cli(self, source, revised, *flags):
        with tempfile.TemporaryDirectory(prefix="report-lint-test-") as temp:
            src = Path(temp) / "source.md"
            dst = Path(temp) / "revised.md"
            src.write_text(source, encoding="utf-8")
            dst.write_text(revised, encoding="utf-8")
            stdout = io.StringIO()
            with patch.object(sys, "argv", ["clean_draft_lint", str(dst), "--source", str(src), "--json", *flags]), contextlib.redirect_stdout(stdout):
                code = lint_module.main()
            return code, json.loads(stdout.getvalue())

    def test_equal_length_does_not_claim_meaning_preservation(self):
        code, result = self.run_cli("建议保留直营渠道", "建议取消直营渠道")
        self.assertEqual(code, 0)
        self.assertEqual(result["scope_metrics"]["ratio"], 1.0)
        self.assertIs(result["scope_metrics"]["meaning_preservation_assessed"], False)
        self.assertEqual(result["status"], "limited_scan_passed")
        self.assertIn("no semantic", result["limitations"])

    def test_shortening_is_warning_not_quota_or_authorization(self):
        code, result = self.run_cli("已有事实与详细案例" * 10, "已有事实")
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "review_candidates")
        self.assertTrue(any(f["kind"] == "length_reduction_review" and f["severity"] == "warning" for f in result["findings"]))

    def test_legacy_flag_does_not_change_authority(self):
        _, before = self.run_cli("详细案例" * 20, "案例")
        _, after = self.run_cli("详细案例" * 20, "案例", "--allow-material-reduction")
        self.assertEqual(before["findings"], after["findings"])


if __name__ == "__main__":
    unittest.main()
