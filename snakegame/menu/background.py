import pygame
from pygame import Surface, Rect, SurfaceType
from pygame.event import Event
from pygame.rect import RectType

from snakegame.text.text import Text
from snakegame import constants, util
from snakegame import validation


class Background:
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
    __color : tuple[int, int, int]
        The background color.
    __images : list[Surface | SurfaceType]
        Background image list.
    __image_event : int
        The ID of the pygame event that triggers the image change.
    __current_image : int
        The index of the current image being used.
    __background : str
        The background image.
    """

    TITLE_MARGIN_PERCENTAGE = 0.04
    """The percentage of distance between the title and the background edge.
    """

    def __init__(
            self,
            title: Text,
            title_alignment: int=1,
            dimensions: tuple[int, int]=constants.WINDOW_DIMENSIONS,
            color: tuple[int, int, int]=constants.LIGHT_GREEN_1,
            image_paths: list[str]=None,
            image_event: int=util.configure_event(
                constants.IMAGE_EVENT,
                constants.IMAGE_MILLISECONDS
            )
    ):
        """
        Initialize a Background.

        Parameters
        ----------
        title : Text
            The title of the menu which can be animated or not.
        title_alignment : {1, 2, 3}, optional
            Represents is the title alignment (default is 1):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.
        dimensions : tuple[int, int], optional
            The width and height dimensions (default is constants.WINDOW_DIMENSIONS).
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
            If the 'text_alignment' is not a valid value, if 'dimensions' are not positive values
            or if the 'color' is not in the RGB range (0-255, 0-255, 0-255).
        FileNotFoundError
            If the 'image_path' is not found.
        """
        self.__title = title
        self.__text_alignment = self.__check_title_alignment(title_alignment)
        self.__dimensions = validation.is_valid_dimensions(dimensions, "All dimensions must be greater than zero!")
        self.__color = validation.is_valid_rgb(color, "'background_color' out of RGB range!")
        self.__image_paths = validation.check_paths(image_paths, "'background_image_path' not found!", True)
        self.__images = self.__load_images()
        self.__image_event = image_event
        self.__current_image = 0
        self.__background: Rect | tuple[Surface | SurfaceType, Rect | RectType] = self.__configure_background()
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
        self.__change_background(event)

    def draw(self, window: Surface) -> None:
        """
        Draw the background on the window.

        Parameters
        ----------
        window : Surface
            The window where the background will be drawn.
        """
        self.__draw_background(window)
        self.__title.draw(window)

    def set_center(self, center: tuple[int, int]) -> None:
        """
        Changes the center coordinate of the background.

        Parameters
        ----------
        center : tuple[int, int]
            The new coordinate of the background center.
        """
        if type(self.__background) is Rect:
            self.__background.center = center
        else:
            for _, rect in self.__images:
                rect.center = center

        self.__align_title()

    def get_center(self) -> tuple[int, int]:
        """
        Returns the center coordinate of the background.

        Returns
        -------
        center : tuple[int, int]
            The center coordinate.
        """
        if type(self.__background) is Rect:
            center = self.__background.center
        else:
            _, rect = self.__background
            center = rect.center

        return center

    def get_midtop(self) -> tuple[int, int]:
        """
        Returns the center coordinates of the top.

        Returns
        -------
        tuple[int, int]
            The midtop-coordinate.
        """
        if type(self.__background) is Rect:
            midtop = self.__background.midtop
        else:
            _, rect = self.__background
            midtop = rect.midtop

        return midtop

    def get_midbottom(self) -> tuple[int, int]:
        """
        Returns the center coordinates of the bottom.

        Returns
        -------
        tuple[int, int]
            The midbottom-coordinate.
        """
        if type(self.__background) is Rect:
            midbottom = self.__background.midbottom
        else:
            _, rect = self.__background
            midbottom = rect.midbottom

        return midbottom

    def get_height(self) -> int:
        """
        Returns the height of the background.

        Returns
        -------
        int
            The height of the background.
        """
        return self.__dimensions[1]

    def change_image_list(self, images: list | list[tuple[Surface | SurfaceType, Rect | RectType]]) -> None:
        """
        Changes the list of images used in the background.

        Parameters
        ----------
        images : list | list[tuple[Surface | SurfaceType, Rect | RectType]]
            The list of images.
        """
        self.__images = images
        self.__background = self.__configure_background()

    def reset_image_loop(self) -> None:
        """Resets the background image loop so that whenever it starts, it starts from the first image."""
        self.__current_image = 0
        self.__background = self.__configure_background()

    def __load_images(self) -> list | list[tuple[Surface | SurfaceType, Rect | RectType]]:
        images = []
        for image in util.load_images(self.__image_paths, self.__dimensions):
            images.append((image, image.get_rect()))

        return images

    def __configure_background(self) -> Rect | tuple[Surface | SurfaceType, Rect | RectType]:
        if self.__images:
            background = self.__images[self.__current_image]
        else:
            background = Rect((0, 0), self.__dimensions)

        return background

    def __draw_background(self, window: Surface) -> None:
        if type(self.__background) is Rect:
            pygame.draw.rect(window, self.__color, self.__background)
        else:
            image, rect = self.__background
            window.blit(image, rect)

    def __align_title(self) -> None:
        if self.__text_alignment == 1:
            self.__align_title_to_top()
        elif self.__text_alignment == 2:
            self.__align_title_to_center()
        else:
            self.__align_title_to_bottom()

    def __align_title_to_top(self) -> None:
        midtop_x, midtop_y = self.get_midtop()
        midtop = midtop_x, midtop_y + self.__calculate_title_margin()
        self.__title.set_midtop(midtop)

    def __align_title_to_center(self) -> None:
        self.__title.set_center(self.get_center())

    def __align_title_to_bottom(self) -> None:
        midbottom_x, midbottom_y = self.get_midbottom()
        midbottom = midbottom_x, midbottom_y - self.__calculate_title_margin()
        self.__title.set_midbottom(midbottom)

    def __calculate_title_margin(self) -> int:
        return int(self.get_height() * Background.TITLE_MARGIN_PERCENTAGE)

    def __change_background(self, event: Event) -> None:
        if type(self.__background) is not Rect and event.type == self.__image_event:
            self.__change_current_image()
            self.__background = self.__images[self.__current_image]

    def __change_current_image(self) -> None:
        if self.__current_image < len(self.__images) - 1:
            self.__current_image += 1
        else:
            self.__current_image = 0

    @staticmethod
    def __check_title_alignment(title_alignment: int) -> int:
        if title_alignment not in [1, 2, 3]:
            raise ValueError("Text alignment does not have a valid value! possible values are 1, 2 and 3.")

        return title_alignment
