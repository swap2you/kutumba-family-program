# Reading KUTUMBA Documents

How to use the rendered Markdown reading experience in Cursor / VS Code.

## First-time setup

1. Close any old raw Markdown tabs for KUTUMBA files.
2. `Ctrl+Shift+P` → **Developer: Reload Window**
3. Reopen a document from [KUTUMBA-READER-HOME.md](../KUTUMBA-READER-HOME.md)

Workspace settings open `.md` files in **Markdown Preview** by default (see `.vscode/settings.json`).

## Preview shortcuts

| Action | Shortcut |
|---|---|
| Open preview | `Ctrl+Shift+V` |
| Side-by-side preview | `Ctrl+K`, then `V` |
| Headings in this file | `Ctrl+Shift+O` |
| Headings across workspace | `Ctrl+T` |

## Alternative: Reopen Editor With

Right-click the file tab → **Reopen Editor With...** → **Markdown Preview**

## Return to text mode

Right-click tab → **Reopen Editor With...** → **Text Editor**

## Mermaid diagrams

Open `visuals/concept-map.md` or `visuals/process-flow.md` (not standalone `.mmd` files) for rendered diagrams.

## Public GitHub rendering

Browse [github.com/swap2you/kutumba-family-program](https://github.com/swap2you/kutumba-family-program) for read-only web rendering without local setup.

## Styling

Preview uses `.vscode/kutumba-markdown.css` — readable width, tables, blockquotes, print-friendly.

No third-party Markdown extension is required.
