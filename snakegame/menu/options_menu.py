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
    Represents the options menu in which you can control the volume level.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : Background
        The options menu background.
    __button_alignment : {1, 2, 3}
        Represents is the alignment of the buttons:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    __volume_bar: VolumeBar
        The volume bar.
    """

    VOLUME_BAR_MARGIN_PERCENTAGE = 0.35
    """The percentage of distance the volume bar is from the background.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: Background=Background(
                AnimatedText(constants.OPTIONS_MENU_TITLE)
            ),
            button_alignment: int=constants.OPTIONS_MENU_BUTTON_ALIGNMENT,
            volume_bar=VolumeBar()
    ):
        """
        Initialize the options' menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        background : Background, optional
            The options menu background (default is Background(AnimatedText(constants.OPTIONS_MENU_TITLE))).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.OPTIONS_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
        volume_bar: VolumeBar, optional
            The volume bar (default is VolumeBar()).
        """
        super().__init__(basic_piece, background, button_alignment)
        self.__volume_bar = self.__align_volume_bar(volume_bar)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.VOLUME_UP:
            self.__volume_bar.volume_up()
            super().back_to_menu()
        elif selected_option == ButtonOption.VOLUME_DOWN:
            self.__volume_bar.volume_down()
            super().back_to_menu()
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

    def __align_volume_bar(self, volume_bar: VolumeBar) -> VolumeBar:
        x, midtop_y = super().get_background().get_midtop()
        center = x, midtop_y + int(super().get_background().get_height()
                                   * OptionsMenu.VOLUME_BAR_MARGIN_PERCENTAGE)
        volume_bar.set_center(center)

        return volume_bar

    def other_updates(self) -> None:
        pass
