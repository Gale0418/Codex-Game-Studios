import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PYTHON = sys.executable


class RegistrySyncTests(unittest.TestCase):
    def test_generator_script_exists(self):
        self.assertTrue(
            (ROOT / "scripts" / "generate_dispatch_manifest.py").is_file()
        )

    def test_derived_docs_are_not_empty(self):
        index_text = (ROOT / "commands" / "index.md").read_text(encoding="utf-8")
        manifest_text = (ROOT / "runtime" / "dispatch-manifest.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("- `/start`", index_text)
        self.assertIn("- `/help`", index_text)
        self.assertIn("### Discovery", manifest_text)
        self.assertIn(
            "- Commands: `/start`, `/help`, `/project-stage-detect`, `/onboard`, `/adopt`",
            manifest_text,
        )

    def test_validator_uses_registry_as_source_of_truth(self):
        ps1 = (ROOT / "scripts" / "validate_studio.ps1").read_text(encoding="utf-8")
        sh = (ROOT / "scripts" / "validate_studio.sh").read_text(encoding="utf-8")
        self.assertNotIn("$WorkflowNames = @(", ps1)
        self.assertNotIn("workflow_names=(", sh)
        self.assertIn("command-registry.md", ps1)
        self.assertIn("command-registry.md", sh)

    def test_fast_entry_and_full_audit_are_documented(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        codex_first = (ROOT / "references" / "codex-first.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Fast Entry", skill)
        self.assertIn("Full Studio Audit", skill)
        self.assertIn("Fast Entry", codex_first)
        self.assertIn("Full Studio Audit", codex_first)

    def test_generated_docs_match_registry(self):
        result = subprocess.run(
            [
                PYTHON,
                str(ROOT / "scripts" / "generate_dispatch_manifest.py"),
                "--root",
                str(ROOT),
                "--check",
            ],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
