#!/usr/bin/env python3
"""
Python E2E Smoke Integration Test for Codex Game Studios.
"""

import unittest
from pathlib import Path
import sys

repo_root = Path(__file__).resolve().parent.parent

class TestGameStudiosE2ESmoke(unittest.TestCase):
    def test_core_files_exist(self):
        self.assertTrue((repo_root / "SKILL.md").exists())
        self.assertTrue((repo_root / "README.zh-TW.md").exists())
        self.assertTrue((repo_root / "agents").exists())
        self.assertTrue((repo_root / "commands").exists())
        self.assertTrue((repo_root / "workflows").exists())

if __name__ == "__main__":
    unittest.main()
