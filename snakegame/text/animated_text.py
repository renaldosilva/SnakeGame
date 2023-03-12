from pygame.event import Event

from snakegame.animation.animation import Animation
from snakegame.animation.horizontal_swing import HorizontalSwing
from snakegame.text.text import Text
from snakegame import constants
from snakegame import util


class AnimatedText(Text):
    """
    Represents an animated line of text.

    Default animation is horizontal movement from left to right and vice versa.

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
    __animation: Animation
        The text animation (default animation is HorizontalSwing).
    __animation_event: int
        The id of the animation event.
    """

    def __init__(
            self,
            content: str,
            size: int=constants.TEXT_SIZE,
            color: tuple[int, int, int] = constants.DARK_GREEN,
            font_path: str = constants.FONT,
            coordinate: tuple[int, int]=(0, 0)
    ):
        """
        Initializes an AnimatedText object.

        Parameters
        ----------
        content : str
            The text content.
        size : int, optional
            The font size for the text (default is constants.TITLE_SIZE).
        color : tuple[int, int, int], optional
            The RGB color value for the text (default is constants.DARK_GREEN).
        font_path : str, optional
            The path to the font file used for the text (default is constants.FONT).
        coordinate : tuple[int, int], optional
            The (x, y) coordinate of the top left corner of the text rectangle (default is (0, 0)).

        Raises
        ------
        ValueError
            If the 'content' is empty, if 'size' is less than 1 or
            if the 'color' is not in the RGB range (0-255, 0-255, 0-255).
        FileNotFoundError
            If the 'font_path' is not found.
        """
        super().__init__(content, size, color, font_path, coordinate)
        self.__animation: Animation = HorizontalSwing(super().get_rect())
        self.__animation_event = util.configure_event(
            constants.ANIMATED_TEXT_EVENT,
            constants.ANIMATED_TEXT_MILLISECONDS
        )

    def animate(self, event: Event) -> None:
        if event.type == self.__animation_event:
            self.__animation.animate()

    def set_content(self, content: str) -> None:
        super().set_content(content)
        self.__reload_animation()

    def set_size(self, size: int) -> None:
        super().set_size(size)
        self.__reload_animation()

    def set_font_path(self, font_path: str) -> None:
       super().set_font_path(font_path)
       self.__reload_animation()

    def set_coordinate(self, coordinate: tuple[int, int]) -> None:
        super().set_coordinate(coordinate)
        self.__reload_animation()

    def set_size_keeping_center_coordinate(self, size) -> None:
        super().set_size_keeping_center_coordinate(size)
        self.__reload_animation()

    def set_center(self, center: tuple[int, int]) -> None:
        super().set_center(center)
        self.__reload_animation()

    def __reload_animation(self) -> None:
        self.__animation.reload_animation(super().get_rect())
