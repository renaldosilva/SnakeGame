from typing import Any

from pygame import Rect

from snakegame.animation.animation import Animation
from snakegame.enuns.direction import Direction


class HorizontalSwing(Animation):
    """
    A class that animates a rectangle to swing horizontally back and forth.

    Attributes
    ----------
    move_limit_size : int
        The maximum distance that the rectangle can move to each side.
    current_direction : Direction
        The current direction of the swing animation.
    """

    RANGE_OF_MOTION_PERCENTAGE = 0.05
    STEP_SIZE = 2

    def __init__(self, main_rectangle: Rect, secondary_rectangles: list[Rect]=None):
        """
        Initialize the HorizontalSwing object

        Parameters
        ----------
        main_rectangle : pygame.Rect
            The main rectangle to be animated.
        secondary_rectangles : list of pygame.Rect, optional
            A list of secondary rectangles to be animated together with the main rectangle.
        """
        super().__init__(main_rectangle, secondary_rectangles)
        self.__move_limit_size = self.__calculate_the_size_of_the_move()
        self.__current_direction = Direction.LEFT

    def animate(self, extra: tuple[Any, ...]=None) -> None:
        """
        Animate the rectangle to swing horizontally.

        Parameters
        ----------
        extra : tuple
            This animation does not use extra arguments.
        """
        origin_coordinate_x = super().get_origin_coordinate_x()
        current_coordinate_x = super().get_current_coordinate_x()

        if self.__current_direction == Direction.LEFT:
            self.__go_left(current_coordinate_x, origin_coordinate_x)
        else:
            self.__go_right(current_coordinate_x, origin_coordinate_x)

    def reload_animation(self,  main_rect: Rect, secondary_rectangles: list[Rect] = None) -> None:
        super().reload_animation(main_rect, secondary_rectangles)
        self.__move_limit_size = self.__calculate_the_size_of_the_move()

    def __go_left(self, current_coordinate_x: int, origin_coordinate_x: int) -> None:
        if current_coordinate_x > origin_coordinate_x-self.__move_limit_size:
            super().set_current_coordinate_x(current_coordinate_x - HorizontalSwing.STEP_SIZE)
        else:
            self.__current_direction = Direction.RIGHT

    def __go_right(self, current_coordinate_x: int, origin_coordinate_x: int) -> None:
        if current_coordinate_x < origin_coordinate_x + self.__move_limit_size:
            super().set_current_coordinate_x(current_coordinate_x + HorizontalSwing.STEP_SIZE)
        else:
            self.__current_direction = Direction.LEFT

    def __calculate_the_size_of_the_move(self) -> int:
        return int(super().get_main_rectangle().width * HorizontalSwing.RANGE_OF_MOTION_PERCENTAGE)
