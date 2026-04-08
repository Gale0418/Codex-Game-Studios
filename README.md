# Codex Game Studios

Use this pack when Codex needs a game-dev studio flow with clear routing, roles, and verification.
Use it as the default studio shell for new sessions and new subagents.

## 繁體中文

這是一套給 Codex 用的遊戲開發工作室骨架 (｀・ω・´)ゞ  
如果你想讓 Codex 先知道「怎麼開始、怎麼分波次、怎麼收回完成分身」，就從這包開始。

## English

This is a Codex-first game-dev studio shell (￣▽￣)  
Use it when you want Codex to know how to start, split work into waves, and close finished subagents cleanly.

## 日本語

これは Codex 向けのゲーム開発スタジオ用テンプレートです (｀・ω・´)ゞ  
開始方法、wave の分け方、完了した分身の回収方法をまとめています。

## Read first

- [references/codex-first.md](references/codex-first.md)
- [references/multi-agent-sop.md](references/multi-agent-sop.md)
- `SKILL.md`
- `AGENTS.md`
- `references/command-registry.md`
- `templates/agent-handoff.md`
- `templates/wave-plan.md`

## Use path

1. Run `/start`
2. If the state is unclear, run `/project-stage-detect`
3. If you need a clean handoff, run `/onboard`
4. Use `/help` when you need the next command

## Quick Notes

- Keep the wave goal explicit before opening subagents.
- Use `references/multi-agent-sop.md` as the default rotation model.
- Rotate one monitor per wave so the studio can self-check and self-correct.
- Close finished agents immediately.
- Save a short checkpoint after each wave.
- Keep the shortest safe entry in `references/codex-first.md`.

## 免責聲明

- 這個工作室套件是從 Claude Game Studio 的概念與結構改造而來，再由 Codex 協助整理成可直接使用的版本。
- 它的目標是讓 Codex 可以直接開箱使用、分波運作、輪流監工。
- 如果你在使用時遇到問題、缺頁、或流程不順，先回報給建立這個倉庫的人，不要直接怪文件自己跑掉 (￣▽￣)"

## Platform

- macOS/Linux: `settings.macos.json`
- Windows: `settings.windows.json`

## Validation

- macOS/Linux: `bash scripts/validate_studio.sh`
- Windows: `scripts\\validate_studio.cmd`

## Keep for later

- `commands/` for browsable command entries
- `workflows/` for the playbooks
- `runtime/` for policy and hooks
- `production/` for active state
- `templates/agent-handoff.md` and `templates/wave-plan.md` for wave targets and close conditions
- `templates/` and `examples/` only when you need output shapes or samples
