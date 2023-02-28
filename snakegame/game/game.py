from snakegame.game.basic_piece import BasicPiece


class Game:
    """
    A class that represents the game loop.

    Attributes
    ----------
    basic_piece : BasicPiece
       Used to handle basic game functionality.

    Methods
    -------
    start() -> None
       Starts the game loop.
    """
    def __init__(
            self,
            basic_piece: BasicPiece
    ):
        """
        Initialize a new Game object.

        Parameters
        ----------
        basic_piece : BasicPiece
            Used to handle basic game functionality.
        """
        self.__basic_piece = basic_piece

    def start(self) -> None:
        """Starts the game loop."""
        self._loop()

    def _loop(self) -> None:
        while self.basic_piece.is_running:
            self._events()
            self._draw()
            self._update()
            self.basic_piece.clock_tick()
        self.basic_piece.close_all()

    def _events(self) -> None:
        self.basic_piece.check_quit()

    def _update(self) -> None:
        self.basic_piece.update_window()

    def _draw(self) -> None:
        self.basic_piece.draw_window()

    @property
    def basic_piece(self) -> BasicPiece:
        """
        Get the basic piece object associated with the game.

        Returns
        -------
        BasicPiece
            The basic piece.
        """
        return self.__basic_piece
