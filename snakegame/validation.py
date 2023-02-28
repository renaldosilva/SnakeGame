def is_smaller_than(value: int, reference: int) -> bool:
    """
    Compare two values.

    Returns
    -------
    is_smaller: bool
        True if the value is greater than the reference value, False otherwise.
    """
    is_smaller = value < reference

    return is_smaller


def is_invalid_rgb(color: tuple[int, int, int]) -> bool:
    """
    Checks if an rgb color is invalid.

    Returns
    -------
    is_valid: bool
        True if the RGB values in the tuple are not in the range (0, 255), False otherwise.
    """
    is_valid = True
    for channel in color:
        if channel < 0 or channel > 255:
            is_valid = False

    return is_valid
