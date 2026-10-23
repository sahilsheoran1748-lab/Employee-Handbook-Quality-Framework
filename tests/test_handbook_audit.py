import json
import sys
import unittest
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from src.handbook_audit import (
    normalize_text,
    extract_document_structure,
    check_main_heading_numbering,
)

class TestHandbookAudit(unittest.TestCase):

    def test_normalize_text(self):
        self.assertEqual(normalize_text("  Hello   World  "), "Hello World")

    def test_normalize_empty_text(self):
        self.assertEqual(normalize_text(""), "")

    def test_extracted_content_exists(self):
        path = PROJECT_DIR / "data/processed/extracted_handbook_content.json"
        self.assertTrue(path.exists(), "Extracted handbook JSON is missing")

    def test_extracted_content_structure(self):
        path = PROJECT_DIR / "data/processed/extracted_handbook_content.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(data, dict)
        self.assertTrue(data, "Extracted handbook JSON is empty")

    def test_project_configuration(self):
        path = PROJECT_DIR / "project_config.json"
        self.assertTrue(path.exists(), "Project configuration is missing")
        config = json.loads(path.read_text(encoding="utf-8"))
        self.assertTrue(config)

    def test_readme_exists(self):
        self.assertTrue((PROJECT_DIR / "README.md").exists())

    def test_requirements_exists(self):
        self.assertTrue((PROJECT_DIR / "requirements.txt").exists())

if __name__ == "__main__":
    unittest.main(verbosity=2)
