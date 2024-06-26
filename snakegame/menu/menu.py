from abc import ABC, abstractmethod

import pygame
from pygame import Surface
from pygame.event import Event
from pygame.key import ScancodeWrapper

from snakegame import constants
from snakegame.enuns.button_option import ButtonOption
from snakegame.menu.sound_manager import SoundManager
from snakegame.game.basic_piece import BasicPiece
from snakegame.menu.button import Button
from snakegame.menu.background import Background
from snakegame.text.animated_text import AnimatedText


class Menu(ABC):
    """
    Abstract representation of a menu.

    Attributes
    ----------
    __basic_piece : BasicPiece
        The basic features of the game.
    __sound_manager : SoundManager
        The sound manager of the game.
    __background : Background
        The menu background.
    __button_alignment : {1, 2, 3}
        Represents is the alignment of the buttons:
            1 - top alignment;
            2 - center alignment;
            3 - bottom alignment.
    __selector : AnimatedText
        The selector used to move around in the menu.
    __buttons : list[Button]
        The menu buttons.
    __current_button : int
        The index of the current button where the selector is on.
    __selected_option : ButtonOption
        The current menu option.
    __last_selected_option : ButtonOption
        The last option that was selected in the menu.
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

    SELECTOR_SYMBOL = ">"
    """The menu selector symbol.
    """

    BUTTON_SPACING_PERCENTAGE = 0.1
    """The percentage of space between buttons.
    """

    BUTTONS_MARGIN_PERCENTAGE = 0.15
    """The percentage of distance the buttons are from the background.
    """

    def __init__(
            self,
            basic_piece: BasicPiece,
            sound_manager: SoundManager,
            background: Background,
            button_alignment: int=constants.TOP_ALIGNMENT
    ):
        """
        Initialize the Menu.

        Parameters
        ----------
        basic_piece : BasicPiece
            The basic features of the game.
        sound_manager : SoundManager
            The sound manager of the game.
        background : Background
            The background of the menu.
        button_alignment : {1, 2, 3}, optional
            Represents is the alignment of the buttons (default is 1):
                1 - top alignment;
                2 - center alignment;
                3 - bottom alignment.

        Raises
        ------
        ValueError
            If the 'button_alignment' value is not in the range (1-3).
        """
        self.__basic_piece = basic_piece
        self.__sound_manager = sound_manager
        self.__background = background
        self.__button_alignment = self.__check_button_alignment(button_alignment)
        self.__buttons = self.__configure_buttons()
        self.__current_button = 0
        self.__selected_option = ButtonOption.NONE
        self.__last_selected_option = ButtonOption.NONE
        self.__is_running = True
        self.__selector = AnimatedText(Menu.SELECTOR_SYMBOL)
        self.__update_selector_position()

    def start(self) -> ButtonOption:
        """
        Start the menu.

        Returns
        -------
        last_selected_option : ButtonOption
            The last option that was selected in the menu.
        """
        self.__loop()
        return self.__last_selected_option

    def __loop(self) -> None:
        while self.__is_running:
            if self.__selected_option == ButtonOption.NONE:
                self.__run_this()
            else:
                self.__last_selected_option = self.__selected_option
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

    def reset_selected_option(self) -> None:
        """Resets selected option to default value (default is ButtonOption.NONE)."""
        self.__selected_option = ButtonOption.NONE

    def get_current_button_option(self) -> ButtonOption:
        """
        Get current button option.

        Returns
        -------
        ButtonOption
            The button option.
        """
        return self.__buttons[self.__current_button].get_option()

    def set_background(self, background: Background) -> None:
        """
        Change the background.

        Parameters
        ----------
        background: Background
            The new background
        """
        last_height = self.__background.get_height()
        self.__background = background
        current_height = self.__background.get_height()

        if current_height != last_height:
            self.__buttons = self.__align_buttons(self.__buttons)

    def get_background(self) -> Background:
        """
        Returns the background of the menu.

        Returns
        -------
        background : Background
            The background.
        """
        return self.__background

    def get_basic_piece(self) -> BasicPiece:
        """
        Returns the basic piece of the game.

        Returns
        -------
        basic_piece: BasicPiece
            The basic piece.
        """
        return self.__basic_piece

    def get_sound_manager(self) -> SoundManager:
        """
        Returns the sound manager of the game.

        Returns
        -------
        sound_manager: SoundManager
            The sound manager.
        """
        return self.__sound_manager

    def __run_this(self) -> None:
        self.__events()
        self.__draw()
        self.__update()

    def __events(self) -> None:
        for event in self.__basic_piece.get_events():
            self.__basic_piece.check_quit(event)
            self.__directional_key_events(event)
            self.__background.events(event)
            self.__selector.animate(event)

        self.__selected_option = self.__button_events()
        self.other_events()

    def __draw(self) -> None:
        window = self.__basic_piece.get_window_manager().get_window()

        self.drawings_below(window)
        self.__background.draw(window)
        self.__draw_buttons(window)
        self.__selector.draw(window)
        self.drawings_above(window)

    def __update(self) -> None:
        self.__basic_piece.get_window_manager().update_window()
        self.__update_selector_position()
        self.other_updates()

    def __configure_buttons(self) -> list[Button]:
        buttons = self.create_buttons()
        buttons = self.__align_buttons(buttons)

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

    def __align_buttons(self, buttons: list[Button]) -> list[Button]:
        button_box_height_without_spaces = self.__calculate_button_box_height(buttons)
        space_between_buttons = int(button_box_height_without_spaces * Menu.BUTTON_SPACING_PERCENTAGE) \
                                // len(buttons)

        if self.__button_alignment == 1:
            buttons = self.__align_buttons_on_top(buttons, space_between_buttons)
        elif self.__button_alignment == 2:
            buttons = self.__align_buttons_on_center(buttons, space_between_buttons)
        else:
            buttons = self.__align_buttons_on_bottom(buttons, space_between_buttons)

        return buttons

    @staticmethod
    def __calculate_button_box_height(buttons: list[Button], space_between_buttons: int=0) -> int:
        overall_spacing_between_buttons = (len(buttons) - 1) * space_between_buttons
        button_box_height = sum([button.get_height() for button in buttons]) \
                            + overall_spacing_between_buttons

        return button_box_height

    def __align_buttons_on_top(self, buttons: list[Button], space_between_buttons: int) -> list[Button]:
        midtop_x, midtop_y = self.__background.get_midtop()

        new_midtop_y = midtop_y + int(self.__background.get_height() * Menu.BUTTONS_MARGIN_PERCENTAGE)
        initial_midtop = midtop_x, new_midtop_y

        return self.__adjust_button_alignment(buttons, initial_midtop, space_between_buttons)

    def __align_buttons_on_center(self, buttons: list[Button], space_between_buttons: int) -> list[Button]:
        center_x, center_y = self.__background.get_center()
        button_box_height = self.__calculate_button_box_height(buttons, space_between_buttons)

        midtop_y = center_y - button_box_height // 2
        initial_midtop = center_x, midtop_y

        return self.__adjust_button_alignment(buttons, initial_midtop, space_between_buttons)

    def __align_buttons_on_bottom(self, buttons: list[Button], space_between_buttons: int) -> list[Button]:
        midbottom_x, midbottom_y = self.__background.get_midbottom()
        button_box_height = self.__calculate_button_box_height(buttons, space_between_buttons)

        midtop_y = midbottom_y - button_box_height \
                       - int(self.__background.get_height() * Menu.BUTTONS_MARGIN_PERCENTAGE)
        initial_midtop = midbottom_x, midtop_y

        return self.__adjust_button_alignment(buttons, initial_midtop, space_between_buttons)

    @staticmethod
    def __adjust_button_alignment(
            buttons: list[Button],
            initial_midtop: tuple[int, int],
            space_between_buttons: int
    ) -> list[Button]:
        for index, button in enumerate(buttons):
            if index == 0:
                button.set_top_shape_midtop(initial_midtop)
            else:
                previous_midbottom = buttons[index - 1].get_bottom_shape_midbottom()
                midtop_y = previous_midbottom[1] + space_between_buttons
                button.set_top_shape_midtop((previous_midbottom[0], midtop_y))

        return buttons

    @abstractmethod
    def other_events(self) -> None:
        """Manage other events in the menu."""
        pass

    @abstractmethod
    def drawings_below(self, window: Surface) -> None:
        """
        Manages drawings displayed one layer below the menu.

        Parameters
        ----------
        window : Surface
            The window where other things can be drawn.
        """
        pass

    @abstractmethod
    def drawings_above(self, window: Surface) -> None:
        """
        Manages drawings displayed one layer above the menu.

        Parameters
        ----------
        window : Surface
            The window where other things can be drawn.
        """
        pass

    @abstractmethod
    def other_updates(self) -> None:
        """Manage other updates in the menu."""
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

        if not button.the_selector_is_next_to_the_button(self.__selector.get_center()[1]):
            center = self.__calculate_selector_center(button)
            self.__selector.set_center(center)

    def __calculate_selector_center(self, current_button: Button) -> tuple[int, int]:
        x = current_button.get_bottom_shape_midleft()[0] - self.__selector.get_width()
        y = current_button.get_bottom_shape_midleft()[1]

        return x, y

    def __directional_key_events(self, event: Event) -> None:
        if event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            self.__pressed_up(pressed_keys)
            self.__pressed_down(pressed_keys)

    def __pressed_up(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[Menu.KEYS["up"]] and not pressed_keys[Menu.KEYS["select"]]:
            if self.__current_button - 1 in range(0, len(self.__buttons)):
                self.__current_button -= 1
            else:
                self.__current_button = len(self.__buttons) - 1

            self.__sound_manager.play_sound("scroll")

    def __pressed_down(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[Menu.KEYS["down"]] and not pressed_keys[Menu.KEYS["select"]]:
            if self.__current_button + 1 in range(0, len(self.__buttons)):
                self.__current_button += 1
            else:
                self.__current_button = 0

            self.__sound_manager.play_sound("scroll")

    def close_all(self) -> None:
        """Closes the Pygame window and exits the program."""
        self.__basic_piece.close_all()

    def quit(self) -> None:
        """Close the menu."""
        self.__is_running = False

    def __reset_state(self) -> None:
        self.__current_button = 0
        self.__background.reset_image_loop()
        self.__selected_option = ButtonOption.NONE
        self.__is_running = True
        self.reset_other_states()

    @abstractmethod
    def reset_other_states(self) -> None:
        """
        Resets other menu states when it is closed.
        """
        pass

    def __draw_buttons(self, window: Surface) -> None:
        for button in self.__buttons:
            button.draw(window)

    @staticmethod
    def __check_button_alignment(button_alignment: int) -> int:
        if button_alignment not in [1, 2, 3]:
            raise ValueError("Button alignment does not have a valid value! possible values are 1, 2 and 3.")

        return button_alignment
