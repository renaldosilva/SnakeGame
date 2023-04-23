from pygame import Surface

from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.background import Background
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.text.animated_text import AnimatedText


BACKGROUND = Background(AnimatedText(constants.PAUSE_MENU_TITLE), dimensions=constants.PAUSE_MENU_DIMENSIONS)
BACKGROUND.set_center(constants.PAUSE_MENU_CENTER)


class PauseMenu(Menu):
    """
    Represents a pause menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : Background
        The pause menu background.
    __button_alignment : {1, 2, 3}
        Represents is the alignment of the buttons:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: Background=BACKGROUND,
            button_alignment: int = constants.PAUSE_MENU_BUTTON_ALIGNMENT
    ):
        """
        Initialize the credits' menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        background : Background, optional
            The pause menu background (default is BACKGROUND).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.PAUSE_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
        """
        super().__init__(basic_piece, background, button_alignment)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.CONTINUE:
            super().get_basic_piece().set_game_state(GameState.GAME)
            super().quit()
        elif selected_option == ButtonOption.BACK_TO_MAIN_MENU:
            super().get_basic_piece().set_game_state(GameState.MENU)
            super().quit()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.CONTINUE),
            Button(ButtonOption.BACK_TO_MAIN_MENU)
        ]
        return buttons

    def other_drawings(self, window: Surface) -> None:
        pass

    def other_updates(self) -> None:
        pass
