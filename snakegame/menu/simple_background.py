import pygame
from pygame import Surface, Rect
from pygame.event import Event

from snakegame.text.text import Text
from snakegame.text.animated_text import AnimatedText
from snakegame import constants
from snakegame import validation


class SimpleBackground:
    """
    Represents a simple screen with title and background.

    Attributes
    ----------
    title : Text
        The title of the menu which can be animated or not.
    text_alignment : {1, 2, 3}
        Represents is the title alignment:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    width, height : int
        The width and height dimensions.
    pixel_dimension : int
        The pixel dimension.
    color : tuple[int, int, int]
        The background color.
    background: str
        The background image.
    """

    def __init__(
            self,
            title: Text,
            title_alignment: int=1,
            dimensions: tuple[int, int]=constants.WINDOW_DIMENSIONS,
            pixel_dimension: int=constants.GAME_PIXEL_DIMENSION,
            color: tuple[int, int, int]=constants.LIGHT_GREEN_1,
            image_path: str=None
    ):
        """
        Initialize a simple background.

        Parameters
        ----------
        title : Text
            The title of the menu which can be animated or not.
        text_alignment : {1, 2, 3}, optional
            Represents is the title alignment (default is 1):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
        dimensions : tuple[int, int], optional
            The width and height dimensions (default is constants.WINDOW_DIMENSIONS).
        pixel_dimension : int, optional
            The pixel dimension (default is constants.GAME_PIXEL_DIMENSION).
        color : tuple[int, int, int], optional
            The background color (default is constants.LIGHT_GREEN_1).
        image_path : str, optional
            The background image path (default is None).

        Raises
        ------
        ValueError
            If the 'text_alignment' is not a valid value, if 'dimensions' are not positive values,
            if 'pixel_dimension' is not positive or if the 'color' is not in the RGB range
            (0-255, 0-255, 0-255).
        FileNotFoundError
            If the 'image_path' is not found.
        """
        self.__title = title
        self.__text_alignment = self.__check_title_alignment(title_alignment)
        self.__width = validation.is_positive(dimensions[0], "The 'width' cannot be less than 1!")
        self.__height = validation.is_positive(dimensions[1], "The 'height' cannot be less than 1!")
        self.__pixel_dimension = validation.is_positive(
            pixel_dimension, "The 'pixel_dimension' cannot be less than 1!"
        )
        self.__color = validation.is_valid_rgb(color, "'background_color' out of RGB range!")
        self.__background: Surface | Rect = self.__configure_background(image_path)
        self.__align_title()

    def events(self, event: Event) -> None:
        """Updates the title animation. If the title is not animated, nothing will be done."""
        if isinstance(self.__title, AnimatedText):
            self.__title.animate(event)

    def draw(self, window: Surface) -> None:
        """Draw the simple background on the window."""
        self.__draw_background(window)
        self.__title.draw(window)

    def get_dimensions(self) -> tuple[int, int]:
        """
        Returns the width and height dimensions of the background.

        Returns
        -------
        tuple[int, int]
            The width and height.
        """
        return self.__width, self.__height

    def __configure_background(self, background_image_path: str) -> Surface | Rect:
        if background_image_path:
            validation.is_valid_path(background_image_path, "'background_image_path' not found!")
            background = pygame.image.load(background_image_path)
            background = pygame.transform.scale(background, self.get_dimensions())
        else:
            background = Rect((0, 0), self.get_dimensions())

        return background

    def __draw_background(self, window: Surface) -> None:
        if type(self.__background) is Surface:
            window.blit(self.__background, (0, 0))
        else:
            pygame.draw.rect(window, self.__color, self.__background)

    def __align_title(self) -> None:
        if self.__text_alignment == 1:
            self.__align_title_to_top()
        elif self.__text_alignment == 2:
            self.__align_title_to_center()
        else:
            self.__align_title_to_bottom()

    def __align_title_to_top(self) -> None:
        midtop = self.__width // 2, self.__pixel_dimension*2
        self.__title.set_midtop(midtop)

    def __align_title_to_center(self) -> None:
        center = self.__width // 2, self.__height // 2
        self.__title.set_center(center)

    def __align_title_to_bottom(self) -> None:
        midbottom = self.__width // 2, self.__height - self.__pixel_dimension*2
        self.__title.set_midbottom(midbottom)

    @staticmethod
    def __check_title_alignment(title_alignment: int) -> int:
        if title_alignment not in [1, 2, 3]:
            raise ValueError("Text alignment does not have a valid value! possible values are 1, 2 and 3.")

        return title_alignment
