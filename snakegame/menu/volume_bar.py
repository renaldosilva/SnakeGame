import pygame
from pygame import Rect, Surface
from pygame.rect import RectType

from snakegame import constants, validation


class VolumeBar:
    """
    Represents a volume bar.

    Attributes
    ----------
    __size : int
        The size of the volume bar.
    __main_color : tuple[int, int, int]
        The main RGB color of the volume bar.
    __secondary_color : tuple[int, int, int]
        The secondary RGB color of the volume bar.
    __accent_color : tuple[int, int, int]
        The volume bar RGB accent color.
    __top_shape : Rect | RectType
        The top shape of the volume bar.
    __bottom_shape : Rect | RectType
        The bottom shape of the volume bar.
    __border_shape : Rect | RectType
        The border shape of the volume bar.
    """

    BORDER_RADIUS_PERCENTAGE = 0.6
    """The radius percentage of the volume bar borders.
    """

    EDGE_THICKNESS_PERCENTAGE = 0.17
    """The percentage of the volume bar border thickness.
    """

    WIDTH_FACTOR = 10
    """The volume bar width factor.
    """

    def __init__(
            self,
            size: int=constants.VOLUME_BAR_SIZE,
            main_color: tuple[int, int, int]=constants.DARK_GREEN,
            secondary_color: tuple[int, int, int]=constants.GREEN_2,
            accent_color: tuple[int, int, int]=constants.LIGHT_GREEN_2,
            coordinate: tuple[int, int]=(0, 0)
    ):
        """
        Initializes the VolumeBar class.

        Parameters
        ----------
        size : int, optional
            The size of the volume bar (default is constants.VOLUME_BAR_SIZE).
        main_color : tuple[int, int, int], optional
            The main RGB color of the volume bar (default is constants.DARK_GREEN).
        secondary_color : tuple[int, int, int], optional
            The secondary RGB color of the volume bar (default is constants.GREEN_2).
        accent_color : tuple[int, int, int], optional
            The volume bar RGB accent color (default is constants.LIGHT_GREEN_2).
        coordinate : tuple[int, int], optional
            The coordinate of the top-left corner of the volume bar (default is (0, 0)).
        """
        self.__size = validation.is_positive(size, "'size' cannot be less than 1!")
        self.__main_color = validation.is_valid_rgb(main_color, "'main_color' out of RGB range!")
        self.__secondary_color = validation.is_valid_rgb(secondary_color, "'secondary_color' out of RGB range!")
        self.__accent_color = validation.is_valid_rgb(accent_color, "'accent_color' out of RGB range!")
        self.__top_shape = self.__configure_top_shape(coordinate)
        self.__bottom_shape = self.__top_shape.copy()
        self.__border_shape = self.__top_shape.copy()

    def draw(self, window: Surface) -> None:
        """
        Draw the volume bar in the window.

        Parameters
        ----------
        window : Surface
            The window where the volume bar will be drawn.
        """
        border_radius = int(self.__size * VolumeBar.BORDER_RADIUS_PERCENTAGE)
        edge_thickness = int(self.__size * VolumeBar.EDGE_THICKNESS_PERCENTAGE)

        self.__draw_shape(self.__bottom_shape, window, border_radius, self.__secondary_color)
        self.__draw_shape(self.__top_shape, window, border_radius, self.__accent_color)
        self.__draw_shape(self.__border_shape, window, border_radius, self.__main_color, edge_thickness)

    def volume_up(self) -> None:
        """Turn up the volume level."""
        if self.__top_shape.width < self.__bottom_shape.width:
            increment = self.__bottom_shape.width // VolumeBar.WIDTH_FACTOR
            self.__top_shape.width += increment

    def volume_down(self) -> None:
        """Turn down the volume level."""
        if self.__top_shape.width > 0:
            decrement = self.__bottom_shape.width // VolumeBar.WIDTH_FACTOR
            self.__top_shape.width -= decrement

    def set_center(self, center) -> None:
        """
        Changes the center coordinate of the volume bar.

        Parameters
        ----------
        center : tuple[int, int]
            The new coordinate of the volume bar center.
        """
        self.__top_shape.center = center
        self.set_coordinate((self.__top_shape.x, self.__top_shape.y))

    def set_coordinate(self, coordinate: tuple[int, int]) -> None:
        """
        Set the (x, y) coordinate of the top-left corner of the volume bar.

        Parameters
        ----------
        coordinate : Tuple[int, int]
            The new (x, y) coordinate.
        """
        self.__top_shape.topleft = coordinate
        self.__bottom_shape.topleft = coordinate
        self.__border_shape.topleft = coordinate

    def __configure_top_shape(self, coordinate: tuple[int, int]) -> Rect:
        width =  self.__size * VolumeBar.WIDTH_FACTOR
        height = self.__size

        return pygame.Rect(coordinate, (width, height))

    @staticmethod
    def __draw_shape(
            background: Rect | RectType,
            window: Surface,
            border_radius: int,
            color: tuple[int, int, int],
            edge_thickness: int = 0
    ) -> None:
        pygame.draw.rect(window, color, background, edge_thickness, border_radius)
