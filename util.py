from enum import Enum
from dataclasses import dataclass, field

class MoveType(Enum):
    WIN = 'win'
    BLOCK = 'block'
    STRATEGIC = 'strategic'
    TACTICAL = 'tactical'
    RANDOM = 'random'

class Level(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'

class CellState(Enum):
    EMPTY = 'empty'
    PLAYER = 'player'
    BOT = 'bot'

@dataclass
class ButtonData:
    width : int
    height : int
    text : str
    bg : str
    fg : str
    level : Level

@dataclass
class Player:
    symbol : CellState
    color : str
    falling_start_y : int

@dataclass
class CellData:
    square_points : tuple[int, int, int, int]
    state : CellState = CellState.EMPTY
    color : str | None = None

@dataclass
class GameData:
    cells : dict[tuple[int, int], CellData] = field(default_factory=dict)
    winner_combinations : list[list[tuple[int, int]]] = field(default_factory=list)
    current_level : Level = Level.EASY
    game_over : bool = True
    animation : bool = False