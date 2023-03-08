import pygame.draw
from pygame import Rect, Surface
from pygame.rect import RectType

from snakegame.animation.click import Click
from snakegame.enuns.button_option import ButtonOption
from snakegame import constants
from snakegame import validation
from snakegame.text.text import Text


class Button:
    """
    A class for creating and drawing a button on the window.

    Attributes
    ----------
    option : ButtonOption
        The option that the button represents.
    size : int
        The size of the button.
    main_color : tuple[int, int, int]
        The RGB color of the button.
    secondary_color : tuple[int, int, int]
        The secondary RGB color of the button.
    accent_color : tuple[int, int, int]
        The RGB color of the button's accent.
    coordinate : tuple[int, int]
        The coordinate of the top-left corner of the button.
    text : Text
        The text that will be displayed on the button.
    top_shape : Rect | RectType
        The top shape of the button.
    bottom_shape : Rect | RectType
        The bottom shape of the button.
    border_shape : Rect | RectType
        The border shape of the button.
    click_animation: Click
        The animation that simulates the button click.
    """

    TEXT_SIZE_PERCENTAGE = 0.5
    BORDER_RADIUS_PERCENTAGE = 0.2
    BOTTOM_BACKGROUND_DISTANCE_PERCENTAGE = 0.1
    EDGE_THICKNESS_PERCENTAGE = 0.09
    WIDTH_FACTOR = 0.5

    def __init__(
            self,
            option: ButtonOption,
            size: int,
            main_color: tuple[int, int, int]=constants.DARK_GREEN,
            secondary_color: tuple[int, int, int]=constants.GREEN_2,
            accent_color: tuple[int, int, int]=constants.LIGHT_GREEN_2,
            font_path: str=constants.FONT,
            coordinate: tuple[int, int]=(0, 0)
    ):
        """
        Initializes the Button class.

        Parameters
        ----------
        option : ButtonOption
            The option that the button represents.
        size : int
            The size of the button.
        main_color : tuple[int, int, int], optional
            The RGB color of the button (default is constants.DARK_GREEN).
        secondary_color : tuple[int, int, int], optional
            The secondary RGB color of the button (default is constants.GREEN_2).
        accent_color : tuple[int, int, int], optional
            The RGB color of the button's accent (default is constants.LIGHT_GREEN_2).
        font_path : str, optional
            The path of the font used in the button's text (default is constants.FONT).
        coordinate : tuple[int, int], optional
            The coordinate of the top-left corner of the button (default is (0, 0)).

        Raises
        ------
        ValueError
            If 'size' is less than 1 or
            if the colors are not in the RGB range (0-255, 0-255, 0-255).
        FileNotFoundError
            If the 'font_path' is not found.
        """
        self.__option = option
        self.__size = validation.is_positive(size, "'size' cannot be less than 1!")
        self.__main_color = validation.is_valid_rgb(main_color, "'main_color' out of RGB range!")
        self.__secondary_color = validation.is_valid_rgb(secondary_color, "'secondary_color' out of RGB range!")
        self.__accent_color = validation.is_valid_rgb(accent_color, "'accent_color' out of RGB range!")
        self.__current_accent_color = self.__secondary_color
        self.__coordinate = coordinate
        self.__text = self.__configure_text(font_path)
        self.__top_shape = self.__configure_top_background()
        self.__bottom_shape = self.__top_shape.copy()
        self.__border_shape = self.__top_shape.copy()
        self.__align_elements()
        self.__click_animation = self.__configure_animation()

    def get_size(self) -> int:
        """
        Returns the size of the button.

        Returns
        -------
        size : int
            The size of the button.
        """
        return self.__size

    def set_size(self, size: int) -> None:
        """
        Set the size of the button.

        Parameters
        ----------
        size : int
            The new size of the button.

        Raises
        ------
        ValueError
            If the given size is less than 1.
        """
        self.__size = validation.is_positive(size, "'size' cannot be less than 1!")
        self.__reload_button()

    def set_coordinate(self, coordinate: tuple[int, int]) -> None:
        """
        Set the (x, y) coordinate of the top-left corner of the button.

        Parameters
        ----------
        coordinate : Tuple[int, int]
            The new (x, y) coordinate.
        """
        self.__coordinate = coordinate
        self.__reload_button()

    def draw(self, window: Surface) -> None:
        """
        Draw the button in the window.

        Parameters
        ----------
        window : Surface
            The window where the button will be drawn.
        """
        border_radius = int(self.__size * Button.BORDER_RADIUS_PERCENTAGE)
        edge_thickness = int(self.__size * Button.EDGE_THICKNESS_PERCENTAGE)

        self.__draw_shape(self.__bottom_shape, window, border_radius, self.__main_color)
        self.__draw_shape(self.__top_shape, window, border_radius, self.__main_color)
        self.__draw_shape(self.__border_shape, window, border_radius,
                          self.__current_accent_color, edge_thickness)
        self.__draw_text(window)

    def events(self, selector_center_y: int, is_clicking: bool) -> ButtonOption:
        """
        Determines the events that occur when a user interacts with the button.

        Parameters
        ----------
        selector_center_y : int
            The y-coordinate of the center of the cursor or selector.
        is_clicking : bool
            True if the cursor or selector is clicking on the button.

        Returns
        -------
        option : ButtonOption
            The option that the button represents when it is clicked,
            or the ButtonOption.NONE option otherwise.
        """
        result = self.__selector_over_button(selector_center_y)
        self.__enable_accent_color(result)
        return self.__manage_click(result, is_clicking)

    def set_size_keeping_center_coordinate(self, size) -> None:
        """
        Changes the size of the button, keeping the center coordinate unchanged.

        Parameters
        ----------
        size : int
            The new button size.
        """
        current_center = self.__top_shape.center
        self.set_size(size)
        self.set_center(current_center)

    def get_center(self) -> tuple[int, int]:
        """
        Returns the center coordinate of the button.

        Returns
        -------
        center : tuple[int, int]
            The center coordinate.
        """
        return self.__top_shape.center

    def set_center(self, center: tuple[int, int]) -> None:
        """
        Changes the center coordinate of the button.

        Parameters
        ----------
        center : tuple[int, int]
            The new coordinate of the button center.
        """
        self.__top_shape.center = center
        self.set_coordinate((self.__top_shape.x, self.__top_shape.y))

    def get_bottom_shape_middle_left(self) -> tuple[int, int]:
        """
        Returns the center coordinates of the left edge of the bottom shape

        Returns
        -------
        midleft : tuple[int, int]
            The midleft-coordinate.
        """
        return self.bottom_shape.midleft

    def __enable_accent_color(self, wish: bool) -> None:
        if wish:
            self.__current_accent_color = self.__accent_color
        else:
            self.__current_accent_color = self.__secondary_color

    def __selector_over_button(self, y: int) -> bool:
        return  self.__top_shape.topleft[1] < y < self.__top_shape.bottomleft[1]

    @staticmethod
    def __draw_shape(
            background: Rect | RectType,
            window: Surface,
            border_radius: int,
            color: tuple[int, int, int],
            edge_thickness: int=0
    ) -> None:
        pygame.draw.rect(window, color, background, edge_thickness, border_radius)

    def __draw_text(self, window: Surface) -> None:
        self.__text.set_color(self.__current_accent_color)
        self.__text.draw(window)

    def __configure_top_background(self) -> Rect | RectType:
        width = self.__text.get_width() + self.__size*Button.WIDTH_FACTOR
        height = self.__size

        return Rect(self.__coordinate, (width, height))


    def __configure_text(self, font_path: str) -> Text:
        size = int(self.__size * Button.TEXT_SIZE_PERCENTAGE)

        return Text(self.__option.name, size, self.__secondary_color, font_path)

    def __configure_animation(self) -> Click:
        return Click(
            self.__top_shape,
            self.__bottom_shape,
            [self.__border_shape, self.__text.get_rect()],
        )

    def __reload_button(self) -> None:
        self.__reload_text()
        self.__reload_shapes()
        self.__align_elements()
        self.__reload_animation()

    def __reload_shapes(self) -> None:
        self.__top_shape = self.__configure_top_background()
        self.__bottom_shape = self.__top_shape.copy()
        self.__border_shape = self.__top_shape.copy()

    def __reload_text(self) -> None:
        self.__text = self.__configure_text(self.__text.get_font_path())

    def __reload_animation(self) -> None:
        self.__click_animation.reload_click(
            self.__top_shape,
            self.__bottom_shape,
            [self.__border_shape, self.__text.get_rect()],
        )

    def __align_elements(self) -> None:
        self.__bottom_shape.center = self.__top_shape.center
        self.__bottom_shape.move_ip(0, self.__size * Button.BOTTOM_BACKGROUND_DISTANCE_PERCENTAGE)
        self.__border_shape.center = self.__top_shape.center
        self.__text.set_center(self.__top_shape.center)

    def __manage_click(self, selector_over_button: bool, is_clicking: bool) -> ButtonOption:
        self.__click_animation.animate((selector_over_button, is_clicking))

        if self.__click_animation.click_done():
            return self.__option
        else:
            return ButtonOption.NONE
