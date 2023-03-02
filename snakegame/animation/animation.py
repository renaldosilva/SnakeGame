from abc import ABC, abstractmethod

from pygame import Rect

from snakegame import validation


class Animation(ABC):
    """
    Abstract base class representing an animation.

    An animation runs on a main rectangle and the secondary rectangles follow the movement.

    Attributes
    ----------
    main_rect : Rect
        The main rectangle of the animation.
    secondary_rectangles : list[Rect] | None
        The list of secondary rectangles of the animation.
    origin_coordinate : tuple[int, int]
        The origin coordinate of the animation
        (corresponding to the upper left corner of the main rectangle).

    Methods
    -------
    animate(*extra)
        Abstract method that performs the animation.
    reload_animation(main_rect: Rect, secondary_rectangles: list[Rect] | None=None)
        Reloads the animation with new main and secondary rectangles.
    restore_origin_coordinate()
        Restores the initial position of the rectangles.
    set_current_coordinate(coordinate: Tuple[int, int])
        Sets the current position of the main rectangle.
    set_current_coordinate_x(x: int)
        Sets the current x-coordinate of the main rectangle.
    set_current_coordinate_y(y: int)
        Sets the current y-coordinate of the main rectangle.
    get_current_coordinate_x() -> int
        Returns the current x-coordinate of the main rectangle.
    get_current_coordinate_y() -> int
        Returns the current y-coordinate of the main rectangle.
    get_origin_coordinate_x() -> int
        Returns the x-coordinate of the origin coordinate of the animation.
    get_origin_coordinate_y() -> int
        Returns the y-coordinate of the origin coordinate of the animation.
    """
    def __init__(self, main_rectangle: Rect, secondary_rectangles: list[Rect]=None):
        """
        Initialize the animation object.

        Parameters
        ----------
        main_rect : Rect
            The main rectangle of the animation.
        secondary_rectangles : list[Rect] | None, optional
            The list of secondary rectangles of the animation (default is NONE).
        """
        self.__main_rect = main_rectangle
        self.__secondary_rectangles = secondary_rectangles
        self.__origin_coordinate = self.main_rect.x, self.main_rect.y

    @property
    def main_rect(self) -> Rect:
        """
        Returns the main rectangle of the animation.

        Returns
        -------
        main_rect: Rect
            The main rectangle.
        """
        return self.__main_rect

    @main_rect.setter
    def main_rect(self, rect: Rect) -> None:
        """
        Sets the main rectangle of the animation.

        Parameters
        ----------
        rect : Rect
            The main rectangle of the animation.
        """
        self.__main_rect = rect

    @property
    def secondary_rectangles(self) -> list[Rect] | None:
        """
        Returns the list of secondary rectangles.

        Returns
        -------
        secondary_rectangles: list[Rect] | None
            The list of secondary rectangles or NONE if the list is empty.
        """
        return self.__secondary_rectangles

    @secondary_rectangles.setter
    def secondary_rectangles(self, rectangles: list[Rect] | None) -> None:
        """
        Sets the list of secondary rectangles.

        Parameters
        ----------
        rectangles : list[pygame.Rect] | None, optional
            The list of secondary rectangles (default is NONE).
        """
        self.__secondary_rectangles = rectangles

    @property
    def origin_coordinate(self) -> tuple[int, int]:
        """
        Returns the origin coordinate of the animation
        (corresponding to the upper left corner of the main rectangle)..

        Returns
        -------
        origin_coordinate: tuple[int, int]
            The origin coordinate.
        """
        return self.__origin_coordinate

    @origin_coordinate.setter
    def origin_coordinate(self, coordinate: tuple[int, int]) -> None:
        """
        Sets the origin coordinate of the animation
        (corresponding to the upper left corner of the main rectangle).

        Parameters
        ----------
        coordinate : tuple[int, int]
            The new origin coordinate of the animation.

        Raises
        ------
        ValueError
            If the coordinate is invalid and goes beyond the limits of the window.
        """
        if validation.is_invalid_coordinate(coordinate):
            raise ValueError("The origin coordinate of the top-left cannot go beyond the limits of the window.")
        else:
            self.__origin_coordinate = coordinate
            self.set_current_coordinate(coordinate)

    @abstractmethod
    def animate(self, *extra) -> None:
        """Abstract method that performs the animation."""
        pass

    def reload_animation(self, main_rect: Rect, secondary_rectangles: list[Rect]=None):
        """
        Reloads the animation with new main and secondary rectangles.

        Parameters
        ----------
        main_rect : Rect
            The main rectangle of the animation.
        secondary_rectangles : list[Rect] | None, optional
            The list of secondary rectangles of the animation (default is NONE).
        """
        self.main_rect = main_rect
        self.secondary_rectangles = secondary_rectangles
        self.origin_coordinate = self.main_rect.x, self.main_rect.y

    def restore_origin_coordinate(self) -> None:
        """Restores the initial position of the rectangles."""
        self.set_current_coordinate(self.origin_coordinate)

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
        self.main_rect.x, self.main_rect.y = coordinate
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
        self.set_current_coordinate((x, self.main_rect.y))

    def set_current_coordinate_y(self, y: int) -> None:
        """
        Sets the current y-coordinate of the main rectangle
        (secondary rectangles will follow the movement).

        Parameters
        ----------
        y : int
            The new y-coordinate.
        """
        self.set_current_coordinate((self.main_rect.x, y))

    def get_current_coordinate_x(self) -> int:
        """
        Returns the current x-coordinate of the main rectangle.

        Returns
        -------
        x: int
            The current x-coordinate.
        """
        return self.main_rect.topleft[0]

    def get_current_coordinate_y(self) -> int:
        """
        Returns the current y-coordinate of the main rectangle.

        Returns
        -------
        y: int
            The current y-coordinate.
        """
        return self.main_rect.topleft[1]

    def get_origin_coordinate_x(self) -> int:
        """
        Returns the origin x-coordinate of the animation.

        Returns
        -------
        x: int
            The origin x-coordinate.
        """
        return self.origin_coordinate[0]

    def get_origin_coordinate_y(self) -> int:
        """
        Returns the origin y-coordinate of the animation.

        Returns
        -------
        y: int
            The origin y-coordinate.
        """
        return self.origin_coordinate[1]

    def __calculate_step_size(self, coordinate: tuple[int, int]) -> tuple[int, int]:
        step_size_in_x = coordinate[0] - self.main_rect.x
        step_size_in_y = coordinate[1] - self.main_rect.y

        return step_size_in_x, step_size_in_y

    def __move_secondary_rectangles(self, step_size_in_x: int, step_size_in_y: int) -> None:
        if self.secondary_rectangles:
            for rect in self.secondary_rectangles:
                rect.x = rect.x + step_size_in_x
                rect.y = rect.y + step_size_in_y
