from pygame import Surface


from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.menu.background import Background
from snakegame.menu.sound_manager import SoundManager
from snakegame.menu.volume_bar import VolumeBar
from snakegame.text.animated_text import AnimatedText


class OptionsMenu(Menu):
    """
    Represents the options menu in which you can control the volume level.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
            The sound manager of the game.
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
            sound_manager: SoundManager,
            background: Background=Background(
                AnimatedText(constants.OPTIONS_MENU_TITLE)
            ),
            button_alignment: int=constants.BOTTOM_ALIGNMENT,
            volume_bar=VolumeBar()
    ):
        """
        Initialize the OptionsMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        background : Background, optional
            The options menu background (default is Background(AnimatedText(constants.OPTIONS_MENU_TITLE))).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.OPTIONS_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
        volume_bar: VolumeBar, optional
            The volume bar (default is VolumeBar()).

        Raises
        ------
        ValueError
            If the 'button_alignment' value is not in the range (1-3).
        """
        super().__init__(basic_piece, sound_manager, background, button_alignment)
        self.__volume_bar = self.__align_volume_bar(volume_bar)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.VOLUME_UP:
            super().get_sound_manager().volume_up()
            self.__volume_bar.set_volume_level(super().get_sound_manager().get_current_volume())
            super().reset_selected_option()
        elif selected_option == ButtonOption.VOLUME_DOWN:
            super().get_sound_manager().volume_down()
            self.__volume_bar.set_volume_level(super().get_sound_manager().get_current_volume())
            super().reset_selected_option()
        elif selected_option == ButtonOption.BACK:
            super().quit()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.VOLUME_UP, super().get_sound_manager()),
            Button(ButtonOption.VOLUME_DOWN, super().get_sound_manager()),
            Button(ButtonOption.BACK, super().get_sound_manager())
        ]
        return buttons

    def other_events(self) -> None:
        pass

    def drawings_below(self, window: Surface) -> None:
        pass

    def drawings_above(self, window: Surface) -> None:
        self.__volume_bar.draw(window)

    def __align_volume_bar(self, volume_bar: VolumeBar) -> VolumeBar:
        x, midtop_y = super().get_background().get_midtop()
        center = x, midtop_y + int(super().get_background().get_height()
                                   * OptionsMenu.VOLUME_BAR_MARGIN_PERCENTAGE)
        volume_bar.set_center(center)

        return volume_bar

    def other_updates(self) -> None:
        pass

    def reset_other_states(self) -> None:
        pass
