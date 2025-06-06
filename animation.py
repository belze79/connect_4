from util import CellState, CellData, Player
from game_data_handler import game_data, is_winner, full_table, bot, reset_cells, get_turn
import f4_session_store as store
from bot_function import move_bot_by_level
from ui_function import change_info_text
from random import randint

def token_falling_down(coordinate : tuple[int, int], player : Player, callback=None):
    x1, y1, x2, y2 = game_data.cells[coordinate].square_points
    cell_height = y2 - y1
    end_y = y1
    y1 = player.falling_start_y
    y2 = y1 + cell_height
    player.falling_start_y += 10
    occupied_cell = [game_data.cells[c] for c in game_data.cells.keys() if not game_data.cells[c].state == CellState.EMPTY]
    redraw_canvas_with_token((x1, y1, x2, y2), occupied_cell, player)
    y1 = player.falling_start_y
    if y1 <= end_y:
        store.root.after(10, token_falling_down, coordinate, player, callback)
    else:
        game_data.animation = False
        game_data.cells[coordinate].color = player.color
        game_data.cells[coordinate].state = player.symbol
        player.falling_start_y = -50
        if is_winner(player):
            change_info_text(f'{player.symbol.value} WIN', player.color)
            game_data.game_over = True
        elif full_table():
            change_info_text('draw', 'orange')
            game_data.game_over = True
        elif callback:
            callback()
        if game_data.game_over:
            reset_cells()
            store.restart_button.is_enabled = True
            store.restart_button.configure(image=store.restart_button.normal)
        else:
            player_turn = get_turn(player)
            change_info_text(f'{player_turn.symbol.value} MOVE', player_turn.color)


def after_animation():
    bot_cell : tuple[int, int] | None = move_bot_by_level(game_data.current_level)
    if bot_cell:
        game_data.animation = True
        after_millisecond = randint(5, 12) * 100
        store.root.after(after_millisecond, token_falling_down, bot_cell, bot, None)

def redraw_canvas_with_token(current_points : tuple[int, int, int, int], occupied_cell : list[CellData], player : Player):
    store.canvas.delete('all')
    store.canvas.create_oval(current_points, fill=player.color)
    store.canvas.create_image(0, 0, image=store.table_enabled, anchor='nw')
    for cell_date in occupied_cell:
        store.canvas.create_oval(cell_date.square_points, fill=cell_date.color)

