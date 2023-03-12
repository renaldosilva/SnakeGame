from pygame.event import Event

from snakegame import constants, validation
from snakegame.text.text import Text
from snakegame import util


class AnimatedFont(Text):
    """
    A class that represents an animated text display where the font of
    the text changes periodically based on a timer event.

    Attributes
    ----------
    __content : str
        The text content.
    __size : int
        The font size for the text.
    __color : tuple[int, int, int]
        The RGB color value for the text.
    __font_path : str
        The path to the font file used for the text.
    __coordinate : tuple[int, int]
        The (x, y) coordinate of the top left corner of the text rectangle.
    __text : Surface | SurfaceType
        The Pygame surface object that contains the text.
    __rect : Rect | RectType
        The Pygame rectangle object that contains the dimensions and position of the text.
    __fonts_paths : list[str]
        A list of file paths to the different font files to be used for the animation.
    __font_event : int
        An event id for the timer event that triggers the font change.
    __current_font_path : int
        The index of the current font file being used for the animation.
    """

    def __init__(
        self,
        content: str,
        size: int = constants.TEXT_SIZE,
        color: tuple[int, int, int]=constants.DARK_GREEN,
        font_paths: list[str]=constants.FONTS,
        coordinate: tuple[int, int]=(0, 0),
    ):
        """
        Initializes a AnimatedFont object.

        Parameters
        ----------
        content : str
            The text content.
        size : int, optional
            The font size for the text (default is constants.TITLE_SIZE).
        color : tuple[int, int, int], optional
            The RGB color value for the text (default is constants.DARK_GREEN).
        font_paths : list[str], optional
            A list of file paths to the different font files to be used
            for the animation, (default is constants.FONT).
        coordinate : tuple[int, int], optional
            The (x, y) coordinate of the top left corner of the text rectangle (default is (0, 0)).

        Raises
        ------
        ValueError
            If the 'content' is empty, if 'size' is less than 1,
            if the 'color' is not in the RGB range (0-255, 0-255, 0-255)
            or if the list of font paths is empty.
        FileNotFoundError
            If the 'font_paths' is not found.
        """
        super().__init__(content, size, color, font_paths[0], coordinate)
        self.__fonts_paths = validation.check_paths(font_paths, "The list of font paths cannot be empty!")
        self.__font_event = util.configure_event(
            constants.ANIMATED_FONT_EVENT,
            constants.ANIMATED_FONT_MILLISECONDS
        )
        self.__current_font_path = 0

    def animate(self, event: Event) -> None:
        if event.type == self.__font_event:
            font_path = self.__fonts_paths[self.__current_font_path]
            super().set_font_path_keeping_center_coordinate(font_path)
            self.__update_current_font_path()

    def __update_current_font_path(self) -> None:
        if self.__current_font_path < len(self.__fonts_paths) - 1:
            self.__current_font_path += 1
        else:
            self.__current_font_path = 0
