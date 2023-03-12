import pygame
from pygame import display

from snakegame import validation


def get_system_display_dimensions() -> tuple[int, int]:
    """
    Returns system screen dimensions in pixels.

    Returns
    -------
    dimensions: tuple[int, int]
        Screen width and height.
    """
    display.init()
    screen_info = display.Info()
    return screen_info.current_w, screen_info.current_h


def configure_event(event: int, milliseconds: int) -> int:
    """
    Configure a pygame event.

    Parameters
    ----------
    event: int
        The event id.
    milliseconds: int
        The time interval of the event.

    Returns
    -------
    event: int
        The event id.
    """
    pygame.time.set_timer(event, milliseconds)

    return event
