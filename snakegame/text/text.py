from abc import abstractmethod

import pygame.font
from pygame.event import Event
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
    """

    def __init__(
            self,
            content: str,
            size: int=constants.TEXT_SIZE,
            color: tuple[int, int, int]=constants.DARK_GREEN,
            font_path: str=constants.FONT,
            coordinate: tuple[int, int]=(0, 0)
    ):
        """
        Initializes a Text object.

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
        pygame.font.init()
        self.__content = validation.is_empty(content, "'content' cannot be empty!")
        self.__size = validation.is_positive(size, "'size' cannot be less than 1!")
        self.__color = validation.is_valid_rgb(color, "'color' out of RGB range!")
        self.__font_path = validation.is_valid_path(font_path, "'font_path' not found!")
        self.__coordinate = coordinate
        self.__text = self.__configure_text()
        self.__rect = self.__configure_rect()

    def set_content(self, content: str) -> None:
        """
        Set the text content.

        Parameters
        ----------
        content : str
            The new text content.

        Raises
        ------
        ValueError
            If the new text content is empty.
        """
        self.__content = validation.is_empty(content, "Content cannot be empty!")
        self.__reload_elements()

    def get_size(self) -> int:
        """
        Returns the font size for the text.

        Returns
        -------
        size : int
            The text size.
        """
        return self.__size

    def set_size(self, size: int) -> None:
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
        self.__size = validation.is_positive(size, "'size' cannot be less than 1!")
        self.__reload_elements()

    def set_color(self, color: tuple[int, int, int]) -> None:
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
        self.__color = validation.is_valid_rgb(color, "'color' out of RGB range!")
        self.__reload_text()

    def get_font_path(self) -> str:
        """
        Returns the path to the font file.

        Returns
        -------
        font_path : str
            The font path.
        """
        return self.__font_path

    def set_font_path(self, font_path: str) -> None:
        """
        Set the path to the font file used by this text object.

        Parameters
        ----------
        font_path : str
            The path to the new font file.

        Raises
        ------
        FileNotFoundError
            If the new font file path is not found.
        """
        self.__font_path = validation.is_valid_path(font_path, "'font_path' not found!")
        self.__reload_elements()

    def set_font_path_keeping_center_coordinate(self, font_path: str) -> None:
        """
        Set the path to the font file used by this text object, keeping the center coordinate unchanged.

        Parameters
        ----------
        font_path : str
            The path to the new font file.
        """
        current_center = self.__rect.center
        self.set_font_path(font_path)
        self.set_center(current_center)

    def get_coordinate(self) -> tuple[int, int]:
        """
        Returns the (x, y) coordinate of the top-left corner of the text.

        Returns
        -------
        coordinate : Tuple[int, int]
            The (x, y) coordinate.
        """
        return self.__coordinate

    def set_coordinate(self, coordinate: tuple[int, int]) -> None:
        """
        Set the (x, y) coordinate of the top-left corner of the text.

        Parameters
        ----------
        coordinate : Tuple[int, int]
            The new (x, y) coordinate.
        """
        self.__coordinate = coordinate
        self.__reload_rect()

    def get_text(self) -> Surface | SurfaceType:
        """
        Returns the rendered text as a pygame Surface object.

        Returns
        -------
        text : Surface | SurfaceType
            The rendered text.
        """
        return self.__text

    def get_rect(self) -> Rect | RectType:
        """
        Returns the rect of the text.

        Returns
        -------
        rect : Rect | RectType
            The rect.
        """
        return self.__rect

    @abstractmethod
    def animate(self, event: Event) -> None:
        """
        Animate the text.

        Parameters
        ----------
        event: Event
            A pygame event.
        """
        pass

    def draw(self, window: Surface) -> None:
        """
        Draw the text in the window.

        Parameters
        ----------
        window : Surface
            The window where the text will be drawn.
        """
        window.blit(self.__text, self.__rect)

    def set_size_keeping_center_coordinate(self, size) -> None:
        """
        Changes the size of the text, keeping the center coordinate unchanged.

        Parameters
        ----------
        size : int
            The new text size.
        """
        current_center = self.__rect.center
        self.set_size(size)
        self.set_center(current_center)

    def get_center(self) -> tuple[int, int]:
        """
        Returns the center coordinate.

        Returns
        -------
        tuple[int, int]
            The center coordinate (x, y).
        """
        return self.__rect.center

    def set_center(self, center: tuple[int, int]) -> None:
        """
        Changes the center coordinate of the text.

        Parameters
        ----------
        center : tuple[int, int]
            The new coordinate of the text center.
        """
        self.__rect.center = center
        self.set_coordinate((self.__rect.x, self.__rect.y))

    def set_midtop(self, midtop: tuple[int, int]) -> None:
        """
        Changes the position of the top center of the text.

        Parameters
        ----------
        midtop : tuple[int, int]
            The new midtop-coordinate.
        """
        self.__rect.midtop = midtop
        self.set_coordinate((self.__rect.x, self.__rect.y))

    def set_midbottom(self, midbottom: tuple[int, int]) -> None:
        """
        Changes the position of the bottom center of the text.

        Parameters
        ----------
        midbottom : tuple[int, int]
            The new midbottom-coordinate.
        """
        self.__rect.midbottom = midbottom
        self.set_coordinate((self.__rect.x, self.__rect.y))

    def get_height(self) -> int:
        """
        Returns the height of the text.

        Returns
        -------
        int
            The height of the text.
        """
        return self.__rect.height

    def get_width(self) -> int:
        """
        Returns the width of the text.

        Returns
        -------
        int
            The width of the text.
        """
        return self.__rect.width

    def __configure_text(self) -> Surface | SurfaceType:
        font = Font(self.__font_path, self.__size)
        text = font.render(self.__content, True, self.__color)
        return text

    def __configure_rect(self) -> Rect | RectType:
        rect = self.__text.get_rect()
        rect.x, rect.y = self.get_coordinate()
        return rect

    def __reload_elements(self) -> None:
        self.__reload_text()
        self.__reload_rect()

    def __reload_text(self) -> None:
        self.__text = self.__configure_text()

    def __reload_rect(self) -> None:
        self.__rect = self.__configure_rect()
