from pygame import Surface

from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.menu.background import Background
from snakegame.menu.score_manager import ScoreManager
from snakegame.menu.score_menu import ScoreMenu
from snakegame.menu.sound_manager import SoundManager
from snakegame.menu.sound_menu import SoundMenu
from snakegame.text.animated_text import AnimatedText


class OptionsMenu(Menu):
    """
    Represents the options' menu.

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
    __sound_menu : SoundMenu
        The game sound menu.
    __score_menu : ScoreMenu
        The scoring menu.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            score_manager: ScoreManager,
            background: Background = Background(
                AnimatedText(constants.OPTIONS_MENU_TITLE)
            ),
            button_alignment: int = constants.CENTER_ALIGNMENT
    ):
        """
        Initialize the OptionsMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        score_manager : ScoreManager
            The score manager.
        background : Background, optional
            The options menu background (default is Background(AnimatedText(constants.OPTIONS_MENU_TITLE))).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.OPTIONS_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.

        Raises
        ------
        ValueError
            If the 'button_alignment' value is not in the range (1-3).
        """
        super().__init__(basic_piece, sound_manager, background, button_alignment)
        self.__sound_menu = SoundMenu(basic_piece, sound_manager)
        self.__score_menu = ScoreMenu(basic_piece, sound_manager, score_manager)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.SOUND:
            self.__sound_menu.start()
            super().reset_selected_option()
        elif selected_option == ButtonOption.SCORE:
            self.__score_menu.start()
            super().reset_selected_option()
        elif selected_option == ButtonOption.BACK:
            super().quit()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.SOUND, super().get_sound_manager()),
            Button(ButtonOption.SCORE, super().get_sound_manager()),
            Button(ButtonOption.BACK, super().get_sound_manager())
        ]
        return buttons

    def other_events(self) -> None:
        pass

    def drawings_below(self, window: Surface) -> None:
        pass

    def drawings_above(self, window: Surface) -> None:
        pass

    def other_updates(self) -> None:
        pass

    def reset_other_states(self) -> None:
        pass
