from tkinter import Label
from image_handler import get_text_image, create_table_image
import f4_session_store as store


def switch_play_restart_button(to_hidden : Label, to_show : Label):
    to_hidden.grid_remove()
    to_show.grid()

def change_state_button(disabled : bool = True):
    for btn in store.level_buttons:
        btn.is_enabled = not btn.is_enabled
        btn.configure(image=btn.disabled if disabled else btn.normal)

def change_info_text(text : str, color : str):
    store.label_info.text = text
    store.label_info.text_image = get_text_image(store.label_info.text, store.label_info.font_size, color)
    store.label_info.configure(image=store.label_info.text_image)

def reset_canvas_and_info():
    _, store.table_disabled = create_table_image('black')
    store.canvas.delete('all')
    store.canvas.create_image(0, 0, image=store.table_disabled, anchor='nw')
    change_state_button(disabled=False)
    change_info_text('select level', store.fg_main)

def set_table_enabled():
    store.canvas.delete('all')
    store.canvas.create_image(0, 0, image=store.table_enabled, anchor='nw')

def redraw_canvas(color : str, disabled_image : bool = True):
    store.table_enabled, store.table_disabled = create_table_image(color)
    store.canvas.delete('all')
    store.canvas.create_image(0, 0, image=store.table_disabled if disabled_image else store.table_enabled, anchor='nw')

# def reset_play_restart_button(btn : Label, disabled : bool = True):
