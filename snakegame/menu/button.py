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
    __option : ButtonOption
        The option that the button represents.
    __size : int
        The size of the button.
    __main_color : tuple[int, int, int]
        The main RGB color of the button.
    __secondary_color : tuple[int, int, int]
        The secondary RGB color of the button.
    __accent_color : tuple[int, int, int]
        the accent RGB color of the button.
    __coordinate : tuple[int, int]
        The coordinate of the top-left corner of the button.
    __text : Text
        The text that will be displayed on the button.
    __top_shape : Rect | RectType
        The top shape of the button.
    __bottom_shape : Rect | RectType
        The bottom shape of the button.
    __border_shape : Rect | RectType
        The border shape of the button.
    __click_animation : Click
        The animation that simulates the button click.
    __border_radius : int
        The radius of the button.
    __edge_thickness : int
        The thickness of the button border.
    """

    TEXT_SIZE_PERCENTAGE = 0.5
    """The percentage of the button text size.
    """

    BORDER_RADIUS_PERCENTAGE = 0.2
    """The radius percentage of the button borders.
    """

    BOTTOM_BACKGROUND_DISTANCE_PERCENTAGE = 0.1
    """The percentage of distance from the bottom to the top of the button.
    """

    EDGE_THICKNESS_PERCENTAGE = 0.09
    """The percentage of the button's border thickness.
    """

    WIDTH_FACTOR = 0.5
    """The button width factor.
    """

    def __init__(
            self,
            option: ButtonOption,
            size: int=constants.BUTTON_SIZE,
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
        size : int, optional
            The size of the button (default is constants.BUTTON_SIZE).
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
        self.__align_elements()
        self.__click_animation = self.__configure_animation()
        self.__border_radius = int(self.__size * Button.BORDER_RADIUS_PERCENTAGE)
        self.__edge_thickness = int(self.__size * Button.EDGE_THICKNESS_PERCENTAGE)

    def get_option(self) -> ButtonOption:
        """
        Returns button option.

        Returns
        -------
        option : ButtonOption
            The button option.
        """
        return self.__option

    def get_height(self) -> int:
        """
        Returns the height of the button.

        Returns
        -------
        int
            The height of the button.
        """
        return self.__bottom_shape.bottomleft[1] - self.__top_shape.topleft[1]

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
        pygame.draw.rect(
            window, self.__main_color, self.__bottom_shape,
            border_radius=self.__border_radius
        )
        pygame.draw.rect(
            window, self.__main_color, self.__top_shape,
            border_radius=self.__border_radius
        )
        pygame.draw.rect(
            window, self.__current_accent_color, self.__top_shape,
            self.__edge_thickness, self.__border_radius
        )

        self.__draw_text(window)

    def events(self, selector_coordinate: tuple[int, int], is_clicking: bool) -> ButtonOption:
        """
        Determines the events that occur when a user interacts with the button.

        Parameters
        ----------
        selector_coordinate : int
            The coordinate of the cursor or selector.
        is_clicking : bool
            True if the cursor or selector is clicking on the button.

        Returns
        -------
        option : ButtonOption
            The option that the button represents when it is clicked,
            or the ButtonOption.NONE option otherwise.
        """
        result = self.the_selector_is_next_to_the_button(selector_coordinate[1])
        self.__enable_accent_color(result)
        return self.__manage_click(result, is_clicking)

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

    def set_top_shape_midtop(self, midtop: tuple[int, int]) -> None:
        """
        Changes the center coordinate of the top edge of the top shape.

        Parameters
        ----------
        midtop : tuple[int, int]
            The new top coordinate of the button.
        """
        self.__top_shape.midtop = midtop
        self.set_coordinate((self.__top_shape.x, self.__top_shape.y))

    def get_bottom_shape_midleft(self) -> tuple[int, int]:
        """
        Returns the center coordinates of the left edge of the bottom shape

        Returns
        -------
        tuple[int, int]
            The midleft-coordinate.
        """
        return self.__bottom_shape.midleft

    def get_bottom_shape_midbottom(self):
        """
        Returns the center coordinates of the bottom edge of the bottom shape

        Returns
        -------
        tuple[int, int]
            The midbottom-coordinate.
        """
        return self.__bottom_shape.midbottom

    def the_selector_is_next_to_the_button(self, selector_coordinate_y: int) -> bool:
        """
        Checks if the selector is at the same y-coordinate as the button.

        Parameters
        ----------
        selector_coordinate_y : int
            The y-coordinate of the selector

        Returns
        -------
        bool
            True if the selector is at the same y-coordinate as the button, False otherwise.
        """
        return self.__top_shape.topleft[1]<selector_coordinate_y< self.__top_shape.bottomleft[1]

    def __enable_accent_color(self, wish: bool) -> None:
        if wish:
            self.__current_accent_color = self.__accent_color
        else:
            self.__current_accent_color = self.__secondary_color

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
            [self.__text.get_rect()]
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
            [self.__text.get_rect()]
        )

    def __align_elements(self) -> None:
        self.__bottom_shape.center = self.__top_shape.center
        self.__bottom_shape.move_ip(0, self.__size * Button.BOTTOM_BACKGROUND_DISTANCE_PERCENTAGE)
        self.__text.set_center(self.__top_shape.center)

    def __manage_click(self, selector_over_button: bool, is_clicking: bool) -> ButtonOption:
        self.__click_animation.animate((selector_over_button, is_clicking))

        if self.__click_animation.click_done():
            return self.__option
        else:
            return ButtonOption.NONE
