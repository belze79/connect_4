from util import Player, GameData, CellData, CellState
from f4_session_store import table_rows, table_cols, cell_width, cell_height, spacing

game_data = GameData()

max_index_row, max_index_col = table_rows - 1, table_cols - 1
step = 3

player = Player(CellState.PLAYER, 'yellow', -50)
bot = Player(CellState.BOT, 'red', -50)

for row in range(table_rows):
    for col in range(table_cols):

        x1 = spacing + col * (cell_width + spacing)
        y1 = spacing + row * (cell_height + spacing)
        x2 = x1 + cell_width
        y2 = y1 + cell_height

        game_data.cells[(row, col)] = CellData((x1, y1, x2, y2))

        if col + step <= max_index_col:
            # horizontal
            game_data.winner_combinations.append([(row, col + i) for i in range(step + 1)])
        if row + step <= max_index_row:
            # vertical
            game_data.winner_combinations.append([(row + i, col) for i in range(step + 1)])
        if row + step <= max_index_row and col + step <= max_index_col:
            # diagonal down
            game_data.winner_combinations.append([(row + i, col + i) for i in range(step + 1)])
        if row - step >= 0 and col + step <= max_index_col:
            # diagonal up
            game_data.winner_combinations.append([(row - i, col + i) for i in range(step + 1)])

def get_cell_by_click(click_x : int, click_y : int) -> tuple[int, int] | None:
    for coordinate in game_data.cells.keys():
        square_points = game_data.cells[coordinate].square_points
        sp_x1, sp_y1, sp_x2, sp_y2 = square_points
        if sp_x1 < click_x < sp_x2 and sp_y1 < click_y < sp_y2:
            return coordinate
    return None

def is_valid_free_cell(coordinate : tuple[int, int]) -> bool:
    _row, _col = coordinate
    state_clicked = game_data.cells[coordinate].state
    if _row == max_index_row and state_clicked == CellState.EMPTY:
        return True
    return state_clicked == CellState.EMPTY and not game_data.cells[(_row + 1, _col)].state == CellState.EMPTY

def reset_cells():
    for cell_data in [game_data.cells[c] for c in game_data.cells.keys()]:
        cell_data.state = CellState.EMPTY
        cell_data.color = None

def is_winner(_player : Player) -> bool:
    for combination in game_data.winner_combinations:
        if all(game_data.cells[c].state == _player.symbol for c in combination):
            return True
    return False

def full_table() -> bool:
    return all(not game_data.cells[c].state == CellState.EMPTY for c in game_data.cells.keys())

def get_turn(_player : Player) -> Player:
    return player if _player.symbol == bot.symbol else bot












