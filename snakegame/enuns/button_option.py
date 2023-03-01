from enum import Enum


class ButtonOption(Enum):
    """
    An enumeration that represents the different button options available in a game.

    Each button option is associated with a specific integer value.
    """

    NONE = 0
    """
    A button option that does not correspond to any particular action.
    """

    START = 3
    """
    A button option that starts a new game.
    """

    OPTIONS = 4
    """
    A button option that opens the options menu.
    """

    CREDITS = 5
    """
    A button option that displays the game's credits.
    """

    QUIT = 6
    """
    A button option that quits the game.
    """

    BACK = 7
    """
    A button option that goes back to the previous menu.
    """
