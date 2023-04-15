from pygame import Surface

from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.menu.simple_background import SimpleBackground
from snakegame.text.animated_text import AnimatedText
from snakegame.text.text import Text
from snakegame import constants


class CreditsMenu(Menu):
    """
    Credits menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : SimpleBackground
        The background of the menu.
    __credits : Text
        The credits that will be displayed.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: SimpleBackground=SimpleBackground(AnimatedText(constants.CREDITS_MENU_TITLE)),
            credits: Text=Text(constants.CREDITS, constants.CREDITS_SIZE)
    ):
        """
        Initialize the credits menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        background : SimpleBackground, optional
            The background of the menu (default is SimpleBackground(AnimatedText(constants.CREDITS_MENU_TITLE))).
        credits: Text, optional
            The credits that will be displayed (default is Text(constants.CREDITS, constants.CREDITS_SIZE)).
        """
        super().__init__(basic_piece, background)
        self.__credits = self.__align_credits(credits)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.BACK:
            super().quit()

    def create_buttons(self) -> list[Button]:
        return [Button(ButtonOption.BACK)]

    def align_buttons(self, buttons: list[Button]) -> list[Button]:
        center = super().get_window_width() // 2, \
            super().get_window_height() - super().get_game_pixel_dimension()*5

        for button in buttons:
            button.set_center(center)

        return buttons

    def other_drawings(self, window: Surface) -> None:
        self.__credits.draw(window)

    def __align_credits(self, credits: Text) -> Text:
        center = super().get_window_width() // 2, super().get_window_height() // 2
        credits.set_center(center)

        return credits
