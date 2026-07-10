#!/usr/bin/env python3
"""Install Codex Game Studios as a personal Skill and local plugin."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


PLUGIN_NAME = "codex-game-studios"
MARKETPLACE_NAME = f"{PLUGIN_NAME}-local"
SKILL_ITEMS = (
    "SKILL.md",
    "agents",
    "assets",
    "commands",
    "examples",
    "production",
    "references",
    "runtime",
    "scripts",
    "templates",
    "workflows",
)
PLUGIN_ITEMS = (
    ".codex-plugin",
    "SKILL.md",
    "agents",
    "assets",
    "commands",
    "examples",
    "production",
    "references",
    "runtime",
    "scripts",
    "skills",
    "templates",
    "workflows",
)


def get_codex_home(explicit: Path | None = None) -> Path:
    if explicit is not None:
        return explicit.expanduser()
    env_path = os.environ.get("CODEX_HOME")
    if env_path:
        return Path(env_path).expanduser()
    return Path.home() / ".codex"


def get_codex_executable(codex_home: Path) -> Path | None:
    env_path = os.environ.get("CODEX_CLI_PATH")
    candidates = []
    if env_path:
        candidates.append(Path(env_path).expanduser())
    candidates.extend(
        [
            codex_home / ".sandbox-bin" / "codex",
            codex_home / ".sandbox-bin" / "codex.exe",
        ]
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    for name in ("codex", "codex.exe"):
        resolved = shutil.which(name)
        if resolved:
            return Path(resolved).resolve()
    return None


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


def write_marketplace_manifest(marketplace_root: Path) -> None:
    manifest_path = marketplace_root / ".agents" / "plugins" / "marketplace.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": MARKETPLACE_NAME,
        "interface": {"displayName": "Local Codex Game Studios"},
        "plugins": [
            {
                "name": PLUGIN_NAME,
                "source": {"source": "local", "path": f"./plugins/{PLUGIN_NAME}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": "Productivity",
            }
        ],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def stage_plugin(repo_root: Path, plugin_root: Path) -> Path:
    for item in PLUGIN_ITEMS:
        copy_fresh_item(repo_root / item, plugin_root / item)
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["version"] = f"0.1.0+codex.{datetime.now().strftime('%Y%m%d%H%M%S')}"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_marketplace_manifest(plugin_root.parent.parent)
    return manifest_path


def register_local_plugin(codex_executable: Path, marketplace_root: Path) -> None:
    plugin_ref = f"{PLUGIN_NAME}@{MARKETPLACE_NAME}"
    subprocess.run(
        [str(codex_executable), "plugin", "remove", plugin_ref], check=False
    )
    subprocess.run(
        [str(codex_executable), "plugin", "marketplace", "remove", MARKETPLACE_NAME],
        check=False,
    )
    subprocess.run(
        [str(codex_executable), "plugin", "marketplace", "add", str(marketplace_root)],
        check=True,
    )
    subprocess.run(
        [str(codex_executable), "plugin", "add", plugin_ref], check=True
    )


def install(codex_home: Path | None = None) -> None:
    repo_root = Path(__file__).resolve().parent.parent
    codex_root = get_codex_home(codex_home)
    skill_root = codex_root / "skills" / PLUGIN_NAME
    marketplace_root = codex_root / "local-marketplaces" / PLUGIN_NAME
    plugin_root = marketplace_root / "plugins" / PLUGIN_NAME

    print(f"Installing Codex Game Studios Skill to: {skill_root}")
    for item in SKILL_ITEMS:
        copy_fresh_item(repo_root / item, skill_root / item)

    print(f"Syncing Codex Game Studios plugin to: {plugin_root}")
    stage_plugin(repo_root, plugin_root)

    codex_executable = get_codex_executable(codex_root)
    if codex_executable is None:
        print("Warning: Codex executable not found; files were synced but not registered.", file=sys.stderr)
        return
    register_local_plugin(codex_executable, marketplace_root)
    print("Codex Game Studios Skill and plugin installed successfully!")


if __name__ == "__main__":
    install()