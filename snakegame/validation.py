import os


def is_empty(value: str, error_message: str) -> str:
    """
    Checks if the value is empty.

    Parameters
    ----------
    value : str
        The value to be checked.
    error_message : str
        The error message that will be displayed.

    Returns
    -------
    value : str
        If the value is not empty.

    Raises
    ------
    ValueError
        If the value is empty.
    """
    if value == "":
        raise ValueError(error_message)

    return value


def is_positive(value: int, error_message: str) -> int:
    """
    Checks if the value is positive.

    Parameters
    ----------
    value : int
        The value to be checked.
    error_message : str
        The error message that will be displayed.

    Returns
    -------
    value : int
        If the value is positive.

    Raises
    ------
    ValueError
        If the value is not positive.
    """
    if value < 1:
        raise ValueError(error_message)

    return value


def is_valid_rgb(color: tuple[int, int, int], error_message: str) -> tuple[int, int, int]:
    """
    Checks if a rgb color is valid.

    Parameters
    ----------
    color : tuple[int, int, int]
        The RGB color.
    error_message : str
        The error message that will be displayed.

    Returns
    -------
    color : tuple[int, int, int]
        If the color is valid.

    Raises
    ------
    ValueError
        If the color is invalid.
    """
    for channel in color:
        if channel<0 or 255<channel:
            raise ValueError(error_message)

    return color


def is_valid_path(path: str, error_message: str) -> str:
    """
    Check if the path exists.

    Parameters
    ----------
    path : str
        The path.
    error_message : str
        The error message that will be displayed.

    Returns
    -------
    path : str
        If the path exists.

    Raises
    ------
    FileNotFoundError
        If the path does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(error_message)

    return path

def check_paths(font_paths: list[str], error_message: str) -> list[str]:
    """
    Check a list of paths.

    Parameters
    ----------
    font_paths : list[str]
        The path list.
    error_message : str
        The error message that will be displayed.

    Returns
    -------
    font_paths : list[str]
        The path list.

    Raises
    ------
    FileNotFoundError
        If the path does not exist.
    ValueError
        If the path list is empty.
    """
    if font_paths:
        for font_path in font_paths:
            is_valid_path(font_path, "'font_path' not found!")
    else:
        raise ValueError(error_message)

    return font_paths
