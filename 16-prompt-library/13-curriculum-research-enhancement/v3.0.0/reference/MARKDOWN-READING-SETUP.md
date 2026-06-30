# Reading Markdown Comfortably in Cursor / VS Code

No plugin is required.

## Open rendered preview

- Windows/Linux: `Ctrl+Shift+V`
- Preview to the side: `Ctrl+K`, then `V`
- Jump through headings: `Ctrl+Shift+O`

## Recommended workspace settings

```json
{
  "workbench.editorAssociations": {
    "*.md": "vscode.markdown.preview.editor"
  },
  "markdown.validate.enabled": true,
  "markdown.updateLinksOnFileMove.enabled": "prompt"
}
```

Cursor/VS Code can render Mermaid diagrams in the built-in Markdown preview.

Keep preview security in Strict mode.
