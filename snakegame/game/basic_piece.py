import sys

import pygame
from pygame import display
from pygame import Surface
from pygame.time import Clock

from snakegame import constants
from snakegame import validation


class BasicPiece:
    """
    A class that provides basic functionality for creating a game.

    Attributes
    -----------
    window : Surface
        The surface to use as the game's main display window.
    clock : Clock
        The clock object used to manage the game's frame rate.
    fps : int, optional
        The target number of frames per second for the game (default is constants.GAME_FPS).
    color : tuple[int, int, int], optional
        The RGB color tuple used to fill the game's display window (default is constants.LIGHT_GREEN_1).
    is_running : bool
        A boolean value that indicates whether the game loop is still running.

    Methods
    -------
    clock_tick() -> None
        Regulates the game's frame rate by calling the Pygame Clock's tick() method with the FPS value.
    check_quit() -> None
        Checks for a quit event from the Pygame event queue, and sets is_running to False if found.
    update_window() -> None
        Calls the Pygame display's update() method to update the game window.
    draw_window() -> None
        Fills the game window with the background color specified by the color attribute.
    close_all() -> None
        Closes the Pygame window and exits the program.
    """

    def __init__(
        self,
        window: Surface,
        clock: Clock,
        fps: int = constants.GAME_FPS,
        color: tuple[int, int, int] = constants.LIGHT_GREEN_1,
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
        self.__fps = fps
        self.__color = color
        self.__is_running = True

    @property
    def window(self) -> Surface:
        """
        Get the Pygame Surface object that represents the game window.

        Returns
        -------
        window: Surface
            The game window.
        """
        return self.__window

    @property
    def clock(self) -> Clock:
        """
        Get the Pygame Clock object used to regulate the game's frame rate.

        Returns
        -------
        clock: Clock
            The game clock.
        """
        return self.__clock

    @property
    def fps(self) -> int:
        """
        Get the current frames per second (FPS) of the game.

        Returns
        -------
        fps: int
            The current FPS of the game.
        """
        return self.__fps

    @fps.setter
    def fps(self, fps: int) -> None:
        """
        Set the frames per second (FPS) of the game.

        Parameters
        ----------
        fps : int
            The new FPS.

        Raises
        ------
        ValueError
            If the specified FPS is less than 1.
        """
        if validation.is_smaller_than(fps, 1):
            raise ValueError("FPS must be greater than or equal to 1!")
        else:
            self.__fps = fps

    @property
    def color(self) -> tuple[int, int, int]:
        """
        Get the RGB color tuple used to fill the game window.

        Returns
        -------
        color: Tuple[int, int, int]
            The RGB color.
        """
        return self.__color

    @color.setter
    def color(self, color: tuple[int, int, int]) -> None:
        """
        Set the RGB color tuple used to fill the game window.

        Parameters
        ----------
        color : Tuple[int, int, int]
            The new RGB color.

        Raises
        ------
        ValueError
            If the RGB values in the tuple are not in the range (0, 255).
        """
        if validation.is_invalid_rgb(color):
            raise ValueError("The R, G and B channels must be in range (0, 255)!")

    @property
    def is_running(self) -> bool:
        """
        Get the running state of the game loop.

        Returns
        -------
        is_running: bool
           True if the game loop is running, False otherwise.
        """
        return self.__is_running

    @is_running.setter
    def is_running(self, value: bool) -> None:
        """
        Set the running state of the game loop.

        Parameters
        ----------
        value : bool
            The new running state.
        """
        self.__is_running = value

    def clock_tick(self) -> None:
        """Regulates the game's frame rate by calling the Pygame Clock's tick() method with the FPS value."""
        self.clock.tick(self.fps)

    def check_quit(self) -> None:
        """Checks for a quit event from the Pygame event queue, and sets is_running to False if found."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    @staticmethod
    def update_window() -> None:
        """Calls the Pygame display's update() method to update the game window."""
        display.update()

    def draw_window(self) -> None:
        """Fills the game window with the background color specified by the color attribute."""
        self.window.fill(self.color)

    @staticmethod
    def close_all() -> None:
        """Closes the Pygame window and exits the program."""
        pygame.quit()
        sys.exit()
