from tkinter import Event, Label
from ui_function import change_info_text, change_state_button, switch_play_restart_button, set_table_enabled, redraw_canvas, reset_canvas_and_info
from game_data_handler import game_data, player, bot, get_cell_by_click, is_valid_free_cell
from animation import token_falling_down, after_animation
import f4_session_store as store


def on_lvl_btn_click(e : Event):
    btn : Label = e.widget
    if btn.is_enabled:
        game_data.current_level = btn.level
        redraw_canvas(btn.bg_color)
        change_info_text(f'level {game_data.current_level.value}', btn.bg_color)
        if not store.play_button.is_enabled:
            store.play_button.is_enabled = True
            store.play_button.configure(image=store.play_button.normal)

def on_canvas_click(e : Event):
    if game_data.animation or game_data.game_over: return
    click_x = e.x
    click_y = e.y
    clicked_cell = get_cell_by_click(click_x, click_y)
    if clicked_cell and is_valid_free_cell(clicked_cell):
        game_data.animation = True
        token_falling_down(clicked_cell, player, callback=lambda : after_animation())


def on_play_restart_button_click(e : Event):
    btn : Label = e.widget
    if btn == store.play_button and btn.is_enabled:
        set_table_enabled()
        change_state_button()
        change_info_text(f'{player.symbol.value} move', player.color)
        game_data.game_over = False
        btn.is_enabled = False
        btn.configure(image=btn.disabled)
        switch_play_restart_button(btn, store.restart_button)
    elif btn == store.restart_button and btn.is_enabled:
        btn.is_enabled = False
        btn.configure(image=btn.disabled)
        switch_play_restart_button(btn, store.play_button)
        reset_canvas_and_info()

def on_enter(e : Event):
    btn : Label = e.widget
    if btn.is_enabled:
        btn.configure(image=btn.hover, cursor='hand2')

def on_leave(e : Event):
    btn : Label = e.widget
    if btn.is_enabled:
        btn.configure(image=btn.normal, cursor='arrow')



