from pygame import display


def get_system_display_dimensions() -> tuple[int, int]:
    """
    Get system screen dimensions in pixels.

    Returns
    -------
    dimensions: tuple[int, int]
        Screen width and height.
    """
    display.init()
    screen_info = display.Info()
    return screen_info.current_w, screen_info.current_h
