from abc import ABC, abstractmethod
from typing import Any

from pygame import Rect


class Animation(ABC):
    """
    Abstract base class representing an animation.

    An animation runs on a main rectangle and the secondary rectangles follow the movement.

    Attributes
    ----------
    __main_rectangle : Rect
        The main rectangle of the animation.
    __secondary_rectangles : list[Rect] | None
        The list of secondary rectangles of the animation.
    __origin_coordinate : tuple[int, int]
        The origin coordinate of the animation
        (corresponding to the upper left corner of the main rectangle).
    """

    def __init__(self, main_rectangle: Rect, secondary_rectangles: list[Rect]=None):
        """
        Initialize the animation object.

        Parameters
        ----------
        main_rectangle : Rect
            The main rectangle of the animation.
        secondary_rectangles : list[Rect] | None, optional
            The list of secondary rectangles of the animation (default is NONE).
        """
        self.__main_rectangle = main_rectangle
        self.__secondary_rectangles = secondary_rectangles
        self.__origin_coordinate = self.__main_rectangle.x, self.__main_rectangle.y

    def get_main_rectangle(self) -> Rect:
        """
        Returns the main rectangle of the animation.

        Returns
        -------
        main_rect: Rect
            The main rectangle.
        """
        return self.__main_rectangle

    def get_origin_coordinate(self) -> tuple[int, int]:
        """
        Returns the origin coordinate of the animation
        (corresponding to the upper left corner of the main rectangle)..

        Returns
        -------
        origin_coordinate: tuple[int, int]
            The origin coordinate.
        """
        return self.__origin_coordinate

    @abstractmethod
    def animate(self, extra: tuple[Any, ...]=None) -> None:
        """
        Abstract method that performs the animation.

        Notes
        -----
        it is possible to pass extra parameters according to the need of the animation.
        """
        pass

    def reload_animation(self, main_rectangle: Rect, secondary_rectangles: list[Rect]=None) -> None:
        """
        Reloads the animation with new main and secondary rectangles.

        Parameters
        ----------
        main_rectangle : Rect
            The main rectangle of the animation.
        secondary_rectangles : list[Rect] | None, optional
            The list of secondary rectangles of the animation (default is NONE).
        """
        self.__main_rectangle = main_rectangle
        self.__secondary_rectangles = secondary_rectangles
        self.__origin_coordinate = self.__main_rectangle.x, self.__main_rectangle.y

    def restore_origin_coordinate(self) -> None:
        """Restores the initial position of the rectangles."""
        self.set_current_coordinate(self.__origin_coordinate)

    def set_current_coordinate(self, coordinate: tuple[int, int]) -> None:
        """
        Sets the current position of the main rectangle
        (secondary rectangles will follow the movement).

        Parameters
        ----------
        coordinate : tuple[int, int]
            The new coordinate.
        """
        step_size_in_x, step_size_in_y = self.__calculate_step_size(coordinate)
        self.__main_rectangle.x, self.__main_rectangle.y = coordinate
        self.__move_secondary_rectangles(step_size_in_x, step_size_in_y)

    def set_current_coordinate_x(self, x: int) -> None:
        """
        Sets the current x-coordinate of the main rectangle
        (secondary rectangles will follow the movement).

        Parameters
        ----------
        x : int
            The new x-coordinate.
        """
        self.set_current_coordinate((x, self.__main_rectangle.y))

    def set_current_coordinate_y(self, y: int) -> None:
        """
        Sets the current y-coordinate of the main rectangle
        (secondary rectangles will follow the movement).

        Parameters
        ----------
        y : int
            The new y-coordinate.
        """
        self.set_current_coordinate((self.__main_rectangle.x, y))

    def get_current_coordinate_x(self) -> int:
        """
        Returns the current x-coordinate of the main rectangle.

        Returns
        -------
        int
            The current x-coordinate.
        """
        return self.__main_rectangle.topleft[0]

    def get_current_coordinate_y(self) -> int:
        """
        Returns the current y-coordinate of the main rectangle.

        Returns
        -------
        int
            The current y-coordinate.
        """
        return self.__main_rectangle.topleft[1]

    def get_origin_coordinate_x(self) -> int:
        """
        Returns the origin x-coordinate of the animation.

        Returns
        -------
        int
            The origin x-coordinate.
        """
        return self.__origin_coordinate[0]

    def get_origin_coordinate_y(self) -> int:
        """
        Returns the origin y-coordinate of the animation.

        Returns
        -------
        int
            The origin y-coordinate.
        """
        return self.__origin_coordinate[1]

    def __calculate_step_size(self, coordinate: tuple[int, int]) -> tuple[int, int]:
        step_size_in_x = coordinate[0] - self.__main_rectangle.x
        step_size_in_y = coordinate[1] - self.__main_rectangle.y

        return step_size_in_x, step_size_in_y

    def __move_secondary_rectangles(self, step_size_in_x: int, step_size_in_y: int) -> None:
        if self.__secondary_rectangles:
            for rect in self.__secondary_rectangles:
                rect.x = rect.x + step_size_in_x
                rect.y = rect.y + step_size_in_y
