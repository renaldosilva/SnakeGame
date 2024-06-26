import pygame
from pygame.key import ScancodeWrapper

from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.loading import Loading
from snakegame.menu.main_menu import MainMenu
from snakegame.menu.score_manager import ScoreManager
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
    __score_manager : ScoreManager
        The score manager.
    __menu : MainMenu
        The game menu.
    __timer : Timer
        The game timer.
    __loading : Loading
        The game loading.
    """

    KEYS = {
        "pause": pygame.K_p
    }

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            score_manager: ScoreManager
    ):
        """
        Initialize a Game object.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        score_manager : ScoreManager
            The score manager.
        """
        self.__basic_piece = basic_piece
        self.__sound_manager = sound_manager
        self.__score_manager = score_manager
        self.__menu = MainMenu(basic_piece, sound_manager, score_manager)
        self.__timer = Timer(basic_piece, sound_manager)
        self.__loading = Loading(basic_piece)

    def start(self) -> None:
        """Starts the game loop."""
        self.__loop()

    def __loop(self) -> None:
        while True:
            game_state = self.__basic_piece.get_game_state()

            if game_state == GameState.MENU:
                self.__menu.start()
            elif game_state == GameState.PAUSE:
                self.__menu.start_pause_menu()
            elif game_state == GameState.TIMER:
                self.__draw()
                self.__timer.start()
            elif game_state == GameState.LOADING:
                self.__loading.start()
            elif game_state == GameState.GAME:
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
        self.__basic_piece.get_window_manager().update_window()

    def __draw(self) -> None:
        self.__basic_piece.get_window_manager().draw_window()

    def __manage_pause(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[Game.KEYS.get("pause")]:
            self.__basic_piece.set_game_state(GameState.PAUSE)
