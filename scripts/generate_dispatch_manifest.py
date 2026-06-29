#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
import sys

CATEGORY_ORDER = ["Discovery", "Planning", "Design", "Build", "Verify", "Ship"]
REQUIRED_WORKFLOW_SECTIONS = [
    "Primary lane",
    "Inputs",
    "Steps",
    "Outputs",
    "Exit criteria",
    "Template",
]


@dataclass
class CommandEntry:
    command: str
    aliases: list[str]
    workflow: str
    routing: str

    @property
    def command_name(self) -> str:
        return self.command.lstrip("/")

    @property
    def alias_names(self) -> list[str]:
        return [alias.lstrip("/") for alias in self.aliases]


def strip_code(value: str) -> str:
    return value.strip().strip("`")


def parse_aliases(value: str) -> list[str]:
    stripped = value.strip()
    if stripped == "-":
        return []
    return [strip_code(part) for part in stripped.split(",") if strip_code(part)]


def parse_registry(path: Path) -> OrderedDict[str, list[CommandEntry]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    data: OrderedDict[str, list[CommandEntry]] = OrderedDict((category, []) for category in CATEGORY_ORDER)
    current_category: str | None = None
    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        if line.startswith("## "):
            heading = line[3:].strip()
            current_category = heading if heading in data else None
            index += 1
            continue
        if current_category and line.startswith("| Command | Aliases | Workflow | Routing |"):
            index += 2
            while index < len(lines) and lines[index].startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip("|").split("|")]
                if len(cells) == 4:
                    data[current_category].append(
                        CommandEntry(
                            command=strip_code(cells[0]),
                            aliases=parse_aliases(cells[1]),
                            workflow=strip_code(cells[2]),
                            routing=cells[3].strip(),
                        )
                    )
                index += 1
            continue
        index += 1
    return data


def format_command_index(data: OrderedDict[str, list[CommandEntry]]) -> str:
    lines = [
        "# Command Index",
        "",
        "## Canonical source",
        "",
        "- `references/command-registry.md`",
        "",
        "## Use this page",
        "",
        "- Navigation view only.",
        "- This index mirrors every canonical command in the registry.",
        "- Update the registry first, then refresh this page.",
        "",
    ]
    for category, entries in data.items():
        lines.append(f"## {category}")
        lines.append("")
        for entry in entries:
            alias_text = f" (aliases: {', '.join(f'`{alias}`' for alias in entry.aliases)})" if entry.aliases else ""
            lines.append(f"- `{entry.command}`{alias_text} -> `{entry.workflow}`")
        lines.append("")
    lines.extend([
        "## Notes",
        "",
        "- Open the matching workflow after you pick the command.",
        "",
    ])
    return "\n".join(lines)


def format_dispatch_manifest(data: OrderedDict[str, list[CommandEntry]]) -> str:
    lines = [
        "# Dispatch Manifest",
        "",
        "## Canonical source",
        "",
        "- `references/command-registry.md` is the source of truth.",
        "- This file is a derived routing summary generated from the registry.",
        "",
        "## Fast Entry",
        "",
        "- Read the target workspace `AGENTS.md` only when that workspace provides one.",
        "- Then read `SKILL.md` and `references/codex-first.md`.",
        "- Pick exactly one command lane and open the matching workflow before expanding into broader runtime docs.",
        "",
        "## Full Studio Audit",
        "",
        "- Use this heavier path for broad, risky, release, migration, or refactor work.",
        "- Add `references/command-registry.md`, `runtime/execution-policy.md`, `runtime/session-lifecycle.md`, `runtime/hook-map.md`, `production/stage.txt`, and `production/active.md`.",
        "",
        "## Routing map",
        "",
    ]
    for category, entries in data.items():
        commands = ", ".join(f"`{entry.command}`" for entry in entries)
        workflows = ", ".join(f"`{entry.workflow}`" for entry in entries)
        lines.extend([
            f"### {category}",
            "",
            f"- Commands: {commands}",
            f"- Workflows: {workflows}",
        ])
        for entry in entries:
            alias_text = f"; aliases: {', '.join(entry.aliases)}" if entry.aliases else ""
            lines.append(f"- `{entry.command}` routes through `{entry.workflow}`{alias_text}; {entry.routing}")
        lines.append("")
    lines.extend([
        "## Handoff",
        "",
        "- Every lane returns `findings`, `risks`, `files`, and `recommended_next_step`.",
        "- The command file chooses the route.",
        "- The workflow file explains the steps.",
        "",
    ])
    return "\n".join(lines)


def validate_registry_structure(root: Path, data: OrderedDict[str, list[CommandEntry]]) -> list[str]:
    errors: list[str] = []
    registered_workflows: set[str] = set()
    registered_commands: set[str] = set()
    for entries in data.values():
        for entry in entries:
            workflow_path = root / entry.workflow
            registered_workflows.add(Path(entry.workflow).name)
            if not workflow_path.is_file():
                errors.append(f"missing workflow: {workflow_path}")
            else:
                content = workflow_path.read_text(encoding="utf-8")
                for section in REQUIRED_WORKFLOW_SECTIONS:
                    if f"## {section}" not in content:
                        errors.append(f"missing section {section} in {workflow_path}")
            command_path = root / "commands" / f"{entry.command_name}.md"
            registered_commands.add(command_path.name)
            if not command_path.is_file():
                errors.append(f"missing command: {command_path}")
            for alias_name in entry.alias_names:
                alias_path = root / "commands" / f"{alias_name}.md"
                alias_workflow_path = root / "workflows" / f"{alias_name}.md"
                registered_commands.add(alias_path.name)
                registered_workflows.add(alias_workflow_path.name)
                if not alias_path.is_file():
                    errors.append(f"missing alias command: {alias_path}")
    actual_workflows = {path.name for path in (root / "workflows").glob("*.md")}
    actual_commands = {path.name for path in (root / "commands").glob("*.md")}
    missing_from_registry_workflows = sorted(actual_workflows - registered_workflows)
    missing_from_registry_commands = sorted(actual_commands - registered_commands - {"index.md"})
    if missing_from_registry_workflows:
        errors.append("unregistered workflows: " + ", ".join(missing_from_registry_workflows))
    if missing_from_registry_commands:
        errors.append("unregistered commands: " + ", ".join(missing_from_registry_commands))
    return errors


def compare_or_write(path: Path, content: str, check: bool) -> list[str]:
    errors: list[str] = []
    normalized = content.rstrip() + "\n"
    if check:
        current = path.read_text(encoding="utf-8")
        if current != normalized:
            errors.append(f"out-of-date derived file: {path}")
    else:
        path.write_text(normalized, encoding="utf-8", newline="\n")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    registry = parse_registry(root / "references" / "command-registry.md")
    errors = validate_registry_structure(root, registry)
    errors.extend(compare_or_write(root / "commands" / "index.md", format_command_index(registry), check=args.check))
    errors.extend(compare_or_write(root / "runtime" / "dispatch-manifest.md", format_dispatch_manifest(registry), check=args.check))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
