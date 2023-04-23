import pygame
from pygame.key import ScancodeWrapper

from snakegame.enuns.game_state import GameState
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.main_menu import MainMenu


class Game:
    """
    A class that represents the game.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __menu : MainMenu
        The game menu.
    """

    def __init__(
            self,
            basic_piece: BasicPiece
    ):
        """
        Initialize a Game object.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        """
        self.__basic_piece = basic_piece
        self.__menu = MainMenu(basic_piece)

    def start(self) -> None:
        """Starts the game loop."""
        self.__loop()

    def __loop(self) -> None:
        while self.__basic_piece.is_running():
            if self.__basic_piece.get_game_state() == GameState.MENU:
                self.__menu.start()
            elif self.__basic_piece.get_game_state() == GameState.PAUSE:
                self.__menu.start_pause_menu()
            elif self.__basic_piece.get_game_state() == GameState.GAME:
                self.__events()
                self.__draw()
                self.__update()

            self.__basic_piece.clock_tick()
        self.__basic_piece.close_all()

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
        if pressed_keys[pygame.K_p]:
            self.__basic_piece.set_game_state(GameState.PAUSE)
