import pygame
from pygame import display, Surface, SurfaceType

from snakegame import validation


def get_system_display_dimensions() -> tuple[int, int]:
    """
    Returns system screen dimensions in pixels.

    Returns
    -------
    dimensions : tuple[int, int]
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
    event : int
        The event id.
    milliseconds: int
        The time interval of the event.

    Returns
    -------
    event : int
        The event id.
    """
    pygame.time.set_timer(event, milliseconds)

    return event


def load_images(image_paths: list[str], dimensions: tuple[int, int]) -> list | list[Surface | SurfaceType]:
    """
    Load a list of images. An empty list is returned if no path exists.

    Parameters
    ----------
    image_paths : list[str]
        The paths of the images.
    dimensions : tuple[int, int]
        The width and height dimensions.

    Returns
    -------
    list | list[Surface | SurfaceType]
        The list.

    Raises
    ------
    ValueError
        If 'dimensions' are not positive values.
    FileNotFoundError
        If any image path is not found.
    """
    images = []
    if image_paths:
        for image_path in image_paths:
            image = load_image(image_path, dimensions)
            images.append(image)

    return images


def load_image(image_path: str, dimensions: tuple[int, int]=(-1, -1)) -> Surface:
    """
    Load an image. If the dimensions are not informed, the image is loaded in the original size.

    Parameters
    ----------
    image_path : str
        The path of the image.
    dimensions : tuple[int, int], optional
        The width and height dimensions (default is (-1, -1)).

    Returns
    -------
    Surface
        The image.

    Raises
    ------
    ValueError
        If 'dimensions' are not positive values.
    FileNotFoundError
        If the 'image_path' is not found.
    """
    validation.is_valid_path(image_path, "'image path' not found!")
    image = pygame.image.load(image_path)

    if dimensions != (-1, -1):
        validation.is_valid_dimensions(dimensions, "All 'dimensions' must be greater than zero!")
        image = pygame.transform.scale(image, dimensions)

    return image
