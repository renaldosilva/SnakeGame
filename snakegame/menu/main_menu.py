from pygame import Surface

from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.credits_menu import CreditsMenu
from snakegame.menu.menu import Menu
from snakegame.menu.background import Background
from snakegame import constants
from snakegame.text.animated_font import AnimatedFont


class MainMenu(Menu):
    """
    Game main menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : Background
        The background of the menu.
    __button_alignment : {1, 2, 3}
            Represents is the alignment of the buttons:
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
    __credits_menu: CreditsMenu
        The credits' menu.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: Background=Background(
                AnimatedFont(constants.MAIN_MENU_TITLE),
                image_paths=constants.MAIN_MENU_IMAGES
            ),
            button_alignment: int=2
    ):
        """
        Initialize the main menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        background : SimpleBackground, optional
        The background of the menu (default is SimpleBackground(
                AnimatedFont(constants.MAIN_MENU_TITLE),
                image_paths=constants.MAIN_MENU_IMAGES
            )).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is 2):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
        """
        super().__init__(basic_piece, background, button_alignment)
        self.__credits_menu = CreditsMenu(basic_piece)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.START:
            super().quit()
        elif selected_option == ButtonOption.OPTIONS:
            super().back_to_main_menu()
        elif selected_option == ButtonOption.CREDITS:
            self.__credits_menu.start()
            super().back_to_main_menu()
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
