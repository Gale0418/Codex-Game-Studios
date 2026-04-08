# Codex Game Studios 指南

## 目的

- 這個倉庫是給 Codex 使用的遊戲開發工作室套件。
- 優先目標不是文件華麗，而是讓 Codex 能快速看懂、正確路由、穩定驗證。

## 先讀哪些

1. `SKILL.md`
2. `README.md`
3. `references/codex-first.md`
4. `references/command-registry.md`
5. `workflows/start.md`
6. `workflows/help.md`
7. `runtime/dispatch-manifest.md`
8. `runtime/execution-policy.md`
9. `runtime/session-lifecycle.md`
10. `runtime/hook-map.md`
11. `templates/agent-handoff.md`
12. `templates/wave-plan.md`

## 做事順序

- 先判斷任務屬於 `intake`、`architecture`、`implementation`、`QA`、`docs`、`release` 哪一類。
- 先讀最小可用文件集合，再決定要不要展開更多參考檔。
- 先走 `/start`，不確定狀態就跑 `/project-stage-detect`，要整理新手入口就跑 `/onboard`。
- 需要命令導覽時用 `/help`，命令來源以 `references/command-registry.md` 為準。

## 分派規則

- 廣泛或高風險任務先做控制平面判斷，再決定是否拆 agent。
- 每條 lane 先指定一個 owner，再視需要加一個 helper，最後由一個 integrator 收尾。
- 以 wave 為單位工作：只開本波需要的 agent，完成的 agent 要立刻關閉，槽位緊張時先回收完成分身再開下一波。
- 每波結束先留短 checkpoint，讓下一波可以乾淨接手。
- 優先保留窄 diff，不要為了順手而大改無關區塊。

## 驗證

- Windows：`scripts\validate_studio.cmd`
- macOS / Linux：`bash scripts/validate_studio.sh`
- 如果驗證缺少平台，就明確標記，不要假裝已經實測。

## 文件原則

- `README.md` 和 `references/codex-first.md` 負責告訴 Codex 先看什麼。
- `commands/`、`workflows/`、`runtime/`、`production/` 是主要執行面。
- `templates/`、`examples/`、`.claude/docs/`、`.claude/rules/` 只在真的需要輸出樣板或相容層時才打開。
