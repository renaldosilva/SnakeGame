from enum import Enum


class ButtonOption(Enum):
    """
    An enumeration that represents the different button options available in a game.

    Attributes
    ----------
    NONE : int
        A button option that does not correspond to any particular action.
    START : int
        A button option that starts a new game.
    OPTIONS : int
        A button option that opens the options' menu.
    CREDITS : int
        A button option that displays the game's credits.
    QUIT : int
        A button option that quits the game.
    BACK : int
        A button option that goes back to the previous menu.
    VOLUME_UP : int
        Volume up button.
    VOLUME_DOWN : int
        Volume down button.
    """

    NONE = 0
    START = 3
    OPTIONS = 4
    CREDITS = 5
    QUIT = 6
    BACK = 7
    VOLUME_UP = 8
    VOLUME_DOWN = 9
