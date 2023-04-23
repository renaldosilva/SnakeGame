from pygame import Surface

from snakegame.enuns.button_option import ButtonOption
from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.credits_menu import CreditsMenu
from snakegame.menu.difficulty_menu import DifficultyMenu
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
    __background : Background
        The main menu background.
    __button_alignment : {1, 2, 3}
        Represents is the alignment of the buttons:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    __credits_menu : CreditsMenu
        The game credits menu.
    __options_menu : OptionsMenu
        The game options menu.
    __difficulty_menu : DifficultyMenu
        The menu to select the difficulty of the game.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: Background=Background(
                AnimatedFont(constants.MAIN_MENU_TITLE),
                image_paths=constants.MAIN_MENU_IMAGES
            ),
            button_alignment: int=constants.MAIN_MENU_BUTTON_ALIGNMENT
    ):
        """
        Initialize the main menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
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
        """
        super().__init__(basic_piece, background, button_alignment)
        self.__credits_menu = CreditsMenu(basic_piece)
        self.__options_menu = OptionsMenu(basic_piece)
        self.__difficulty_menu = DifficultyMenu(basic_piece)
        self.__pause_menu = PauseMenu(basic_piece)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.START:
            option = self.__difficulty_menu.start()
            self.__manage_start(option)
        elif selected_option == ButtonOption.OPTIONS:
            self.__options_menu.start()
            super().back_to_menu()
        elif selected_option == ButtonOption.CREDITS:
            self.__credits_menu.start()
            super().back_to_menu()
        elif selected_option == ButtonOption.QUIT:
            super().close_all()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.START),
            Button(ButtonOption.OPTIONS),
            Button(ButtonOption.CREDITS),
            Button(ButtonOption.QUIT)
        ]
        return buttons

    def other_drawings(self, window: Surface) -> None:
        pass

    def other_updates(self) -> None:
        pass

    def __manage_start(self, option: ButtonOption) -> None:
        if option == ButtonOption.BACK:
            super().back_to_menu()
        else:
            super().get_basic_piece().set_game_state(GameState.GAME)
            super().quit()

    def start_pause_menu(self) -> None:
        """Start the pause menu."""
        self.__pause_menu.start()
