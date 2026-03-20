# from https://github.com/wochap/nix-config/blob/11e30a7a16f5cea8617ed216be87d4757b649af7/modules/shared/programs/gui/kitty/scripts/tab_bar.py
import math
from kitty.fast_data_types import Screen, get_options
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    TabBarData,
    as_rgb,
    draw_tab_with_separator,
)

opts = get_options()
window_icon = ""
layout_icon = ""
SHOW_RIGHT_STATUS = False
RIGHT_STATUS_STYLE = "plain"  # "plain" or "pill"
RIGHT_STATUS_ICONS = False

active_tab_layout_name = ""
active_tab_num_windows = 1


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_title_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    global active_tab_layout_name
    global active_tab_num_windows
    if tab.is_active:
        active_tab_layout_name = tab.layout_name
        active_tab_num_windows = tab.num_windows
    end = draw_tab_with_separator(
        draw_data, screen, tab, before, max_title_length, index, is_last, extra_data
    )
    if SHOW_RIGHT_STATUS:
        _draw_right_status(
            screen,
            is_last,
        )
    return end


def _draw_right_status(screen: Screen, is_last: bool) -> int:
    if not SHOW_RIGHT_STATUS:
        return screen.cursor.x
    if not is_last:
        return screen.cursor.x

    status_bg = as_rgb(opts.color0)
    status_fg = as_rgb(opts.foreground)
    # Ensure caps match the actual bar background (avoid black gaps).
    bar_bg = as_rgb(opts.background)

    if RIGHT_STATUS_STYLE == "pill":
        cells = [
            # left cap
            (status_bg, bar_bg, ""),
            # layout name
            (status_fg, status_bg, " " + layout_icon + " "),
            (status_fg, status_bg, active_tab_layout_name + " "),
            # num windows
            (status_fg, status_bg, " " + window_icon + " "),
            (status_fg, status_bg, str(active_tab_num_windows) + " "),
            # right cap
            (status_bg, bar_bg, ""),
        ]
    else:
        if RIGHT_STATUS_ICONS:
            text = (
                " "
                + layout_icon
                + " "
                + active_tab_layout_name
                + "  "
                + window_icon
                + " "
                + str(active_tab_num_windows)
                + " "
            )
        else:
            text = (
                " layout:"
                + active_tab_layout_name
                + "  win:"
                + str(active_tab_num_windows)
                + " "
            )
        cells = [(status_fg, bar_bg, text)]

    # calculate leading spaces to separate tabs from right status
    right_status_length = 0
    for _, _, cell in cells:
        right_status_length += len(cell)
    leading_spaces = 0
    if opts.tab_bar_align == "center":
        leading_spaces = (
            math.ceil((screen.columns - screen.cursor.x) / 2) - right_status_length
        )
    elif opts.tab_bar_align == "left":
        leading_spaces = screen.columns - screen.cursor.x - right_status_length

    # draw leading spaces
    if leading_spaces > 0:
        screen.cursor.bg = bar_bg
        screen.cursor.fg = 0
        screen.draw(" " * leading_spaces)

    # draw right status
    for fg, bg, cell in cells:
        screen.cursor.fg = fg
        screen.cursor.bg = bg
        screen.draw(cell)
    screen.cursor.fg = 0
    screen.cursor.bg = bar_bg

    # update cursor position
    screen.cursor.x = max(screen.cursor.x, screen.columns - right_status_length)
    return screen.cursor.x
