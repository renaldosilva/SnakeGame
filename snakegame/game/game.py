from snakegame.game.basic_piece import BasicPiece


class Game:
    """
    A class used to represent a game.

    The game has a main loop where events are handled,
    drawn in the window and updated.

    Attributes
    ----------
    basic_piece: BasicPiece
        The basic pieces of the game.
    """

    def __init__(
            self,
            basic_piece: BasicPiece
    ):
        """
        Parameters
        ----------
        basic_piece: BasicPiece
            The basic pieces of the game.
        """
        self._basic_piece = basic_piece

    def start(self) -> None:
        """Start the game loop."""
        self._loop()

    def _loop(self) -> None:
        while self._basic_piece.is_running():
            self._events()
            self._draw()
            self._update()
            self._basic_piece.clock_tick()
        self._basic_piece.close_all()

    def _events(self) -> None:
        self._basic_piece.check_quit()

    def _update(self) -> None:
        self._basic_piece.update_window()

    def _draw(self) -> None:
        self._basic_piece.draw_window()
