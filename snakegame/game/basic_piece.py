import sys

import pygame
from pygame import display
from pygame import Surface
from pygame.event import Event
from pygame.time import Clock

from snakegame import constants
from snakegame import validation


class BasicPiece:
    """
    A class that provides basic functionality for creating a game.

    Attributes
    ----------
    window : Surface
        The surface to use as the game's main display window.
    clock : Clock
        The clock object used to manage the game's frame rate.
    fps : int, optional
        The target number of frames per second for the game (default is constants.GAME_FPS).
    color : tuple[int, int, int], optional
        The RGB color tuple used to fill the game's display window (default is constants.LIGHT_GREEN_1).
    game_pixel_dimension : int, optional
        The pixel dimension used in the game (default is constants.GAME_PIXEL_DIMENSION).
    is_running : bool
        A boolean value that indicates whether the game loop is still running.
    """

    def __init__(
        self,
        window: Surface,
        clock: Clock,
        fps: int=constants.GAME_FPS,
        color: tuple[int, int, int]=constants.LIGHT_GREEN_1,
        game_pixel_dimension: int=constants.GAME_PIXEL_DIMENSION
    ):
        """
        Initializes a new instance of the BasicPiece class.

        Parameters
        -----------
        window : Surface
            The surface to use as the game's main display window.
        clock : Clock
            The clock object used to manage the game's frame rate.
        fps : int, optional
            The target number of frames per second for the game (default is constants.GAME_FPS).
        color : tuple[int, int, int], optional
            The RGB color tuple used to fill the game's display window (default is constants.LIGHT_GREEN_1).
        """
        self.__window = window
        self.__clock = clock
        self.__fps = validation.is_positive(fps, "'fps' cannot be less than 1!")
        self.__color = validation.is_valid_rgb(color, "'color' out of RGB range!")
        self.__game_pixel_dimension = validation.is_positive(
            game_pixel_dimension,
            "'game_pixel_dimension' cannot be less than 1!"
        )
        self.__is_running = True

    def get_window(self) -> Surface:
        """
        Returns the Pygame Surface object that represents the game window.

        Returns
        -------
        window : Surface
            The game window.
        """
        return self.__window

    def get_window_height(self) -> int:
        """
        Returns the height of the window.

        Returns
        -------
        int
            The height of the window.
        """
        return self.__window.get_height()

    def get_window_width(self) -> int:
        """
        Returns the width of the window.

        Returns
        -------
        int
            The width of the window.
        """
        return self.__window.get_width()

    def get_game_pixel_dimension(self) -> int:
        """
        returns the pixel dimension used in the game.

        Returns
        -------
        int
            The pixel dimension.
        """
        return self.__game_pixel_dimension

    def is_running(self) -> bool:
        """
        Returns the running state of the game loop.

        Returns
        -------
        is_running : bool
           True if the game loop is running, False otherwise.
        """
        return self.__is_running

    def clock_tick(self) -> None:
        """Regulates the game's frame rate by calling the Pygame Clock's tick() method with the FPS value."""
        self.__clock.tick(self.__fps)

    @staticmethod
    def get_events() -> list[Event]:
        """Returns the list of game events."""
        return pygame.event.get()

    def check_quit(self, event: Event) -> None:
        """Checks for a quit event from the Pygame event queue, and sets is_running to False if found."""
        if event.type == pygame.QUIT:
            self.__is_running = False

    @staticmethod
    def update_window() -> None:
        """Calls the Pygame display's update() method to update the game window."""
        display.update()

    def draw_window(self) -> None:
        """Fills the game window with the background color specified by the color attribute."""
        self.__window.fill(self.__color)

    @staticmethod
    def close_all() -> None:
        """Closes the Pygame window and exits the program."""
        pygame.quit()
        sys.exit()
