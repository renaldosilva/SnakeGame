import pygame
from pygame import Rect
from pygame.rect import RectType

from snakegame import util, constants, validation
from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.sound_manager import SoundManager
from snakegame.text.text import Text


class Timer:
    """
    Represents a timer.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
        The sound manager of the game.
    __seconds : int
        The seconds that the timer will be active.
    __size : int
        The size of the timer.
    __number_color : tuple[int, int, int]
        The color of the timer number.
    __background_color : tuple[int, int, int]
        The timer background color.
    __number : Text
        The text representing the seconds.
    __background : Rect
        The timer background.
    __border_radius : int
        The radius of the timer.
    __timer_event : int
        The ID of the pygame event that triggers the timer count.
    __seconds_aux : int
        Auxiliary variable for counting seconds.
    """

    BORDER_RADIUS_PERCENTAGE = 0.25
    """The radius percentage of the timer borders.
    """

    WIDTH_FACTOR = 0.5
    """The timer width factor.
    """

    HEIGHT_FACTOR = 0.3
    """The timer height factor.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            seconds: int = constants.TIMER_SECONDS,
            size: int = constants.TIMER_SIZE,
            number_color: tuple[int, int, int] = constants.LIGHT_GREEN_2,
            background_color: tuple[int, int, int] = constants.DARK_GREEN,
            font_path: str = constants.FONT,
            timer_event: int = util.configure_event(
                constants.TIMER_EVENT,
                constants.TIMER_MILLISECONDS
            )
    ):
        """
        Initialize a Timer.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        seconds : int, optional
            The seconds that the timer will be active (default is constants.TIMER_SECONDS).
        size : int, optional
            The size of the timer (default is constants.TIMER_SIZE).
        number_color : tuple[int, int, int], optional
            The color of the timer number (default is constants.LIGHT_GREEN_2).
        background_color : tuple[int, int, int], optional
            The timer background color (default is constants.DARK_GREEN).
        font_path : str, optional
            The path to the font file used for the text (default is constants.FONT).
        timer_event : int, optional
            The ID of the pygame event that triggers the timer count
            (default is util.configure_event(constants.TIMER_EVENT, constants.TIMER_MILLISECONDS)).
        """
        self.__basic_piece = basic_piece
        self.__sound_manager = sound_manager
        self.__seconds = validation.is_positive(seconds, "'seconds' cannot be less than 1!")
        self.__size = validation.is_positive(size, "'size' cannot be less than 1!")
        self.__number_color = validation.is_valid_rgb(number_color, "'number_color' out of RGB range!")
        self.__background_color = validation.is_valid_rgb(background_color, "'background_color' out of RGB range!")
        self.__number = self.__configure_number(font_path)
        self.__background = self.__configure_background()
        self.__border_radius = int(self.__size * Timer.BORDER_RADIUS_PERCENTAGE)
        self.__align_elements()
        self.__timer_event = timer_event
        self.__seconds_aux = self.__seconds

    def start(self) -> None:
        """
        Start the timer.
        """
        self.__loop()

    def __loop(self) -> None:
        while self.__seconds_aux > -1:
            self.__events()
            self.__draw()
            self.__update()
            self.__basic_piece.clock_tick()
        self.__stop()

    def __events(self) -> None:
        for event in self.__basic_piece.get_events():
            self.__basic_piece.check_quit(event)

            if event.type == self.__timer_event:
                if self.__seconds_aux > 0:
                    self.__number.set_content(str(self.__seconds_aux))
                    self.__sound_manager.play_sound("time_tick")

                self.__seconds_aux -= 1

    def __draw(self) -> None:
        window = self.__basic_piece.get_window()

        pygame.draw.rect(window, self.__background_color, self.__background, border_radius=self.__border_radius)
        self.__number.draw(self.__basic_piece.get_window())

    def __update(self) -> None:
        self.__basic_piece.update_window()

    def __stop(self) -> None:
        self.__number.set_content(str(self.__seconds))
        self.__seconds_aux = self.__seconds
        self.__select_next_game_state()

    def __select_next_game_state(self) -> None:
        last_game_state = self.__basic_piece.get_last_game_state()

        if last_game_state == GameState.LOADING:
            self.__basic_piece.set_game_state(GameState.GAME)
        elif last_game_state == GameState.PAUSE:
            self.__basic_piece.set_game_state(GameState.GAME)

    def __configure_number(self, font_path) -> Text:
        return Text(str(self.__seconds), self.__size, self.__number_color, font_path)

    def __configure_background(self) -> Rect | RectType:
        width = self.__number.get_width() + self.__size * Timer.WIDTH_FACTOR
        height = self.__number.get_height() + self.__size * Timer.HEIGHT_FACTOR

        return Rect((0, 0), (width, height))

    def __align_elements(self) -> None:
        center = self.__basic_piece.get_window_center()
        self.__number.set_center(center)
        self.__background.center = center
