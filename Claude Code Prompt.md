# Claude Code — AI 每日简报生成指令

把下面整份内容粘贴给 Claude Code（或 `claude` CLI），它会根据今天搜集到的真实内容，生成一份可直接打开的 HTML 简报。

---

## 使用方法

1. 把 `AI Newsletter Terminal.html`（作为模板）放在你的工作目录
2. 在 Claude Code 里运行：`claude`
3. 把本文件从 `=== PROMPT START ===` 到 `=== PROMPT END ===` 之间的内容整段粘贴
4. Claude 会输出一份 `AI Daily YYYY-MM-DD.html`

---

=== PROMPT START ===

# 任务：生成今日 AI 简报 HTML

请根据今天（使用当前日期）搜集的 AI 行业情报，生成一份 HTML 简报，文件名格式：`AI Daily YYYY-MM-DD.html`。

## 视觉风格

**Terminal / 终端主题**（深色背景 + 等宽字体 + 薄荷绿强调色），但标题采用**编辑部式排版**（衬线斜体大字 + 手写体副标题）。具体样式参见下方完整模板。

## 内容结构（6 大板块，顺序固定）

| # | 板块 | 中文标题 | 条数 |
|---|------|----------|------|
| 01 | top_news | AI 热门要闻 | **5 条** |
| 02 | trending_repos | GitHub 飙升榜 | **6 条** |
| 03 | hot_skills | Skills 飙升榜 | **10 条** |
| 04 | tips | Claude Code 技巧 | **5 条** |
| 05 | token_leaderboard | OpenRouter 调用榜 TOP 10 | **10 条** |
| 06 | security_alerts | AI 安全事件 | **5 条** |

## 每块的数据字段

### 01 AI 热门要闻（5 条）
- `title`: 标题（中文，≤30 字）
- `blurb`: 2-3 句要点（中文，≤90 字）
- `source`: 来源（英文官方名，如 OpenAI Blog / The Verge / 36Kr）
- `time`: 相对时间（如 `2h` / `1d`）

### 02 GitHub 飙升榜（6 条）
- `repo`: `owner/repo` 格式
- `blurb`: 一句话描述（中文，≤55 字）
- `stars`: 近一周新增（如 `+4.2k`）
- `total`: 总 star 数（如 `38.1k`）
- `lang`: 主语言

### 03 Skills 飙升榜（10 条）
- `name`: skill 名（小写连字符）
- `blurb`: 一句话描述（中文，≤50 字）
- `uses`: 使用次数（如 `12.3k`）
- `author`: 作者 handle（如 `·jwang`，用 · 号不用 @，避免 Outlook 自动识别超链接）

### 04 Claude Code 技巧（5 条）
- `tip`: 标题（中文，≤20 字，可含 `<code>` 关键字）
- `body`: 解释 + 使用场景（中文，≤80 字）

### 05 OpenRouter 调用榜（10 条，来源：openrouter.ai/rankings）
- `rank`: 1-10
- `model`: 模型名
- `vendor`: 厂商
- `tokens`: 周调用量（如 `18.4B`）
- `change`: 环比 `+xx%` 或 `-xx%`
- `bar_pct`: 相对榜首的百分比（如榜首=100，第二=14.2/18.4×100=77）

### 06 AI 安全事件（5 条）
- `severity`: `high` / `medium` / `low`
- `title`: 标题（中文，≤26 字）
- `blurb`: 2 句描述 + 建议（中文，≤90 字）

## 数据获取来源

- **News**: OpenAI Blog / Anthropic News / DeepMind / The Verge / TechCrunch / 36Kr / 量子位
- **GitHub**: `https://github.com/trending?since=daily`（或 daily trending API）
- **Skills**: `https://claude.ai/skills` 或 Anthropic 官方榜单
- **Tips**: Claude Code 官方 docs + Anthropic cookbook + 社区经验
- **OpenRouter**: `https://openrouter.ai/rankings`（近 7 天 tokens）
- **Security**: CVE-MITRE / HuggingFace security / OpenAI security advisories / 安全社区

## 输出要求

1. **单一自包含 HTML 文件**：所有样式内联，无外部依赖（字体通过 Google Fonts CDN 加载）
2. **完全照搬模板的双布局结构**（MSO Outlook + iOS/现代客户端），只替换数据内容
   - Outlook：`<!--[if mso]>` table 布局
   - iOS/浏览器：`<!--[if !mso]><!-->` CSS flex/grid 布局
   - 所有颜色用十六进制，不用 CSS `var()`
3. **panel-hd 只显示编号和标题**，不要右侧 tag 注释（不含 `<span class="tag">`）
4. **masthead 中的期号**从 `issue_counter.txt` 读取并加 1
5. **日期使用当前真实日期**，格式 `YYYY / MM / DD`；tagline 下方加 14px 空行
6. **token bar 宽度**根据 `bar_pct` 百分比动态计算
7. **severity 颜色**：high=红、medium=黄、low=蓝

## HTML 模板（完整粘贴，改内容不改结构）

```html
<!-- 此处粘贴 AI Newsletter Terminal.html 的完整内容作为结构模板 -->
<!-- Claude Code 读取本地 AI Newsletter Terminal.html 作为模板参考 -->
```

请执行：
1. 读取当前目录下的 `AI Newsletter Terminal.html` 作为样式模板
2. 根据上述字段要求搜集今日真实数据（必要时使用 WebSearch / WebFetch）
3. 用真实内容替换模板中的占位数据，保持 DOM 结构完全一致
4. 输出新文件：`AI Daily YYYY-MM-DD.html`
5. 最后总结今日最值得关注的 3 条要点

=== PROMPT END ===

---

## 附：快速 CLI 写法

如果你想一句话触发，也可以：

```bash
claude "读取 AI Newsletter Terminal.html 作为模板，搜集今日（$(date +%Y-%m-%d)）的 AI 热门要闻 5 条、GitHub 飙升榜 6 条、最火 Skills 5 条、Claude Code 技巧 4 条、OpenRouter 调用榜 TOP 10、AI 安全事件 5 条，完全按模板的 DOM 结构替换内容，输出 AI Daily $(date +%Y-%m-%d).html"
```

## 数据字段速查（JSON schema）

```json
{
  "issue": 49,
  "date": "2026 / 04 / 27",
  "news": [
    { "title": "", "blurb": "", "source": "", "time": "2h" }
  ],
  "github": [
    { "repo": "owner/name", "blurb": "", "stars": "+4.2k", "total": "38.1k", "lang": "TypeScript" }
  ],
  "skills": [
    { "name": "skill-name", "blurb": "", "uses": "12.3k", "author": "·handle" }
  ],
  "tips": [
    { "tip": "", "body": "" }
  ],
  "tokens": [
    { "rank": 1, "model": "", "vendor": "", "tokens": "18.4B", "change": "+12%", "bar_pct": 100 }
  ],
  "security": [
    { "severity": "high|medium|low", "title": "", "blurb": "" }
  ]
}
```
