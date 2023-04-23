from pygame import Surface

from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.enuns.difficulty import Difficulty
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.background import Background
from snakegame.menu.button import Button
from snakegame.menu.menu import Menu
from snakegame.text.animated_text import AnimatedText



BACKGROUNDS = (
    Background(AnimatedText(constants.EASY_MENU_TITLE)),
    Background(AnimatedText(constants.MEDIUM_MENU_TITLE)),
    Background(AnimatedText(constants.HARD_MENU_TITLE)),
    Background(AnimatedText(constants.NEUTRAL_MENU_TITLE))
)


class DifficultyMenu(Menu):
    """
    Difficulty choice menu. Each difficulty level has a specific background
    that changes depending on the menu selector.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __backgrounds : tuple[Background, Background, Background, Background]
        The backgrounds of the difficulty selection menu.
        They are arranged in the following order:
            - Easy background;
            - Medium background;
            - Hard background;
            - Neutral background.
    __button_alignment : {1, 2, 3}
        Represents is the alignment of the buttons:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.

    Notes
    -----
    Neutral background is used when no difficulty is being selected.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            backgrounds: tuple[Background, Background, Background, Background]=BACKGROUNDS,
            button_alignment: int=constants.DIFFICULTY_MENU_BUTTON_ALIGNMENT
    ):
        """
        Initialize the DifficultyMenu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        backgrounds : tuple[Background, Background, Background, Background], optional
            The backgrounds of the difficulty selection menu.
            They are arranged in the following order (default is BACKGROUNDS):
                - Easy background;
                - Medium background;
                - Hard background;
                - Neutral background.
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is constants.DIFFICULTY_MENU_BUTTON_ALIGNMENT):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.

        Raises
        ------
        ValueError
            If the 'button_alignment' value is not in the range (1-3).
        """
        super().__init__(basic_piece, backgrounds[0], button_alignment)
        self.__backgrounds = backgrounds

    def start_other_elements(self) -> None:
        pass

    def run_another_action(self, selected_option: ButtonOption) -> None:
        if selected_option == ButtonOption.EASY:
            self.__update_difficulty(Difficulty.EASY)
            super().quit()
        elif selected_option == ButtonOption.MEDIUM:
            self.__update_difficulty(Difficulty.MEDIUM)
            super().quit()
        elif selected_option == ButtonOption.HARD:
            self.__update_difficulty(Difficulty.HARD)
            super().quit()
        elif selected_option == ButtonOption.BACK:
            super().quit()

    def create_buttons(self) -> list[Button]:
        buttons = [
            Button(ButtonOption.EASY),
            Button(ButtonOption.MEDIUM),
            Button(ButtonOption.HARD),
            Button(ButtonOption.BACK)
        ]
        return buttons

    def other_drawings(self, window: Surface) -> None:
        pass

    def other_updates(self) -> None:
        current_option = super().get_current_button_option()

        if current_option == ButtonOption.EASY:
            super().set_background(self.__backgrounds[0])
        elif current_option == ButtonOption.MEDIUM:
            super().set_background(self.__backgrounds[1])
        elif current_option == ButtonOption.HARD:
            super().set_background(self.__backgrounds[2])
        elif current_option == ButtonOption.BACK:
            super().set_background(self.__backgrounds[3])

    def __update_difficulty(self, difficulty: Difficulty) -> None:
        basic_piece = super().get_basic_piece()
        basic_piece.set_difficulty(difficulty)
