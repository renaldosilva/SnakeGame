from enum import Enum


class GameState(Enum):
    """
    An enumeration that represents the state of the game.

    Attributes
    ----------
    MENU : int
        State in which the menu is running.
    PAUSE : int
        State where the pause menu is running.
    GAME : int
        State in which the game is running.
    """

    MENU = 0
    PAUSE = 1
    GAME = 2

    