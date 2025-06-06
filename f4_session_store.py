from tkinter import Tk, Canvas, Label, PhotoImage, Frame

root : Tk | None = None
root_width, root_height = 530, 684
bg_main = '#222'
fg_main = '#ccc'

table_rows, table_cols = 6, 7
cell_width, cell_height = 50, 50
spacing = 10
canvas_width = cell_width * table_cols + spacing * (table_cols + 1)
canvas_height = cell_height * table_rows + spacing * (table_rows + 1)

title_image : PhotoImage | None = None
label_title : Label | None = None

level_buttons_grid : Frame | None = None
level_buttons : list[Label] = []

canvas : Canvas | None = None
table_enabled : PhotoImage | None = None
table_disabled : PhotoImage | None = None

label_info : Label | None = None

play_button : Label | None = None

restart_button : Label | None = None





