from enum import Enum


class GameState(Enum):
    """
    An enumeration that represents the state of the game.

    Attributes
    ----------
    MENU : int
        State in which the menu is running.
    PAUSE : int
        State in which the pause menu is running.
    TIMER : int
        State in which a timer is activated
    LOADING : int
        State in which loading screen is running.
    GAME : int
        State in which the game is running.
    """

    MENU = 0
    PAUSE = 1
    TIMER = 2
    LOADING = 3
    GAME = 4

    