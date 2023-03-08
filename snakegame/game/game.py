from snakegame.game.basic_piece import BasicPiece


class Game:
    """
    A class that represents the game loop.

    Attributes
    ----------
    basic_piece : BasicPiece
       Used to handle basic game functionality.
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
        self.__loop()

    def __loop(self) -> None:
        while self.__basic_piece.is_running():
            self.__events()
            self.__draw()
            self.__update()
            self.__basic_piece.clock_tick()
        self.__basic_piece.close_all()

    def __events(self) -> None:
        for event in self.__basic_piece.get_events():
            self.__basic_piece.check_quit(event)

    def __update(self) -> None:
        self.__basic_piece.update_window()

    def __draw(self) -> None:
        self.__basic_piece.draw_window()
