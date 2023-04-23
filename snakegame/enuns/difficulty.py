from enum import Enum


class Difficulty(Enum):
    """
    An enumeration representing the difficulties of the game.

    Attributes
    ----------
    NONE : int
        Neutral value that does not correspond to any difficulty.
    EASY : int
        Easy difficulty.
    MEDIUM : int
        Medium difficulty.
    HARD : int
        Hard difficulty.
    """

    NONE = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3
