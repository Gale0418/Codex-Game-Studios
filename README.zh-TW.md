# Codex Game Studios 遊戲工作室自動化外掛

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![Game Engine](https://img.shields.io/badge/Engine-Godot%20%7C%20Unity%20%7C%20Web-orange.svg)]()

<p align="center">
  <a href="README.md">🇺🇸 English</a> · <a href="README.zh-TW.md">🇹🇼 繁體中文</a> · <a href="README.ja.md">🇯🇵 日本語</a>
</p>

**Codex Game Studios** 是一套專為遊戲開發打造的 AI 工作室工作流框架與 Skill / Plugin。它整合了遊戲企劃、Godot / Unity 引擎開發、美術資材去背導出、音效設計與 CodeReview 稽核流程，協助開發者完成遊戲開發閉環。

---

## 💡 核心特色

- **遊戲工作室角色調度 (Multi-Agent Roster)**：內建企劃 (Planner)、工程 (Developer)、美術/去背 (Artist)、音效 (Audio) 與稽核 (Reviewer) 等角色範本。
- **Godot / Unity 雙引擎適配**：提供 Godot 4.x (GDScript) 與 Unity (C#) 的專案結構範本、自動化測試與資材載入規範。
- **資材與圖資去背工作流**：整合透明 Sprite Sheet 去背導出規範，自動對接邊緣延展 (Extrude & Padding) 與 JSON 座標對應。
- **分波次監工與執行紀律**：自動判定極簡流程或多 Agent 協作模式，避免一次性過度更動專案。

---

## 🏗️ 專案目錄結構

```text
codex-game-studios/
├── .codex-plugin/           # Codex 外掛定義檔
├── SKILL.md                 # 核心技能規範
├── README.md                # 英文說明文件
├── README.zh-TW.md          # 繁體中文說明文件
├── README.ja.md             # 日本語說明文件
├── agents/                  # 工作室 Agent 角色定義
├── commands/                # 快速指令與流程引導
├── examples/                # 範例遊戲架構與資材規範
├── production/              # 導出與構建作業規範
├── templates/               # 遊戲專案範本 (Godot / Unity)
├── workflows/               # 遊戲開發工作流 (企劃/開發/測試/去背)
└── scripts/                 # 自動化安裝與驗證腳本
```

---

## 🚀 快速開始與安裝

### 一鍵安裝 (Windows / macOS / Linux)

```powershell
# PowerShell (Windows / macOS)
pwsh -ExecutionPolicy Bypass -File ./scripts/install.ps1

# Python (跨平台 CLI)
python3 scripts/install.py
```

### 呼叫方式

在 Codex 中直接輸入：

```text
請使用 $codex-game-studios 幫我規劃這個 Godot 遊戲專案的工作室開發流程。
```

---

## 📄 授權條款

本專案採用 [MIT License](LICENSE) 條款開源發布。
