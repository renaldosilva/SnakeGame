from abc import ABC, abstractmethod

import pygame
from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper

from snakegame.enuns.button_option import ButtonOption
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.simple_background import SimpleBackground
from snakegame.text.animated_text import AnimatedText


class Menu(ABC):
    """
    Abstract representation of a menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __background : SimpleBackground
        The background of the menu.
    __selector : AnimatedText
        The selector used to move around in the menu.
    __buttons : list[Button]
        The menu buttons.
    __current_button : int
        The index of the current button where the selector is on.
    __selected_option : ButtonOption
        The current menu option.
    __is_running : bool
        Indicates whether the menu is running.
    """

    KEYS = {
        "select": pygame.K_RETURN,
        "up": pygame.K_UP,
        "down": pygame.K_DOWN
    }
    """The menu control keys.
    """

    SELECTOR_SYMBOL = "->"
    """The menu selector symbol.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            background: SimpleBackground,
    ):
        """
        Initialize the menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        background : SimpleBackground
            The background of the menu.
        """
        self.__basic_piece = basic_piece
        self.__background = background
        self.__selector = AnimatedText(Menu.SELECTOR_SYMBOL)
        self.__buttons = self.__configure_buttons()
        self.__current_button = 0
        self.__selected_option = ButtonOption.NONE
        self.__is_running = True

    def start(self) -> None:
        """Start the menu."""
        self.__loop()

    def __loop(self) -> None:
        while self.__is_running:
            if self.__selected_option == ButtonOption.NONE:
                self.__run_this()
            else:
                self.run_another_action(self.__selected_option)
            self.__basic_piece.clock_tick()
        self.__reset_state()

    @abstractmethod
    def run_another_action(self, selected_option: ButtonOption) -> None:
        """
        Manages changes in the menu screen.

        Parameters
        ----------
        selected_option : ButtonOption
            The option selected from the menu.
        """
        pass

    def back_to_main_menu(self) -> None:
        """Returns to the main menu screen."""
        self.__selected_option = ButtonOption.NONE

    def get_window_height(self) -> int:
        """
        Returns the height of the window.

        Returns
        -------
        int
            The width of the window.
        """
        return self.__basic_piece.get_window_height()

    def get_game_pixel_dimension(self) -> int:
        """
        returns the pixel dimension used in the game.

        Returns
        -------
        int
            The pixel dimension.
        """
        return self.__basic_piece.get_game_pixel_dimension()

    def __run_this(self) -> None:
        self.__events()
        self.__draw()
        self.__update()

    def __events(self) -> None:
        for event in self.__basic_piece.get_events():
            self.__check_close_all(event)
            self.__current_button_event(event)
            self.__background.events(event)
            self.__selector.animate(event)

        self.__selected_option = self.__button_events()

    def __draw(self) -> None:
        self.__background.draw(self.__basic_piece.get_window())
        self.__draw_buttons()
        self.__selector.draw(self.__basic_piece.get_window())
        self.other_drawings(self.__basic_piece.get_window())

    def __update(self) -> None:
        self.__basic_piece.update_window()
        self.__update_selector_position()

    def __configure_buttons(self) -> list[Button]:
        buttons = self.create_buttons()
        buttons = self.align_buttons(buttons)

        return buttons

    @abstractmethod
    def create_buttons(self) -> list[Button]:
        """
        Create menu buttons.

        Returns
        -------
        buttons : list[Button]
            A list of buttons.
        """
        pass

    @abstractmethod
    def align_buttons(self, buttons: list[Button]) -> list[Button]:
        """
        Arrange the buttons on the menu.

        Parameters
        ----------
        buttons : list[Button]
            A list of buttons.

        Returns
        -------
        buttons : list[Button]
            The list of buttons lined up.
        """
        pass

    @abstractmethod
    def other_drawings(self, window: Surface) -> None:
        """
        Manage other drawings in the menu.

        Parameters
        ----------
        window : Surface
            The window where other things can be drawn.
        """
        pass

    def __button_events(self) -> ButtonOption:
        pressed_select = pygame.key.get_pressed()[Menu.KEYS["select"]]
        selector_coordinate = self.__selector.get_center()
        option = ButtonOption.NONE
        index = 0

        while option==ButtonOption.NONE and index<len(self.__buttons):
            button = self.__buttons[index]
            option = button.events(selector_coordinate, pressed_select)
            index += 1

        return option

    def __update_selector_position(self) -> None:
        button = self.__buttons[self.__current_button]

        if not button.selector_next_to_the_button(self.__selector.get_center()):
            center = self.__calculate_selector_center(button)
            self.__selector.set_center(center)

    def __calculate_selector_center(self, current_button: Button) -> tuple[int, int]:
        x = current_button.get_bottom_shape_middle_left()[0] - self.__selector.get_width()
        y = current_button.get_bottom_shape_middle_left()[1]

        return x, y

    def __current_button_event(self, event: Event) -> None:
        if event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            self.__pressed_up(pressed_keys)
            self.__pressed_down(pressed_keys)

    def __pressed_up(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[Menu.KEYS["up"]]:
            if self.__current_button - 1 in range(0, len(self.__buttons)):
                self.__current_button -= 1
            else:
                self.__current_button = len(self.__buttons) - 1

    def __pressed_down(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[Menu.KEYS["down"]]:
            if self.__current_button + 1 in range(0, len(self.__buttons)):
                self.__current_button += 1
            else:
                self.__current_button = 0

    def __check_close_all(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            self.close_all()

    def close_all(self) -> None:
        """Closes the Pygame window and exits the program."""
        self.__basic_piece.close_all()

    def quit(self) -> None:
        """Close the menu."""
        self.__is_running = False

    def __reset_state(self) -> None:
        self.__current_button = 0
        self.__selected_option = ButtonOption.NONE
        self.__is_running = True

    def __draw_buttons(self) -> None:
        for button in self.__buttons:
            button.draw(self.__basic_piece.get_window())
