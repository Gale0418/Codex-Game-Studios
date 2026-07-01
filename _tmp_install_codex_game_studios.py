#!/usr/bin/env python3
"""Install Codex Game Studios as both a skill and a local Codex plugin."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


SKILL_ITEMS = (
    "SKILL.md",
    "agents",
    "assets",
    "commands",
    "workflows",
    "references",
    "runtime",
    "production",
    "templates",
    "scripts",
    "examples",
    ".claude",
    "LICENSE",
    "README.md",
    "README.en.md",
    "README.zh-TW.md",
    "README.ja.md",
)

PLUGIN_ITEMS = (
    ".codex-plugin",
    "SKILL.md",
    "agents",
    "assets",
    "commands",
    "workflows",
    "references",
    "runtime",
    "production",
    "templates",
    "scripts",
    "examples",
    "skills",
    ".claude",
    "LICENSE",
    "README.md",
    "README.en.md",
    "README.zh-TW.md",
    "README.ja.md",
)


def copy_fresh_item(source: Path, destination: Path) -> None:
    if not source.exists():
        return

    if destination.exists() or destination.is_symlink():
        if destination.is_dir() and not destination.is_symlink():
            shutil.rmtree(destination)
        else:
            destination.unlink()

    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)


def get_codex_home() -> Path:
    env_path = os.environ.get("CODEX_HOME")
    if env_path:
        return Path(env_path).expanduser()
    return Path.home() / ".codex"


def get_codex_executable(codex_home: Path) -> Path | None:
    for candidate in (
        codex_home / ".sandbox-bin" / "codex",
        codex_home / ".sandbox-bin" / "codex.exe",
    ):
        if candidate.exists():
            return candidate

    for name in ("codex", "codex.exe"):
        resolved = shutil.which(name)
        if resolved:
            return Path(resolved)

    return None


def run_native_or_throw(executable: Path, *arguments: str) -> None:
    subprocess.run([str(executable), *arguments], check=True)


def main() -> int:
    source_root = Path(__file__).resolve().parent
    codex_home = get_codex_home()
    codex_executable = get_codex_executable(codex_home)

    skill_root = codex_home / "skills" / "codex-game-studios"
    marketplace_root = codex_home / "local-marketplaces" / "codex-game-studios"
    marketplace_manifest_path = marketplace_root / ".agents" / "plugins" / "marketplace.json"
    plugin_root = marketplace_root / "plugins" / "codex-game-studios"
    installed_plugin_manifest_path = plugin_root / ".codex-plugin" / "plugin.json"

    print(f"Installing personal skill from {source_root} to {skill_root}")
    for item in SKILL_ITEMS:
        copy_fresh_item(source_root / item, skill_root / item)

    print(f"Syncing local plugin package to {plugin_root}")
    for item in PLUGIN_ITEMS:
        copy_fresh_item(source_root / item, plugin_root / item)

    plugin_manifest = json.loads(installed_plugin_manifest_path.read_text(encoding="utf-8"))
    plugin_manifest["version"] = f"0.1.0+codex.{datetime.now().strftime('%Y%m%d%H%M%S')}"
    installed_plugin_manifest_path.write_text(
        json.dumps(plugin_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    marketplace_manifest = {
        "name": "codex-game-studios-local",
        "interface": {"displayName": "Local Codex Game Studios"},
        "plugins": [
            {
                "name": "codex-game-studios",
                "source": {
                    "source": "local",
                    "path": "./plugins/codex-game-studios",
                },
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Productivity",
            }
        ],
    }
    marketplace_manifest_path.parent.mkdir(parents=True, exist_ok=True)
    marketplace_manifest_path.write_text(
        json.dumps(marketplace_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if codex_executable is None:
        print("Warning: Codex executable not found; local plugin files were synced but not registered.", file=sys.stderr)
        print("Install completed.")
        return 0

    print(f"Registering marketplace with {codex_executable}")
    run_native_or_throw(codex_executable, "plugin", "marketplace", "add", str(marketplace_root))
    print("Installing or refreshing local plugin codex-game-studios@codex-game-studios-local")
    run_native_or_throw(codex_executable, "plugin", "add", "codex-game-studios@codex-game-studios-local")
    print("Install completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
