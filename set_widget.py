from tkinter import Canvas, Label, Event, Frame
from image_handler import get_text_image, get_state_image_button, create_table_image
from event_function import on_canvas_click, on_lvl_btn_click, on_play_restart_button_click, on_enter, on_leave
from util import ButtonData, Level
import f4_session_store as store

level_buttons_set : list[ButtonData] = [
    ButtonData(100, 30, Level.EASY.value.upper(), 'green', 'lime', Level.EASY),
    ButtonData(100, 30, Level.MEDIUM.value.upper(), 'orange', 'yellow', Level.MEDIUM),
    ButtonData(100, 30, Level.HARD.value.upper(), 'purple', 'violet', Level.HARD)
]


def set_label_title(text : str, color : str):
    text_image = get_text_image(text, 30, store.fg_main)
    store.title_image = text_image
    store.label_title = Label(store.root, image=text_image, bg=store.bg_main)

def set_level_btn_grid(spacing : int):
    store.level_buttons_grid = Frame(store.root, bg=store.bg_main)
    store.level_buttons_grid.grid_columnconfigure((1, 3), minsize=spacing)
    for i, btn in enumerate(level_buttons_set):
        normal, hover, disabled = get_state_image_button(btn.text, btn.width, btn.height,btn.bg, btn.fg)
        button = Label(store.level_buttons_grid, image=normal, bg=store.bg_main)
        button.grid(row=0, column=i * 2)
        button.normal = normal
        button.hover = hover
        button.disabled = disabled
        button.is_enabled = True
        button.bg_color = btn.bg
        button.level = btn.level
        button.bind('<Button-1>', lambda event : on_lvl_btn_click(event))
        button.bind('<Enter>', lambda event : on_enter(event))
        button.bind('<Leave>', lambda event : on_leave(event))
        store.level_buttons.append(button)


def set_canvas():
    store.canvas = Canvas(store.root, width=store.canvas_width, height=store.canvas_height, bg=store.bg_main, borderwidth=0, highlightthickness=0)
    _, store.table_disabled = create_table_image('black')
    store.canvas.create_image(0, 0, image=store.table_disabled, anchor='nw')
    store.canvas.bind('<Button-1>', lambda event : on_canvas_click(event))

def set_label_info():
    store.label_info = Label(store.root)
    store.label_info.text = 'select level'
    store.label_info.font_size = 20
    store.label_info.text_image = get_text_image(store.label_info.text, store.label_info.font_size, store.fg_main)
    store.label_info.configure(image=store.label_info.text_image, bg=store.bg_main)

def set_play_button():
    normal, hover, disabled = get_state_image_button('PLAY', 100, 30, 'lime', 'green')
    store.play_button = Label(store.root, image=disabled, bg=store.bg_main)
    store.play_button.normal = normal
    store.play_button.hover = hover
    store.play_button.disabled = disabled
    store.play_button.is_enabled = False
    store.play_button.bind('<Button-1>', lambda event : on_play_restart_button_click(event))
    store.play_button.bind('<Enter>', lambda event: on_enter(event))
    store.play_button.bind('<Leave>', lambda event: on_leave(event))

def set_restart_button():
    normal, hover, disabled = get_state_image_button('restart', 100, 30, 'lime', 'green')
    store.restart_button = Label(store.root, image=disabled, bg=store.bg_main)
    store.restart_button.normal = normal
    store.restart_button.hover = hover
    store.restart_button.disabled = disabled
    store.restart_button.is_enabled = False
    store.restart_button.bind('<Button-1>', lambda event : on_play_restart_button_click(event))
    store.restart_button.bind('<Enter>', lambda event: on_enter(event))
    store.restart_button.bind('<Leave>', lambda event: on_leave(event))





















