from pygame import Surface

from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.background import Background
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.menu.sound_manager import SoundManager
from snakegame.text.animated_text import AnimatedText


class ConfirmationMenu(Menu):
    """
    Represents a confirmation menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
        The sound manager of the game.
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
            sound_manager: SoundManager,
            background: Background = Background(
                AnimatedText(constants.CONFIRMATION_MENU_TITLE),
                dimensions=constants.CONFIRMATION_MENU_DIMENSIONS,
                color=constants.GREEN_1
            ),
            button_alignment: int = constants.BOTTOM_ALIGNMENT
    ):
        """
        Initialize the ConfirmationMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        background : Background, optional
            The pause menu background (default is BACKGROUND).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.PAUSE_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.

        Raises
        ------
        ValueError
            If the 'button_alignment' value is not in the range (1-3).
        """
        background.set_center(basic_piece.get_window_center())
        super().__init__(basic_piece, sound_manager, background, button_alignment)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.YES:
            super().quit()
        elif selected_option == ButtonOption.NO:
            super().quit()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.YES, super().get_sound_manager()),
            Button(ButtonOption.NO, super().get_sound_manager())
        ]
        return buttons

    def other_events(self) -> None:
        pass

    def other_drawings(self, window: Surface) -> None:
        pass

    def other_updates(self) -> None:
        pass
