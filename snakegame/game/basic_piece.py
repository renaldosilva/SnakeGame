import sys

import pygame
from pygame.event import Event
from pygame.time import Clock

from snakegame import constants
from snakegame import validation
from snakegame.enuns.game_state import GameState
from snakegame.game.window_manager import WindowManager


class BasicPiece:
    """
    A class that provides basic functionality for creating a game.

    Attributes
    ----------
    __game_state : GameState
        Indicates the state of the game.
    __last_game_state : GameState
        Saves the last game state.
    __window_manager : WindowManager
        The window manager in which the game will be displayed.
    __clock : Clock
        The clock object used to manage the game's frame rate.
    __fps : int, optional
        The target number of frames per second for the game.
    """

    WAITING_TIME_TO_CLOSE = 350
    """Wait time to close (milliseconds).
    """

    def __init__(
        self,
        window_manager: WindowManager,
        clock: Clock,
        fps: int=constants.GAME_FPS
    ):
        """
        Initializes a new instance of the BasicPiece class.

        Parameters
        -----------
        window_manager : WindowManager
            The window manager in which the game will be displayed.
        clock : Clock
            The clock object used to manage the game's frame rate.
        fps : int, optional
            The target number of frames per second for the game (default is constants.GAME_FPS).

        Raises
        ------
        ValueError
                If 'fps' is less than 1.
        """
        self.__game_state = GameState.MENU
        self.__last_game_state = GameState.MENU
        self.__window_manager = window_manager
        self.__clock = clock
        self.__fps = validation.is_positive(fps, "'fps' cannot be less than 1!")

    def set_game_state(self, game_state: GameState) -> None:
        """
        Set the game state.

        Parameters
        ----------
        game_state : GameState
            The new game state.
        """
        self.__last_game_state = self.__game_state
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

    def get_last_game_state(self) -> GameState:
        """
        Returns the last state of the game.

        Returns
        -------
        last_game_state : GameState
            The last game state.
        """
        return self.__last_game_state

    def get_window_manager(self) -> WindowManager:
        """Returns the window manager."""
        return self.__window_manager

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
    def close_all() -> None:
        """Closes the Pygame window and exits the program."""
        pygame.time.wait(BasicPiece.WAITING_TIME_TO_CLOSE)
        pygame.quit()
        sys.exit()
