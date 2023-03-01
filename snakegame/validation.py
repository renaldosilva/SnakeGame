import os

from snakegame import constants


def is_invalid_rgb(color: tuple[int, int, int]) -> bool:
    """
    Checks if an rgb color is invalid.

    Parameters
    ----------
    color: tuple[int, int, int]
        The RGB color.

    Returns
    -------
    is_valid: bool
        True if the RGB values in the tuple are not in the range (0, 255), False otherwise.
    """
    is_valid = True
    for channel in color:
        if channel<0 or channel>255:
            is_valid = False

    return is_valid


def is_invalid_path(path: str) -> bool:
    """
    Checks if a path does not exist.

    Parameters
    ----------
    path: str
        The path.

    Returns
    -------
    non_existent_path: bool
        True if the path does not exist, False otherwise.
    """
    non_existent_path = not os.path.exists(path)

    return non_existent_path


def is_invalid_coordinate(coordinate: tuple[int, int]) -> bool:
    """
    Check if the provided coordinate is invalid, i.e. outside the window bounds.

    Parameters
    ----------
    coordinate : tuple[int, int]
        A tuple representing the (x, y) coordinate.

    Returns
    -------
    is_invalid: bool
        Returns True if the coordinate is invalid, False otherwise.
    """
    x = coordinate[0]
    y = coordinate[1]
    is_invalid = True

    if 0<=x<=constants.SYSTEM_DISPLAY_WIDTH or 0<=y<=constants.SYSTEM_DISPLAY_HEIGHT:
        is_invalid = False

    return is_invalid
