from tkinter import Tk
from set_widget import set_label_title, set_level_btn_grid, set_canvas, set_label_info, set_play_button, set_restart_button
import f4_session_store as store


store.root = Tk()
store.root.title('FORZA 4')
screen_width, screen_height = store.root.winfo_screenwidth(), store.root.winfo_screenheight()
store.root.geometry(f'{store.root_width}x{store.root_height}+{(screen_width - store.root_width) // 2}+{(screen_height - store.root_height - screen_height) // 2}')
store.root.configure(bg=store.bg_main)

store.root.grid_columnconfigure((0, 2), weight=1)
store.root.grid_columnconfigure(1, weight=2)
store.root.grid_rowconfigure((1, 3, 5, 7), weight=1)
store.root.grid_rowconfigure((0, 2, 4, 6, 8), weight=2)

set_label_title('CONNECT 4', 'orange')
set_canvas()
set_level_btn_grid(50)
set_label_info()
set_restart_button()
set_play_button()

store.label_title.grid(row=0, column=1, pady=(10, 0))
store.level_buttons_grid.grid(row=2, column=1)
store.canvas.grid(row=4, column=1)
store.label_info.grid(row=6, column=1)
store.restart_button.grid(row=8, column=1, pady=(0, 10))
store.restart_button.grid_remove()
store.play_button.grid(row=8, column=1, pady=(0, 10))

store.root.mainloop()