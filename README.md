# Kitty Config (Ghostty‑Inspired)

A clean, GUI‑friendly Kitty setup inspired by Ghostty: minimal chrome, subtle split borders, mouse‑first actions, and macOS‑friendly shortcuts.

## Features
- Clean look with Catppuccin Frappe theme
- Subtle split borders only when you split
- Unfocused panes dimmed for focus
- Hidden scrollbar for a clean canvas
- Minimal tab bar that only appears with 2+ tabs
- Ghostty‑style mouse shortcuts and macOS keybindings
- Smooth window resizing (pixel‑based)
- Large scrollback history

## Screenshots
![Neofetch](image/neofetch.png)
![Split and tab](image/split-and-tab.png)

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
- `cmd+e` tab switcher
- `cmd+shift+e` window/split switcher (focus overlay)
- `cmd+shift+f` search scrollback (opens pager)
- `cmd+.` show last command output (formatted, overlay pager; Nerd Font icons enabled; requires shell integration)

## Mouse Shortcuts
- Right click: paste
- `ctrl` + right click: split right
- `ctrl` + `shift` + right click: split down
- `alt` + right click: close split
- `shift` + right click: reset terminal
- Middle click: paste from primary selection
- Middle click on tab: close tab (kitty default)

## Menubar Actions (macOS)
- Actions → Paste
- Actions → Split Right
- Actions → Split Down
- Actions → Reset Terminal
- Actions → Change Tab Title

## Notes
- Splits use Kitty’s `splits` layout. This is forced automatically by the shortcuts.
- `vsplit` = left/right, `hsplit` = top/bottom
- Window resizing is smooth: `window_resize_step_cells 0`
- Large scrollback: `scrollback_lines 10000`
- Close confirmation enabled: `confirm_os_window_close 1`

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
