from pygame import Surface


from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.menu.background import Background
from snakegame.menu.volume_bar import VolumeBar
from snakegame.text.animated_text import AnimatedText


class OptionsMenu(Menu):
    """
    Options menu. In this menu you can control the volume.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : Background
        The background of the menu.
    __volume_bar: VolumeBar
        The menu volume bar.
    """

    VOLUME_BAR_MARGIN_PERCENTAGE = 0.35
    """The percentage of distance the volume bar is from the background.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: Background=Background(AnimatedText(constants.OPTIONS_MENU_TITLE)),
            button_alignment: int=3,
            volume_bar=VolumeBar()
    ):
        """
        Initialize the options' menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        background : SimpleBackground, optional
            The background of the menu (default is SimpleBackground(AnimatedText(constants.OPTIONS_MENU_TITLE))).
        volume_bar: VolumeBar, optional
            The menu volume bar (default is VolumeBar()).
        """
        super().__init__(basic_piece, background, button_alignment)
        self.__volume_bar = volume_bar
        self.__align_volume_bar()

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.VOLUME_UP:
            self.__volume_bar.volume_up()
            super().back_to_main_menu()
        elif selected_option == ButtonOption.VOLUME_DOWN:
            self.__volume_bar.volume_down()
            super().back_to_main_menu()
        elif selected_option == ButtonOption.BACK:
            super().quit()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.VOLUME_UP),
            Button(ButtonOption.VOLUME_DOWN),
            Button(ButtonOption.BACK)
        ]
        return buttons

    def other_drawings(self, window: Surface) -> None:
        self.__volume_bar.draw(window)

    def __align_volume_bar(self) -> None:
        x, midtop_y = super().get_background_midtop()
        center = x, midtop_y + int(super().get_background_height() * OptionsMenu.VOLUME_BAR_MARGIN_PERCENTAGE)

        self.__volume_bar.set_center(center)
