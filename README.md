# Codex Game Studios

> "It ain't perfect, but it's honest work." (´・ω・`)a

Use this pack when Codex needs a game-dev studio flow with clear routing, roles, and verification.
Use it as the default studio shell for new sessions and new subagents.


<a id="zh-tw"></a>

<p align="center">
  <a href="#zh-tw">🇹🇼 繁中</a> · <a href="#english">🇺🇸 English</a> · <a href="#ja">🇯🇵 日本語</a>
</p>

## 🚀 安裝方式

如果你想讓別人的 Codex 也能直接用這套工作室，先把這個 GitHub repo 裝成 skill。

1. 打開 repo：`https://github.com/Gale0418/Codex-Game-Studios`
2. 用你的 Codex skill installer 安裝它
3. 如果你的環境沒有 installer，就把整個資料夾放進 `~/.codex/skills/codex-game-studios/`
4. 重新啟動 Codex，讓它重新掃描 skills
5. 新會話先跑 `/start`

<a id="english"></a>
English:

1. Open the repo: `https://github.com/Gale0418/Codex-Game-Studios`
2. Install it with your Codex skill installer
3. If you do not have an installer, copy the folder into `~/.codex/skills/codex-game-studios/`
4. Restart Codex so it rescans skills
5. Start a new session with `/start`

## 🤖 自動判斷模式
<a id="ja"></a>

如果你不知道該用哪個指令，也可以直接把需求丟給 AI，讓它自己判斷流程並自動往下跑。
你不用先背 `/start`、`/project-stage-detect`、`/onboard`，因為這套工作室會先看情況，再決定要走哪條 lane。

English:

If you do not know which command to use, just give the request to the AI and let it choose the next safe workflow.
You do not need to memorize `/start`, `/project-stage-detect`, or `/onboard` first.

日本語:

どのコマンドを使えばいいか分からないときは、AI にそのまま依頼して大丈夫です。
`/start` や `/project-stage-detect` を覚えていなくても、AI が状況を見て安全な流れを選びます。

## 🕹️ 如何呼叫

如果你已經把這個 skill 掛進 Codex，最簡單的用法就是直接丟任務，不必先背流程。

你可以這樣講：

- `請用 codex-game-studios skill 幫我看這個專案`
- `用工作室模式 review 這個五子棋遊戲`
- `直接幫我判斷這個任務要不要開多 agent`
- `幫我用自動判斷模式整理這份 README`

如果 Codex 沒有自動抓到 skill，就補一句：

- `用 codex-game-studios skill`
- `請以工作室流程處理`

English:

- `Please use the codex-game-studios skill to review this project.`
- `Use the studio workflow to inspect this game.`
- `Decide whether this task needs parallel agents.`

日本語:

- `codex-game-studios skill を使ってこのプロジェクトを見てください。`
- `ワークフローに従ってこのゲームを確認してください。`
- `このタスクに並列エージェントが必要か判断してください。`

日本語:

1. この repo を開く: `https://github.com/Gale0418/Codex-Game-Studios`
2. Codex の skill installer でインストールする
3. installer がない場合は `~/.codex/skills/codex-game-studios/` に配置する
4. Codex を再起動して skills を再スキャンする
5. 新しいセッションでは `/start` から始める

## 繁體中文

這是一套給 Codex 用的遊戲開發工作室骨架 (｀・ω・´)ゞ  
如果你想讓 Codex 先知道「怎麼開始、怎麼分波次、怎麼收回完成分身」，就從這包開始。  
說白了，它不是很花俏，但它很誠實，也真的能跑。

## English

This is a Codex-first game-dev studio shell (￣▽￣)  
Use it when you want Codex to know how to start, split work into waves, and close finished subagents cleanly.  
It is not fancy, but it is organized enough to keep the studio from falling apart.

## 日本語

これは Codex 向けのゲーム開発スタジオ用テンプレートです (｀・ω・´)ゞ  
開始方法、wave の分け方、完了した分身の回収方法をまとめています。  
完璧ではないけど、少なくとも迷子にはなりにくいはずです。

## 📚 Read First

- [references/codex-first.md](references/codex-first.md)
- [references/multi-agent-sop.md](references/multi-agent-sop.md)
- `SKILL.md`
- `AGENTS.md`
- `references/command-registry.md`
- `templates/agent-handoff.md`
- `templates/wave-plan.md`

## 🚦 Use Path

1. Run `/start`
2. If the state is unclear, run `/project-stage-detect`
3. If you need a clean handoff, run `/onboard`
4. Use `/help` when you need the next command

## 🧠 Quick Notes

- Keep the wave goal explicit before opening subagents.
- Use `references/multi-agent-sop.md` as the default rotation model.
- Rotate one monitor per wave so the studio can self-check and self-correct.
- Close finished agents immediately.
- Save a short checkpoint after each wave.
- Keep the shortest safe entry in `references/codex-first.md`.
- If a wave gets messy, stop and re-route instead of pretending it is fine. That trick never works (￣▽￣)

## 免責聲明

- 這個工作室套件是從 Claude Game Studio 的概念與結構改造而來，再由 Codex 協助整理成可直接使用的版本。
- 它的目標是讓 Codex 可以直接開箱使用、分波運作、輪流監工。
- 如果你在使用時遇到問題、缺頁、或流程不順，先回報給建立這個倉庫的人，不要直接怪文件自己跑掉 (￣▽￣)"

## 🖥️ Platform

- macOS/Linux: `settings.macos.json`
- Windows: `settings.windows.json`

## ✅ Validation

- macOS/Linux: `bash scripts/validate_studio.sh`
- Windows: `scripts\\validate_studio.cmd`

## License

- MIT License
- See [LICENSE](LICENSE)

## 📎 Keep for Later

- `commands/` for browsable command entries
- `workflows/` for the playbooks
- `runtime/` for policy and hooks
- `production/` for active state
- `templates/agent-handoff.md` and `templates/wave-plan.md` for wave targets and close conditions
- `templates/` and `examples/` only when you need output shapes or samples
