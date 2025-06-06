from random import shuffle, randint
from game_data_handler import game_data, player, bot, is_valid_free_cell
from util import MoveType, Level, CellState

def get_level_move_type(level : Level) -> list[MoveType]:
    match level:
        case Level.EASY: return [MoveType.WIN, MoveType.RANDOM]
        case Level.MEDIUM: return [MoveType.WIN, MoveType.BLOCK, MoveType.RANDOM]
        case Level.HARD: return [MoveType.WIN, MoveType.BLOCK, MoveType.STRATEGIC, MoveType.TACTICAL, MoveType.RANDOM]
        case _: return []

def get_cell_to_place(move_type : MoveType) -> tuple[int, int] | None:
    cells : list[tuple[int, int]] = []
    for combination in game_data.winner_combinations:
        bot_cell = [c for c in combination if game_data.cells[c].state == bot.symbol]
        free_cell = [c for c in combination if game_data.cells[c].state == CellState.EMPTY]
        if move_type == MoveType.WIN and len(bot_cell) == 3 and len(free_cell) == 1:
            if is_valid_free_cell(free_cell[0]): cells.append(free_cell[0])
        elif move_type == MoveType.BLOCK and len([c for c in combination if game_data.cells[c].state == player.symbol]) == 3 and len(free_cell) == 1:
            if is_valid_free_cell(free_cell[0]): cells.append(free_cell[0])
        elif move_type == MoveType.STRATEGIC and len(bot_cell) == 2 and len(free_cell) == 2:
            cells += [c for c in free_cell if is_valid_free_cell(c)]
        elif move_type == MoveType.TACTICAL and len(bot_cell) == 1 and len(free_cell) == 3:
            cells += [c for c in free_cell if is_valid_free_cell(c)]
        elif move_type == MoveType.RANDOM:
            cells += [c for c in game_data.cells.keys() if is_valid_free_cell(c)]

    if not cells: return None
    if len(cells) == 1: return cells[0]
    shuffle(cells)
    return cells[randint(0, len(cells) - 1)]

def move_bot_by_level(level : Level) -> tuple[int, int] | None:
    move_type_list = get_level_move_type(level)
    for move_type in move_type_list:
        cell = get_cell_to_place(move_type)
        if cell:
            game_data.cells[cell].state = player.symbol
            return cell
    return None


