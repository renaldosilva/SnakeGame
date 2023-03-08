from enum import Enum


class Direction(Enum):
    """
    An enumeration of directions.

    Attributes
    ----------
    LEFT : tuple of int
        The left direction. (-1, 0)
    RIGHT : tuple of int
        The right direction. (1, 0)
    UP : tuple of int
        The up direction. (0, -1)
    DOWN : tuple of int
        The down direction. (0, 1)

    Notes
    -----
    Each direction is represented as a tuple of two integers, where the first
    integer represents the horizontal component and the second integer represents
    the vertical component.
    """

    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
