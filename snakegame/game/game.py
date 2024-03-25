import pygame
from pygame.key import ScancodeWrapper

from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.main_menu import MainMenu
from snakegame.menu.record_manager import RecordManager
from snakegame.menu.sound_manager import SoundManager
from snakegame.menu.timer import Timer


class Game:
    """
    A class that represents the game.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
        The sound manager of the game.
    __record_manager : RecordManager
        The record manager.
    __menu : MainMenu
        The game menu.
    __timer : Timer
        The game timer.
    """

    KEYS = {
        "pause": pygame.K_p
    }

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            record_manager: RecordManager
    ):
        """
        Initialize a Game object.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        record_manager : RecordManager
            The record manager.
        """
        self.__basic_piece = basic_piece
        self.__sound_manager = sound_manager
        self.__record_manager = record_manager
        self.__menu = MainMenu(basic_piece, sound_manager, record_manager)
        self.__timer = Timer(basic_piece, sound_manager)

    def start(self) -> None:
        """Starts the game loop."""
        self.__loop()

    def __loop(self) -> None:
        while True:
            if self.__basic_piece.get_game_state() == GameState.MENU:
                self.__menu.start()
            elif self.__basic_piece.get_game_state() == GameState.PAUSE:
                self.__menu.start_pause_menu()
            elif self.__basic_piece.get_game_state() == GameState.TIMER:
                self.__draw()
                self.__timer.start()
            elif self.__basic_piece.get_game_state() == GameState.GAME:
                self.__events()
                self.__draw()
                self.__update()

            self.__basic_piece.clock_tick()

    def __events(self) -> None:
        for event in self.__basic_piece.get_events():
            self.__basic_piece.check_quit(event)

        pressed_keys = pygame.key.get_pressed()

        self.__manage_pause(pressed_keys)

    def __update(self) -> None:
        self.__basic_piece.update_window()

    def __draw(self) -> None:
        self.__basic_piece.draw_window()

    def __manage_pause(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[Game.KEYS.get("pause")]:
            self.__basic_piece.set_game_state(GameState.PAUSE)
