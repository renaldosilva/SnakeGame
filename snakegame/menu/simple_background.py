import pygame
from pygame import Surface, Rect
from pygame.event import Event

from snakegame.text.text import Text
from snakegame import constants, util
from snakegame import validation


class SimpleBackground:
    """
    Represents a simple screen with title and background.
    The background may change periodically when you have more than one image.

    Attributes
    ----------
    __title : Text
        The title of the menu which can be animated or not.
    __text_alignment : {1, 2, 3}
        Represents is the title alignment:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    __width, __height : int
        The width and height dimensions.
    __pixel_dimension : int
        The pixel dimension.
    __color : tuple[int, int, int]
        The background color.
    __images : list[Surface | SurfaceType]
        Background image list.
    __image_event : int
        The ID of the pygame event that triggers the image change.
    __current_image_path : int
        The index of the current image being used.
    __background : str
        The background image.
    """

    def __init__(
            self,
            title: Text,
            title_alignment: int=1,
            dimensions: tuple[int, int]=constants.WINDOW_DIMENSIONS,
            pixel_dimension: int=constants.GAME_PIXEL_DIMENSION,
            color: tuple[int, int, int]=constants.LIGHT_GREEN_1,
            image_paths: list[str]=None,
            image_event: int=util.configure_event(
                constants.IMAGE_EVENT,
                constants.IMAGE_MILLISECONDS
            )
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
        image_paths : list[str], optional
            The background image paths (default is None).
        image_event : int, optional
            The ID of the pygame event that triggers the image change
            (default is util.configure_event(constants.IMAGE_EVENT, constants.IMAGE_MILLISECONDS)).

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
        self.__images = self.__configure_images(
            validation.check_paths(image_paths, "'background_image_path' not found!", True)
        )
        self.__image_event = image_event
        self.__current_image_path = 0
        self.__background: Surface | Rect = self.__configure_background()
        self.__align_title()

    def events(self, event: Event) -> None:
        """
        Manages titles and background animations, if any.

        Parameters
        ----------
        event : Event
            A pygame event.
        """
        self.__title.animate(event)

        if event.type == self.__image_event:
            self.__update_current_image_path()
            self.__background = self.__configure_background()

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

    def __configure_images(self, image_paths: list[str]) -> list[Surface] | list:
        images = []
        if image_paths:
            for image_path in image_paths:
                image = pygame.image.load(image_path)
                image = pygame.transform.scale(image, self.get_dimensions())
                images.append(image)

        return images

    def __configure_background(self) -> Surface | Rect:
        if self.__images:
            background = self.__images[self.__current_image_path]
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

    def __update_current_image_path(self) -> None:
        if self.__current_image_path < len(self.__images) - 1:
            self.__current_image_path += 1
        else:
            self.__current_image_path = 0

    @staticmethod
    def __check_title_alignment(title_alignment: int) -> int:
        if title_alignment not in [1, 2, 3]:
            raise ValueError("Text alignment does not have a valid value! possible values are 1, 2 and 3.")

        return title_alignment
