import sys

import pygame
from pygame import display
from pygame import Surface
from pygame.event import Event
from pygame.time import Clock

from snakegame import constants
from snakegame import validation
from snakegame.enuns.game_state import GameState


class BasicPiece:
    """
    A class that provides basic functionality for creating a game.

    Attributes
    ----------
    __game_state : GameState
        Indicates the state of the game.
    __window : Surface
        The surface to use as the game's main display window.
    __clock : Clock
        The clock object used to manage the game's frame rate.
    __fps : int, optional
        The target number of frames per second for the game.
    __color : tuple[int, int, int]
        The RGB color tuple used to fill the game's display window.
    """

    WAITING_TIME_TO_CLOSE = 350
    """Wait time to close (milliseconds).
    """

    def __init__(
        self,
        window: Surface,
        clock: Clock,
        fps: int=constants.GAME_FPS,
        color: tuple[int, int, int]=constants.LIGHT_GREEN_1
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
        self.__game_state = GameState.MENU
        self.__window = window
        self.__clock = clock
        self.__fps = validation.is_positive(fps, "'fps' cannot be less than 1!")
        self.__color = validation.is_valid_rgb(color, "'color' out of RGB range!")

    def set_game_state(self, game_state: GameState) -> None:
        """
        Set the game state.

        Parameters
        ----------
        game_state : GameState
            The new game state.
        """
        self.__game_state = game_state

    def get_game_state(self) -> GameState:
        """
        Returns the state of the game.

        Returns
        -------
        game_state : GameState
            The game state.
        """
        return self.__game_state

    def get_window(self) -> Surface:
        """
        Returns the Pygame Surface object that represents the game window.

        Returns
        -------
        window : Surface
            The game window.
        """
        return self.__window

    def clock_tick(self) -> None:
        """Regulates the game's frame rate by calling the Pygame Clock's tick() method with the FPS value."""
        self.__clock.tick(self.__fps)

    @staticmethod
    def get_events() -> list[Event]:
        """Returns the list of game events."""
        return pygame.event.get()

    def check_quit(self, event: Event) -> None:
        """
        Checks for a quit event from the Pygame event queue, and sets is_running to False if found.

        Parameters
        ----------
        event : Event
            The game event.
        """
        if event.type == pygame.QUIT:
            self.close_all()

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
        pygame.time.wait(BasicPiece.WAITING_TIME_TO_CLOSE)
        pygame.quit()
        sys.exit()
