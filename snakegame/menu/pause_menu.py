from pygame import Surface

from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.background import Background
from snakegame.menu.button import Button
from snakegame.menu.confirmation_menu import ConfirmationMenu
from snakegame.menu.menu import Menu
from snakegame.menu.sound_manager import SoundManager
from snakegame.text.animated_text import AnimatedText


class PauseMenu(Menu):
    """
    Represents a pause menu.

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
    __confirmation_menu : ConfirmationMenu
        An auxiliary menu.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            background: Background=Background(AnimatedText(constants.PAUSE_MENU_TITLE)),
            button_alignment: int = constants.BOTTOM_ALIGNMENT
    ):
        """
        Initialize the PauseMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        background : Background, optional
            The pause menu background (default is Background(AnimatedText(constants.PAUSE_MENU_TITLE))).
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
        super().__init__(basic_piece, sound_manager, background, button_alignment)
        self.__confirmation_menu = ConfirmationMenu(basic_piece, sound_manager)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.CONTINUE:
            super().get_sound_manager().stop_sound("pause_menu")
            super().get_basic_piece().set_game_state(GameState.TIMER)
            super().quit()
        elif selected_option == ButtonOption.BACK_TO_MAIN_MENU:
            option = self.__confirmation_menu.start()
            self.__confirm_option(option)

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.CONTINUE, super().get_sound_manager()),
            Button(ButtonOption.BACK_TO_MAIN_MENU, super().get_sound_manager())
        ]
        return buttons

    def other_events(self) -> None:
        super().get_sound_manager().play_sound("pause_menu", -1)

    def drawings_below(self, window: Surface) -> None:
        pass

    def drawings_above(self, window: Surface) -> None:
        pass

    def other_updates(self) -> None:
        pass

    def reset_other_states(self) -> None:
        pass

    def __confirm_option(self, option: ButtonOption) -> None:
        if option == ButtonOption.YES:
            super().get_sound_manager().stop_sound("pause_menu")
            super().get_basic_piece().set_game_state(GameState.LOADING)
            super().quit()
        else:
            super().reset_selected_option()
