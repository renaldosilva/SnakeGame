import sys

import pygame
from pygame import display
from pygame import Surface
from pygame.time import Clock

from snakegame import constants


class BasicPiece:
    """
    A class used to represent the basic pieces of a game.

    Attributes
    ----------
    window: Surface
        The window where the game is displayed.
    clock : Clock
        The clock that manages the game's frame rate.
    fps: int
        The game frame rate
    color : tuple[int, int, int]
        The main color of the window background.
    """

    def __init__(
            self,
            window: Surface,
            clock: Clock,
            fps: int=constants.GAME_FPS,
            color: tuple[int, int, int]=constants.LIGHT_GREEN_1
    ):
        """
        Parameters
        ----------
        window: Surface
            The window where the game is displayed.
        clock : Clock
            The clock that manages the game's frame rate.
        fps: int
            The game frame rate
        color : tuple[int, int, int]
            The main color of the window background.
        """
        self._window = window
        self._clock = clock
        self._fps = fps
        self._color = color
        self._is_running = True

    def is_running(self) -> bool:
        """
        Informs if the game is running.

        Returns
        -------
        is_running: bool
            True when running or false otherwise.
        """
        return self._is_running

    def get_window(self) -> Surface:
        """
        Get the window where the game is displayed.

        Returns
        -------
        canvas: Surface
            The canvas.
        """
        return self._window

    def clock_tick(self) -> None:
        """Controls the game's frame rate."""
        self._clock.tick(self._fps)

    def check_quit(self) -> None:
        """Checks if the player wants to close the game window."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._is_running = False

    @staticmethod
    def update_window():
        """Update the game window."""
        display.update()

    def draw_window(self) -> None:
        """Draws the game window with a solid color."""
        self._window.fill(self._color)

    @staticmethod
    def close_all() -> None:
        """Ends all execution."""
        pygame.quit()
        sys.exit()
