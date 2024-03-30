from pygame import Surface

from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.confirmation_menu import ConfirmationMenu
from snakegame.menu.menu import Menu
from snakegame.menu.background import Background
from snakegame.menu.score_manager import ScoreManager
from snakegame.menu.sound_manager import SoundManager
from snakegame.text.animated_text import AnimatedText
from snakegame.text.text import Text
from snakegame import constants


class ScoreMenu(Menu):
    """
    Represents a score menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
        The sound manager of the game.
    __score_manager : RecordManager
        The record manager.
    __record : int
        The record.
    __background : Background
        The credits menu background.
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
            score_manager: ScoreManager,
            background: Background = Background(
                AnimatedText(constants.SCORE_MENU_TITLE)
            ),
            button_alignment: int = constants.BOTTOM_ALIGNMENT
    ):
        """
        Initialize the ScoreMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        score_manager : ScoreManager
            The score manager.
        background : Background, optional
            The credits menu background (default is Background(AnimatedText(constants.CREDITS_MENU_TITLE))).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.CREDITS_MENU_BUTTON_ALIGNMENT):
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
        self.__score_manager = score_manager
        self.__record = Text(str(self.__score_manager.get_score()))
        self.__record = self.__align_record(self.__record)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.DELETE_SCORE:
            if self.__score_manager.get_score() > 0:
                option = self.__confirmation_menu.start()
                self.__confirm_option(option)
            else:
                super().reset_selected_option()
        elif selected_option == ButtonOption.BACK:
            super().quit()

    def create_buttons(self) -> list[Button]:
        return [
            Button(ButtonOption.DELETE_SCORE, super().get_sound_manager()),
            Button(ButtonOption.BACK, super().get_sound_manager())
        ]

    def other_events(self) -> None:
        pass

    def drawings_below(self, window: Surface) -> None:
        pass

    def drawings_above(self, window: Surface) -> None:
        self.__record.draw(window)

    def other_updates(self) -> None:
        self.__record.set_content(str(self.__score_manager.get_score()))
        self.__record = self.__align_record(self.__record)

    def reset_other_states(self) -> None:
        pass

    def __confirm_option(self, option: ButtonOption) -> None:
        if option == ButtonOption.YES:
            self.__score_manager.reset_score()

        super().reset_selected_option()

    def __align_record(self, record: Text) -> Text:
        center = super().get_background().get_center()
        record.set_center(center)

        return record
