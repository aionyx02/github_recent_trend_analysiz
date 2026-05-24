# Extracted Workflow From Reference Project

## 抽出的工作流骨架

參考專案的 context engineering 不是單純的 prompt engineering，而是把 AI 可用上下文拆成多層文件：

| 層級 | 檔案 | 用途 |
|---|---|---|
| Bootstrap | `CLAUDE.md` | 每次 session 的最小啟動規則 |
| Governance | `docs/CLAUDE.md` | 文件路由、ADR、衝突處理、更新規則 |
| Router | `docs/index.md` | 文件地圖與按意圖檢索規則 |
| Stable facts | `docs/project.md` | 專案長期不常變資訊 |
| Current state | `docs/memory/current.md` | 目前策略、焦點、限制、下一步 |
| Task state | `docs/tasks/active.md` | 現在正在做什麼 |
| Detailed task plan | `docs/tasks/*.md` | 較大的 task plan、done criteria、non-goals |
| Decision records | `docs/adr/*.md` | 架構、安全、schema、依賴等決策 |
| Historical log | `docs/memory/sessions/*.md` | 執行紀錄、debug narrative、命令輸出 |
| Generated summaries | `docs/state/*.json` | 給 AI 快速讀取的壓縮狀態 |
| Guard scripts | `scripts/docs-*.mjs` | 防止文件膨脹、前置資料錯誤、狀態不同步 |

## 關鍵設計模式

### 1. Retrieval-first，不做 full-doc prompt dump

AI 不應該一開始遞迴讀完 `docs/`。正確流程是：

```text
CLAUDE.md -> docs/index.md -> current.md + active.md -> task-specific docs
```

### 2. Current state 與 history 分離

`current.md` 和 `active.md` 只保存目前狀態。詳細敘事、debug 過程、命令輸出都進 session log。

### 3. ADR 是架構變更的門檻

只要涉及核心依賴、資料格式、安全邊界、IPC/API contract、重大演算法，就先寫 ADR。AI 可以提出 `proposed` ADR，但不應自行標成 `accepted`。

### 4. 文件衝突有優先序

建議優先序：

1. 使用者當前明確指令
2. `docs/tasks/active.md`
3. `docs/memory/current.md`
4. accepted ADR
5. `docs/security.md`
6. `docs/architecture.md`
7. sessions / archive

### 5. Guard scripts 是路由回饋

檢查失敗不只是格式錯誤，而是在提醒：這段內容可能放錯地方。例如把長篇 execution narrative 寫進 `current.md`，就會被 narrative check 擋下。

## 通用化後的差異

本模板移除了原專案的 Tauri / React / Rust 特定內容，保留：

- 文件拓撲
- 啟動與收尾流程
- ADR 規則
- 狀態與歷史分流
- 檢查 scripts
- task / memory / decision summary 產生方式
