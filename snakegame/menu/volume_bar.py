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
        The main RGB color of the volume bar used on the edge of the top shape.
    __secondary_color : tuple[int, int, int]
        The secondary RGB color of the volume bar used in the bottom shape.
    __accent_color : tuple[int, int, int]
        The accent RGB color of the volume bar used in the top shape.
    __top_shape : Rect | RectType
        The top shape of the volume bar.
    __bottom_shape : Rect | RectType
        The bottom shape of the volume bar.
    __border_radius : int
        The radius of the volume bar.
    __edge_thickness : int
        The thickness of the volume bar border.
    __volume_step : int
        The size that the bar can be increased or decreased with each manipulation of the volume.
    """

    BORDER_RADIUS_PERCENTAGE = 0.4
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
            The main RGB color of the volume bar used on the edge of the top shape (default is constants.DARK_GREEN).
        secondary_color : tuple[int, int, int], optional
            The secondary RGB color of the volume bar used in the bottom shape (default is constants.GREEN_2).
        accent_color : tuple[int, int, int], optional
            The accent RGB color of the volume bar used in the top shape (default is constants.LIGHT_GREEN_2).
        coordinate : tuple[int, int], optional
            The coordinate of the top-left corner of the volume bar (default is (0, 0)).
        """
        self.__size = validation.is_positive(size, "'size' cannot be less than 1!")
        self.__main_color = validation.is_valid_rgb(main_color, "'main_color' out of RGB range!")
        self.__secondary_color = validation.is_valid_rgb(secondary_color, "'secondary_color' out of RGB range!")
        self.__accent_color = validation.is_valid_rgb(accent_color, "'accent_color' out of RGB range!")
        self.__top_shape = self.__configure_top_shape(coordinate)
        self.__bottom_shape = self.__top_shape.copy()
        self.__border_radius = int(self.__size * VolumeBar.BORDER_RADIUS_PERCENTAGE)
        self.__edge_thickness = int(self.__size * VolumeBar.EDGE_THICKNESS_PERCENTAGE)
        self.__volume_step = self.__bottom_shape.width // VolumeBar.WIDTH_FACTOR

    def draw(self, window: Surface) -> None:
        """
        Draw the volume bar in the window.

        Parameters
        ----------
        window : Surface
            The window where the volume bar will be drawn.
        """
        pygame.draw.rect(
            window, self.__secondary_color, self.__bottom_shape,
            border_radius=self.__border_radius
        )
        pygame.draw.rect(
            window, self.__accent_color, self.__top_shape,
            border_radius=self.__border_radius
        )
        pygame.draw.rect(
            window, self.__main_color,  self.__top_shape,
            self.__edge_thickness, self.__border_radius
        )

    def volume_up(self) -> None:
        """Turn up the volume level."""
        if self.__top_shape.width < self.__bottom_shape.width:
            self.__top_shape.width += self.__volume_step

    def volume_down(self) -> None:
        """Turn down the volume level."""
        if self.__top_shape.width > 0:
            self.__top_shape.width -= self.__volume_step

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

    def __configure_top_shape(self, coordinate: tuple[int, int]) -> Rect:
        width, height =  self.__size*VolumeBar.WIDTH_FACTOR, self.__size

        return pygame.Rect(coordinate, (width, height))
