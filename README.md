# Kitty Config (Ghostty‑Inspired)

A clean, GUI‑friendly Kitty setup inspired by Ghostty: minimal chrome, subtle split borders, mouse‑first actions, and macOS‑friendly shortcuts.

## Features
- Clean look with Catppuccin Frappe theme
- Subtle split borders only when you split
- Unfocused panes dimmed for focus
- Hidden scrollbar for a clean canvas
- Minimal tab bar that only appears with 2+ tabs
- Ghostty‑style mouse shortcuts and macOS keybindings

## Requirements
- Kitty terminal
- Font: `JetBrainsMono Nerd Font Mono`

## Install
1. Clone or copy this repo to your Kitty config directory:
   - macOS/Linux default: `~/.config/kitty`
2. Start Kitty or reload the config.

## Reload Config
- Restart Kitty, or
- Use `ctrl+shift+f5`

## Keybindings
- `cmd+d` split right
- `cmd+shift+d` split down
- `cmd+w` close split
- `cmd+shift+r` reset terminal (also sends Enter)
- `cmd+shift+l` clear screen
- `cmd+shift+i` change tab title
- `cmd+t` new tab
- `cmd+shift+left/right` previous/next tab

## Mouse Shortcuts
- Right click: paste
- `ctrl` + right click: split right
- `ctrl` + `shift` + right click: split down
- `alt` + right click: close split
- `shift` + right click: reset terminal
- Middle click: paste from primary selection

## File Layout
- `kitty.conf` main config
- `current-theme.conf` Catppuccin Frappe theme (included)
- `Catppuccin-Frappe.conf` theme source

## Customize
Common tweaks in `kitty.conf`:
- Font size: `font_size`
- Unfocused dim: `inactive_text_alpha`
- Split border thickness: `window_border_width`
- Tab bar style: `tab_bar_style`, `tab_bar_min_tabs`
- Padding/margins: `window_padding_width`, `window_margin_width`

---

If you want a different look (more minimal or more decorative), open an issue or tweak the values above.
