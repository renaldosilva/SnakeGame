from pygame import Surface

from snakegame.enuns.button_option import ButtonOption
from snakegame.menu.record_manager import RecordManager
from snakegame.menu.record_menu import RecordMenu
from snakegame.menu.sound_manager import SoundManager
from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.credits_menu import CreditsMenu
from snakegame.menu.menu import Menu
from snakegame.menu.background import Background
from snakegame import constants
from snakegame.menu.options_menu import OptionsMenu
from snakegame.menu.pause_menu import PauseMenu
from snakegame.text.animated_font import AnimatedFont


class MainMenu(Menu):
    """
    The game's main menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
        The sound manager of the game.
    __background : Background
        The main menu background.
    __button_alignment : {1, 2, 3}
        Represents is the alignment of the buttons:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    __options_menu : OptionsMenu
        The game options menu.
    __record_menu : RecordMenu
        The record menu.
    __credits_menu : CreditsMenu
        The game credits menu.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            record_manager: RecordManager,
            background: Background=Background(
                AnimatedFont(constants.MAIN_MENU_TITLE),
                image_paths=constants.MAIN_MENU_IMAGES
            ),
            button_alignment: int=constants.BUTTON_ALIGNMENT_CENTER
    ):
        """
        Initialize the MainMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        record_manager : RecordManager
            The record manager.
        background : Background, optional
            The main menu background (default is Background(
                AnimatedFont(constants.MAIN_MENU_TITLE),
                image_paths=constants.MAIN_MENU_IMAGES
            )).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.MAIN_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.

        Raises
        ------
        ValueError
            If the 'button_alignment' value is not in the range (1-3).
        """
        super().__init__(basic_piece, sound_manager, background, button_alignment)
        self.__options_menu = OptionsMenu(basic_piece, sound_manager)
        self.__record_menu = RecordMenu(basic_piece, sound_manager, record_manager)
        self.__credits_menu = CreditsMenu(basic_piece, sound_manager)
        self.__pause_menu = PauseMenu(basic_piece, sound_manager)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.START:
            super().get_sound_manager().stop_sound("main_menu")
            super().get_basic_piece().set_game_state(GameState.GAME)
            super().quit()
        elif selected_option == ButtonOption.OPTIONS:
            self.__options_menu.start()
            super().reset_selected_option()
        elif selected_option == ButtonOption.RECORD:
            self.__record_menu.start()
            super().reset_selected_option()
        elif selected_option == ButtonOption.CREDITS:
            self.__credits_menu.start()
            super().reset_selected_option()
        elif selected_option == ButtonOption.QUIT:
            super().close_all()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.START, super().get_sound_manager()),
            Button(ButtonOption.OPTIONS, super().get_sound_manager()),
            Button(ButtonOption.RECORD, super().get_sound_manager()),
            Button(ButtonOption.CREDITS, super().get_sound_manager()),
            Button(ButtonOption.QUIT, super().get_sound_manager())
        ]
        return buttons

    def other_events(self) -> None:
        super().get_sound_manager().play_sound("main_menu", -1)

    def other_drawings(self, window: Surface) -> None:
        pass

    def other_updates(self) -> None:
        pass

    def start_pause_menu(self) -> None:
        """Start the pause menu."""
        self.__pause_menu.start()
