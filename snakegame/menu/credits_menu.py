from pygame import Surface

from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.menu.background import Background
from snakegame.menu.sound_manager import SoundManager
from snakegame.text.animated_text import AnimatedText
from snakegame.text.text import Text
from snakegame import constants


class CreditsMenu(Menu):
    """
    Represents a credits menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
        The sound manager of the game.
    __background : Background
        The credits menu background.
    __button_alignment : {1, 2, 3}
        Represents is the alignment of the buttons:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    __credits : Text
        The credits that will be displayed.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            background: Background = Background(
                AnimatedText(constants.CREDITS_MENU_TITLE)
            ),
            button_alignment: int = constants.BOTTOM_ALIGNMENT,
            credits: Text = Text(constants.CREDITS, constants.CREDITS_SIZE)
    ):
        """
        Initialize the CreditsMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        background : Background, optional
            The credits menu background (default is Background(AnimatedText(constants.CREDITS_MENU_TITLE))).
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.CREDITS_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
        credits : Text, optional
            The credits that will be displayed (default is Text(constants.CREDITS, constants.CREDITS_SIZE)).

        Raises
        ------
        ValueError
            If the 'button_alignment' value is not in the range (1-3).
        """
        super().__init__(basic_piece, sound_manager, background, button_alignment)
        self.__credits = self.__align_credits(credits)

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.BACK:
            super().quit()

    def create_buttons(self) -> list[Button]:
        return [Button(ButtonOption.BACK, super().get_sound_manager())]

    def other_events(self) -> None:
        pass

    def drawings_below(self, window: Surface) -> None:
        pass

    def drawings_above(self, window: Surface) -> None:
        self.__credits.draw(window)

    def other_updates(self) -> None:
        pass

    def reset_other_states(self) -> None:
        pass

    def __align_credits(self, credits: Text) -> Text:
        center = super().get_background().get_center()
        credits.set_center(center)

        return credits
