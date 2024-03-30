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
    SCORE: int
        A button to access the game score.
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
    CONTINUE : int
        A button to continue the game.
    BACK_TO_MAIN_MENU : int
        A button to go back to the main menu.
    YES : int
        A confirmation button.
    NO : int
        A reject button.
    DELETE_SCORE : int
        A button to delete the score.
    SOUND : int
        A button option that opens the sound menu.
    """

    NONE = 0
    START = 3
    OPTIONS = 4
    SCORE = 5
    CREDITS = 6
    QUIT = 7
    BACK = 8
    VOLUME_UP = 9
    VOLUME_DOWN = 10
    CONTINUE = 11
    BACK_TO_MAIN_MENU = 12
    YES = 13
    NO = 14
    DELETE_SCORE = 15
    SOUND = 16
