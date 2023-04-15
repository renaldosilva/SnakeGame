from pygame import Surface

from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.credits_menu import CreditsMenu
from snakegame.menu.menu import Menu
from snakegame.menu.simple_background import SimpleBackground
from snakegame import constants
from snakegame.text.animated_font import AnimatedFont


class MainMenu(Menu):
    """
    Game main menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : SimpleBackground
        The background of the menu.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: SimpleBackground=SimpleBackground(
                AnimatedFont(constants.MAIN_MENU_TITLE),
                image_paths=constants.MAIN_MENU_IMAGES
            )
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
        """
        super().__init__(basic_piece, background)
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
            Button(ButtonOption.QUIT),
        ]
        return buttons

    def align_buttons(self, buttons: list[Button]) -> list[Button]:
        initial_center = super().get_window_height() // 2, super().get_game_pixel_dimension() * 15

        for index, button in enumerate(buttons):
            if index == 0:
                button.set_center(initial_center)
            else:
                previous_button = buttons[index - 1]
                center = self.__calculates_the_center_of_the_next_button(previous_button)
                button.set_center(center)

        return buttons

    def other_drawings(self, window: Surface) -> None:
        pass

    def __calculates_the_center_of_the_next_button(self, previous_button: Button) -> tuple[int, int]:
        x, y = previous_button.get_bottom_shape_middle_bottom()
        return x, y + super().get_game_pixel_dimension() * 2
