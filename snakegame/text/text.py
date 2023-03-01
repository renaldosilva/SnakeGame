import pygame.font
from pygame.font import Font
from pygame.rect import Rect
from pygame.rect import RectType
from pygame.surface import Surface
from pygame.surface import SurfaceType

from snakegame import validation
from snakegame import constants


class Text:
    """
    A class for creating text objects to be displayed on a window.

    Attributes
    ----------
    content : str
        The text content.
    size : int
        The font size for the text.
    color : tuple[int, int, int]
        The RGB color value for the text.
    font_path : str
        The path to the font file used for the text.
    coordinate : tuple[int, int]
        The (x, y) coordinate of the top left corner of the text rectangle.
    text : Surface | SurfaceType
        The Pygame surface object that contains the text.
    rect : Rect | RectType
        The Pygame rectangle object that contains the dimensions and position of the text.

    Methods
    -------
    draw(window: Surface) -> None:
        Draws the text on a given window.
    set_size_keeping_center_coordinate(size) -> None:
        Changes the size of the text, keeping the center coordinate unchanged.
    set_x(x: int) -> None:
        Changes the x-coordinate of the top left corner of the text.
    set_y(y: int) -> None:
        Changes the y-coordinate of the top left corner of the text.
    set_center(center: tuple[int, int]) -> None:
        Changes the center coordinate of the text.
    set_center_x(x: int) -> None:
        Changes the x-coordinate of the center of the text.
    get_center() -> tuple[int, int]:
        Returns the center coordinate of the text.
    get_center_y() -> int:
        Returns the y-coordinate of the center of the text.
    set_midtop(midtop: tuple[int, int]) -> None:
        Changes the position of the top center of the text.
    get_height() -> int:
        Returns the height of the text.
    get_width() -> int:
        Returns the width of the text.
    get_middle_bottom() -> tuple[int, int]:
        Returns the coordinates of the center of the bottom edge of the text.
    """
    def __init__(
            self,
            content: str,
            size: int,
            color: tuple[int, int, int]=constants.DARK_GREEN,
            font_path: str = constants.FONT,
            coordinate: tuple[int, int]=(0, 0)
    ):
        """
        Initializes a Text object.

        Parameters
        ----------
        content : str
            The text content.
        size : int
            The font size for the text.
        color : tuple[int, int, int], optional
            The RGB color value for the text (default is constants.DARK_GREEN).
        font_path : str, optional
            The path to the font file used for the text (default is constants.FONT).
        coordinate : tuple[int, int], optional
            The (x, y) coordinate of the top left corner of the text rectangle (default is (0, 0)).
        """
        pygame.font.init()
        self.__content = content
        self.__size = size
        self.__color = color
        self.__font_path = font_path
        self.__coordinate = coordinate
        self.__text = self.__configure_text()
        self.__rect = self.__configure_rect(self.text)

    @property
    def content(self) -> str:
        """
        Returns the text content.

        Returns
        -------
        content: str
            The content.
        """
        return self.__content

    @content.setter
    def content(self, content: str) -> None:
        """
        Set the text content.

        Parameters
        ----------
        content: str
            The new text content.

        Raises
        ------
        ValueError
            If the new text content is empty.
        """
        if content == "":
            raise ValueError("Content cannot be empty!")
        else:
            self.__content = content
            self.__reload_elements()

    @property
    def size(self) -> int:
        """
        Returns the font size for the text.

        Returns
        -------
        size: int
            The text size.
        """
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        """
        Set the text size.

        Parameters
        ----------
        size : int
            The new text size.

        Raises
        ------
        ValueError
            If the specified text size is less than 1.
        """
        if size < 1:
            raise ValueError("Size must be greater than or equal to 1!")
        else:
            self.__size = size
            self.__reload_elements()

    @property
    def color(self) -> tuple[int, int, int]:
        """
        Returns the RGB color value for the text.

        Returns
        -------
        color: Tuple[int, int, int]
            The RGB color.
        """
        return self.__color

    @color.setter
    def color(self, color: tuple[int, int, int]) -> None:
        """
        Set the RGB color value for the text.

        Parameters
        ----------
        color : Tuple[int, int, int]
            The new RGB color.

        Raises
        ------
        ValueError
            If the RGB values in the tuple are not in the range (0, 255).
        """
        if validation.is_invalid_rgb(color):
            raise ValueError("The R, G and B channels must be in range (0, 255)!")
        else:
            self.__color = color
            self.__reload_text()

    @property
    def font_path(self) -> str:
        """
        Returns the path to the font file.

        Returns
        -------
        font_path: str
            The font path.
        """
        return self.__font_path

    @font_path.setter
    def font_path(self, font_path: str) -> None:
        """
        Set the path to the font file used by this text object.

        Parameters
        ----------
        font_path: str
            The path to the new font file.

        Raises
        ------
        FileNotFoundError
            If the new font file path is not found.
        """
        if validation.is_invalid_path(font_path):
            raise FileNotFoundError("Font_path not found!")
        else:
            self.__font_path = font_path
            self.__reload_elements()

    @property
    def coordinate(self) -> tuple[int, int]:
        """
        Returns the (x, y) coordinate of the top-left corner of the text.

        Returns
        -------
        coordinate: Tuple[int, int]
            The (x, y) coordinate.
        """
        return self.__coordinate

    @coordinate.setter
    def coordinate(self, coordinate: tuple[int, int]) -> None:
        """
        Set the (x, y) coordinate of the top-left corner of the text.

        Parameters
        ----------
        coordinate : Tuple[int, int]
            The new (x, y) coordinate.

        Raises
        ------
        ValueError
            If the coordinate is invalid and goes beyond the limits of the window.
        """
        if validation.is_invalid_coordinate(coordinate):
            raise ValueError("The coordinate of the top-left cannot go beyond the limits of the window.")
        else:
            self.__coordinate = coordinate
            self.__reload_rect()

    @property
    def text(self) -> Surface | SurfaceType:
        """
        Returns the rendered text as a pygame Surface object.

        Returns
        -------
        text: Surface | SurfaceType
            The rendered text.
        """
        return self.__text

    @property
    def rect(self) -> Rect | RectType:
        """
        Returns the rect of the text.

        Returns
        -------
        rect : Rect | RectType
            The rect.
        """
        return self.__rect

    def draw(self, window: Surface) -> None:
        """
        Draw the text in the window.

        Parameters
        ----------
        window: Surface
            The window where the text will be drawn.
        """
        window.blit(self.text, self.rect)

    def set_size_keeping_center_coordinate(self, size) -> None:
        """
        Changes the size of the text, keeping the center coordinate unchanged.

        Parameters
        ----------
        size: int
            The new text size.
        """
        current_center = self.rect.center
        self.size = size
        self.set_center(current_center)

    def set_x(self, x: int) -> None:
        """
        Changes the x-coordinate of the top left corner of the text.

        Parameters
        ----------
        x: int
            The new x-coordinate.
        """
        self.coordinate = x, self.coordinate[1]

    def set_y(self, y: int) -> None:
        """
        Changes the y-coordinate of the top left corner of the text.

        Parameters
        ----------
        y: int
            The new y-coordinate.
        """
        self.coordinate = self.coordinate[0], y

    def set_center(self, center: tuple[int, int]) -> None:
        """
        Changes the center coordinate of the text.

        Parameters
        ----------
        center: tuple[int, int]
            The new coordinate of the text center.
        """
        self.rect.center = center
        self.coordinate = self.rect.x, self.rect.y

    def set_center_x(self, x: int) -> None:
        """
        Changes the x-coordinate of the center of the text.

        Parameters
        ----------
        x: int
            The new x-coordinate of the center
        """
        self.set_center((x, self.rect.center[1]))

    def get_center(self) -> tuple[int, int]:
        """
        Returns the center coordinate of the text.

        Returns
        -------
        center: tuple[int, int]
            The center coordinate.
        """
        return self.rect.center

    def get_center_y(self) -> int:
        """
        Returns the y-coordinate of the center of the text.

        Returns
        -------
        y: int
            The y-coordinate of the center.
        """
        return self.rect.center[1]

    def set_midtop(self, midtop: tuple[int, int]):
        """
        Changes the position of the top center of the text.

        Parameters
        ----------
        midtop: tuple[int, int]
            The new midtop-coordinate.
        """
        self.rect.midtop = midtop
        self.coordinate = self.rect.x, self.rect.y

    def get_height(self) -> int:
        """
        Returns the height of the text.

        Returns
        -------
        height: int
            The height of the text.
        """
        return self.rect.height

    def get_width(self) -> int:
        """
        Returns the width of the text.

        Returns
        -------
        width: int
            The width of the text.
        """
        return self.rect.width

    def get_middle_bottom(self) -> tuple[int, int]:
        """
        Returns the coordinates of the center of the bottom edge of the text.

        Returns
        -------
        midbottom: tuple[int, int]
            The midbottom-coordinate.
        """
        return self.rect.midbottom

    def __configure_text(self) -> Surface | SurfaceType:
        font = Font(self.font_path, self.size)
        text = font.render(self.content, True, self.color)
        return text

    def __configure_rect(self, text: Surface | SurfaceType) -> Rect | RectType:
        rect = text.get_rect()
        rect.x, rect.y = self.coordinate
        return rect

    def __reload_elements(self) -> None:
        self.__reload_text()
        self.__reload_rect()

    def __reload_text(self) -> None:
        self.__text = self.__configure_text()

    def __reload_rect(self) -> None:
        self.__rect = self.__configure_rect(self.text)
