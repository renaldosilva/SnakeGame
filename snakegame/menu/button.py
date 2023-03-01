import pygame.draw
from pygame import Rect, Surface
from pygame.rect import RectType

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
        The color of the button.
    secondary_color : tuple[int, int, int]
        The secondary color of the button.
    accent_color : tuple[int, int, int]
        The color of the button's accent.
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

    Methods
    -------
    draw(window: Surface) -> None:
        Draws the button on the window.
    events(selector_center_y: int, is_clicking: bool) -> ButtonOption:
        Manages the events of the button.
    set_size_keeping_center_coordinate(size: int) -> None:
        Changes the size of the button, keeping the center of the button.
    set_y(y: int) -> None:
        Changes the y coordinate of the top-left corner of the button.
    set_center(center: tuple[int, int]) -> None:
        Changes the center of the button.
    set_center_x(x: int) -> None:
        Changes the x coordinate of the center of the button.
    get_center() -> tuple[int, int]:
        Returns the center coordinate of the button.
    get_center_y() -> int:
        Returns the y coordinate of the center of the button.
    get_bottom_shape_middle_left(self) -> tuple[int, int]:
        Returns the left center coordinate of the bottom shape.
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
            The color of the button (default is constants.DARK_GREEN).
        secondary_color : tuple[int, int, int], optional
            The secondary color of the button (default is constants.GREEN_2).
        accent_color : tuple[int, int, int], optional
            The color of the button's accent (default is constants.LIGHT_GREEN_2).
        font_path : str, optional
            The path of the font used in the button's text (default is constants.FONT).
        coordinate : tuple[int, int], optional
            The coordinate of the top-left corner of the button (default is (0, 0)).
        text : Text
            The text that will be displayed on the button.
        top_shape : Rect | RectType
            The top shape of the button.
        bottom_shape : Rect | RectType
            The bottom shape of the button.
        border_shape : Rect | RectType
            The border shape of the button.
        """
        self.__option = option
        self.__size = size
        self.__main_color = main_color
        self.__secondary_color = secondary_color
        self.__accent_color = accent_color
        self.__current_accent_color = self.secondary_color
        self.__coordinate = coordinate
        self.__text = self.__configure_text(font_path)
        self.__top_shape = self.__configure_top_background()
        self.__bottom_shape = self.top_shape.copy()
        self.__border_shape = self.top_shape.copy()
        self.__align_elements()

    @property
    def option(self) -> ButtonOption:
        """
        Returns the option that the button represents.

        Returns
        -------
        option: ButtonOption
            The option.
        """
        return self.__option

    @property
    def size(self) -> int:
        """
        Returns the size of the button.

        Returns
        -------
        size: int
            The size of the button.
        """
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
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
        if size < 1:
            raise ValueError("Button size must be greater than or equal to 1!")
        else:
            self.__size = size
            self.__reload_button()

    @property
    def main_color(self) -> tuple[int, int, int]:
        """
        Returns the main color of the button.

        Returns
        -------
        main_color: tuple[int, int, int]
            A tuple representing the RGB values of the main color.
        """
        return self.__main_color

    @main_color.setter
    def main_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the main color of the button.

        Parameters
        ----------
        color : tuple[int, int, int]
            A tuple representing the RGB values of the new main color.

        Raises
        ------
        ValueError
            If any of the RGB values in the tuple are outside the valid range (0, 255).
        """
        if validation.is_invalid_rgb(color):
            raise ValueError("Main color: the R, G and B channels must be in range (0, 255)!")
        else:
            self.__main_color = color

    @property
    def secondary_color(self) -> tuple[int, int, int]:
        """
        Returns the secondary color of the button.

        Returns
        -------
        secondary_color: tuple[int, int, int]
            A tuple representing the RGB values of the secondary color.
        """
        return self.__secondary_color

    @secondary_color.setter
    def secondary_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the secondary color of the button.

        Parameters
        ----------
        color : tuple[int, int, int]
            A tuple representing the RGB values of the new secondary color.

        Raises
        ------
        ValueError
            If any of the RGB values in the tuple are outside the valid range (0, 255).
        """
        if validation.is_invalid_rgb(color):
            raise ValueError("Secondary color: the R, G and B channels must be in range (0, 255)!")
        else:
            self.__secondary_color = color

    @property
    def accent_color(self) -> tuple[int, int, int]:
        """
        Returns the accent color of the button.

        Returns
        -------
        accent_color: tuple[int, int, int]
            A tuple representing the RGB values of the accent color.
        """
        return self.__accent_color

    @accent_color.setter
    def accent_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the accent color of the button.

        Parameters
        ----------
        color : tuple[int, int, int]
            A tuple representing the RGB values of the new accent color.

        Raises
        ------
        ValueError
            If any of the RGB values in the tuple are outside the valid range (0, 255).
        """
        if validation.is_invalid_rgb(color):
            raise ValueError("Accent color: the R, G and B channels must be in range (0, 255)!")
        else:
            self.__accent_color = color

    @property
    def coordinate(self) -> tuple[int, int]:
        """
        Returns the (x, y) coordinate of the top-left corner of the button.

        Returns
        -------
        coordinate: Tuple[int, int]
            The (x, y) coordinate.
        """
        return self.__coordinate

    @coordinate.setter
    def coordinate(self, coordinate: tuple[int, int]) -> None:
        """
        Set the (x, y) coordinate of the top-left corner of the button.

        Parameters
        ----------
        coordinate : Tuple[int, int]
            The new (x, y) coordinate.

        Raises
        ------
        ValueError
            If the coordinate is invalid and goes beyond the limits of the window.
        """
        if validation.is_invalid_coordinate(coordinate):
            raise ValueError("The coordinate of the top-left cannot go beyond the limits of the window.")
        else:
            self.__coordinate = coordinate
            self.__reload_button()

    @property
    def text(self) -> Text:
        """
        Returns the text that is displayed on the button.

        Returns
        -------
        text: Text
            The button text.
        """
        return self.__text

    @property
    def top_shape(self) -> Rect | RectType:
        """
        Returns the top shape of the button.

        Returns
        -------
        top_shape: Rect | RectType
            The top shape.
        """
        return self.__top_shape

    @property
    def bottom_shape(self) -> Rect | RectType:
        """
        Returns the bottom shape of the button.

        Returns
        -------
        bottom_shape: Rect | RectType
            The bottom shape.
        """
        return self.__bottom_shape

    @property
    def border_shape(self) -> Rect | RectType:
        """
        Returns the border shape of the button.

        Returns
        -------
        border_shape: Rect | RectType
            The border shape.
        """
        return self.__border_shape

    def draw(self, window: Surface) -> None:
        """
        Draw the button in the window.

        Parameters
        ----------
        window: Surface
            The window where the button will be drawn.
        """
        border_radius = int(self.size * Button.BORDER_RADIUS_PERCENTAGE)
        edge_thickness = int(self.size * Button.EDGE_THICKNESS_PERCENTAGE)

        self.__draw_shape(self.bottom_shape, window, border_radius, self.main_color)
        self.__draw_shape(self.top_shape, window, border_radius, self.main_color)
        self.__draw_shape(self.border_shape, window, border_radius,
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
        option: ButtonOption
            The option that the button represents when it is clicked,
            or the ButtonOption.NONE option otherwise.
        """
        result = self.__is_next_to_the_button(selector_center_y)
        self.__enable_accent_color(result)
        return self.__manage_click(result, is_clicking)

    def set_size_keeping_center_coordinate(self, size) -> None:
        """
        Changes the size of the button, keeping the center coordinate unchanged.

        Parameters
        ----------
        size: int
            The new button size.
        """
        current_center = self.top_shape.center
        self.size = size
        self.set_center(current_center)

    def set_y(self, y: int) -> None:
        """
        Changes the y-coordinate of the top left corner of the button.

        Parameters
        ----------
        y: int
            The new y-coordinate.
        """
        self.coordinate = self.coordinate[0], y

    def set_center(self, center: tuple[int, int]) -> None:
        """
        Changes the center coordinate of the button.

        Parameters
        ----------
        center: tuple[int, int]
            The new coordinate of the button center.
        """
        self.top_shape.center = center
        self.coordinate = self.top_shape.x, self.top_shape.y
        self.__reload_button()

    def set_center_x(self, x: int) -> None:
        """
        Changes the x-coordinate of the center of the button.

        Parameters
        ----------
        x: int
            The new x-coordinate of the center
        """
        self.set_center((x, self.top_shape.center[1]))

    def get_center(self) -> tuple[int, int]:
        """
        Returns the center coordinate of the button.

        Returns
        -------
        center: tuple[int, int]
            The center coordinate.
        """
        return self.top_shape.center

    def get_center_y(self) -> int:
        """
        Returns the y-coordinate of the center of the button.

        Returns
        -------
        y: int
            The y-coordinate of the center.
        """
        return self.top_shape.center[1]

    def get_bottom_shape_middle_left(self) -> tuple[int, int]:
        """
        Returns the center coordinates of the left edge of the bottom shape

        Returns
        -------
        midleft: tuple[int, int]
            The midleft-coordinate.
        """
        return self.bottom_shape.midleft

    def __enable_accent_color(self, wish: bool) -> None:
        if wish:
            self.__current_accent_color = self.accent_color
        else:
            self.__current_accent_color = self.secondary_color

    def __is_next_to_the_button(self, y: int) -> bool:
        return  self.top_shape.topleft[1] < y < self.top_shape.bottomleft[1]

    @staticmethod
    def __draw_shape(
            background: Rect | RectType,
            window: Surface,
            border_radius: int,
            color: tuple[int, int, int],
            edge_thickness: int=0
    ) -> None:
        pygame.draw.rect(
            window,
            color,
            background,
            edge_thickness,
            border_radius,
        )

    def __draw_text(self, window: Surface) -> None:
        self.text.color = self.__current_accent_color
        self.text.draw(window)

    def __configure_top_background(self) -> Rect | RectType:
        width = self.text.get_width() + self.size*Button.WIDTH_FACTOR
        height = self.size

        return Rect(self.coordinate, (width, height))


    def __configure_text(self, font_path: str) -> Text:
        size = int(self.size * Button.TEXT_SIZE_PERCENTAGE)

        return Text(self.option.name, size, self.secondary_color, font_path)

    def __reload_button(self) -> None:
        self.__reload_text()
        self.__reload_shapes()
        self.__align_elements()

    def __reload_shapes(self) -> None:
        self.__top_shape = self.__configure_top_background()
        self.__bottom_shape = self.top_shape.copy()
        self.__border_shape = self.top_shape.copy()

    def __reload_text(self) -> None:
        self.__text = self.__configure_text(self.text.font_path)

    def __align_elements(self) -> None:
        self.bottom_shape.center = self.top_shape.center
        self.bottom_shape.move_ip(0, self.size * Button.BOTTOM_BACKGROUND_DISTANCE_PERCENTAGE)
        self.border_shape.center = self.top_shape.center
        self.text.set_center(self.top_shape.center)

    def __manage_click(self, is_on_the_button: bool, is_clicking: bool) -> ButtonOption:
        if is_on_the_button and is_clicking:
            return self.option
        else:
            return ButtonOption.NONE
