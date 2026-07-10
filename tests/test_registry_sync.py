import importlib.util
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).parents[1]
PYTHON = sys.executable
INSTALLER = ROOT / "scripts" / "install.py"


def load_installer():
    spec = importlib.util.spec_from_file_location("codex_game_studios_installer", INSTALLER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RegistrySyncTests(unittest.TestCase):
    def test_installer_stages_icon_bearing_local_plugin(self):
        installer = load_installer()
        codex_home = Path(r"D:\MyGame\_tmp_codex_game_studios_installer")
        shutil.rmtree(codex_home, ignore_errors=True)
        self.addCleanup(shutil.rmtree, codex_home, ignore_errors=True)

        with patch.object(installer, "get_codex_executable", return_value=None):
            installer.install(codex_home=codex_home)

        skill_root = codex_home / "skills" / "codex-game-studios"
        plugin_root = (
            codex_home
            / "local-marketplaces"
            / "codex-game-studios"
            / "plugins"
            / "codex-game-studios"
        )
        marketplace_manifest = (
            plugin_root.parent.parent / ".agents" / "plugins" / "marketplace.json"
        )

        self.assertTrue((skill_root / "SKILL.md").is_file())
        self.assertTrue((plugin_root / "assets" / "icon-small.svg").is_file())
        self.assertTrue((plugin_root / "assets" / "logo-large.svg").is_file())
        self.assertTrue((plugin_root / ".codex-plugin" / "plugin.json").is_file())
        self.assertTrue(marketplace_manifest.is_file())

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
        self.assertIn(
            "$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)",
            ps1,
        )
        self.assertNotIn("$Root = Split-Path -Parent $MyInvocation.MyCommand.Path`n`nfunction Fail", ps1)
        self.assertIn("windowsapps", ps1.lower())

    def test_install_docs_and_validators_do_not_require_temp_installer(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        ps1 = (ROOT / "scripts" / "validate_studio.ps1").read_text(encoding="utf-8")
        sh = (ROOT / "scripts" / "validate_studio.sh").read_text(encoding="utf-8")

        self.assertIn("scripts/install.py", readme)
        self.assertIn("Skill and plugin", readme)
        self.assertNotIn("_tmp_install_codex_game_studios.py", readme)
        self.assertNotIn("_tmp_install_codex_game_studios.py", ps1)
        self.assertNotIn("_tmp_install_codex_game_studios.py", sh)
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
