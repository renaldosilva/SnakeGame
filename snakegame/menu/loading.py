import random
import time

from pygame import Surface, SurfaceType, Rect
from pygame.rect import RectType

from snakegame import constants, validation, util
from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.background import Background
from snakegame.text.animated_text import AnimatedText


class Loading:
    """
    Represents a loading screen. Each time it is launched, a background image is chosen to appear.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : Background
        The loading background.
    __seconds : int
        The seconds of the loading screen.
    __dimensions : tuple[int, int]
        The height and width of the loading screen.
    __image_path_lists : list[list[str]]
        the image path lists.
    __image_lists : list | list[list[tuple[Surface | SurfaceType, Rect | RectType]]]
        The image lists.
    __start_time : int
        The time in seconds that the loading screen started.
    """
    def __init__(
            self,
            basic_piece: BasicPiece,
            background: Background = Background(
                AnimatedText(constants.LOADING_TITLE),
                constants.BOTTOM_ALIGNMENT
            ),
            seconds: int = constants.LOADING_SECONDS,
            dimensions: tuple[int, int] = constants.WINDOW_DIMENSIONS,
            image_path_lists: list[list[str]] = constants.LOADING_IMAGE_LISTS
    ):
        """
        Initializes the loading screen.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        background : Background, optional
            The loading background
            (default is Background(AnimatedText(constants.LOADING_TITLE), constants.BOTTOM_ALIGNMENT)).
        seconds : int, optional
            The seconds of the loading screen (default is constants.LOADING_SECONDS).
        dimensions : tuple[int, int], optional
            The height and width of the loading screen (default is constants.WINDOW_DIMENSIONS).
        image_path_lists : list[list[str]], optional
            the image path lists (default is constants.LOADING_IMAGE_LISTS).

        Raises
        ------
        ValueError
            If 'seconds' is not a positive value, if 'dimensions' are not positive values or
            if any of the 'image_path_lists' are empty.
        FileNotFoundError
            If any image path is not found.
        """
        self.__basic_piece = basic_piece
        self.__background = background
        self.__seconds = validation.is_positive(seconds, "'seconds' cannot be less than 1!")
        self.__dimensions = validation.is_valid_dimensions(dimensions, "All dimensions must be greater than zero!")
        self.__image_path_lists = self.__check_image_path_lists(image_path_lists)
        self.__image_lists = self.__load_images()
        self.__start_time = 0

    def start(self) -> None:
        """
        Starts the loading screen.
        """
        self.__start_time = time.time()
        self.__set_random_image_list()
        self.__loop()

    def __loop(self) -> None:
        while self.__there_is_time():
            self.__events()
            self.__draw()
            self.__update()
            self.__basic_piece.clock_tick()
        self.__stop()

    def __events(self) -> None:
        for event in self.__basic_piece.get_events():
            self.__basic_piece.check_quit(event)
            self.__background.events(event)

    def __draw(self) -> None:
        self.__background.draw(self.__basic_piece.get_window_manager().get_window())

    def __update(self) -> None:
        self.__basic_piece.get_window_manager().update_window()

    def __there_is_time(self) -> bool:
        current_seconds = time.time() - self.__start_time
        return current_seconds < self.__seconds

    def __stop(self) -> None:
        self.__start_time = 0
        self.__select_next_game_state()

    def __select_next_game_state(self) -> None:
        last_game_state = self.__basic_piece.get_last_game_state()

        if last_game_state == GameState.MENU:
            self.__basic_piece.set_game_state(GameState.TIMER)
        elif last_game_state == GameState.PAUSE:
            self.__basic_piece.set_game_state(GameState.MENU)

    def __set_random_image_list(self) -> None:
        amount = len(self.__image_lists)
        index = random.randint(0, amount - 1)

        self.__background.change_image_list(self.__image_lists[index])

    @staticmethod
    def __check_image_path_lists(image_lists: list[list[str]]) -> list[list[str]]:
        lists = []
        for image_list in image_lists:
            result = validation.check_paths(image_list, "'images_path' not found!")
            lists.append(result)

        return lists

    def __load_images(self) -> list | list[list[tuple[Surface | SurfaceType, Rect | RectType]]]:
        image_lists = []
        for image_paths in self.__image_path_lists:
            current_list = []
            for image in util.load_images(image_paths, self.__dimensions):
                current_list.append((image, image.get_rect()))

            image_lists.append(current_list)

        return image_lists
