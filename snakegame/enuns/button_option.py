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
    EASY : int
        Easy difficulty button.
    MEDIUM : int
        Medium difficulty button.
    HARD : int
        Hard difficulty button.
    CONTINUE : int
        A button to continue the game.
    BACK_TO_MAIN_MENU : int
        A button to go back to the main menu.
    """

    NONE = 0
    START = 3
    OPTIONS = 4
    CREDITS = 5
    QUIT = 6
    BACK = 7
    VOLUME_UP = 8
    VOLUME_DOWN = 9
    EASY = 10
    MEDIUM = 11
    HARD = 12
    CONTINUE = 13
    BACK_TO_MAIN_MENU = 14
