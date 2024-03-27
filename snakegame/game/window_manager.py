from pygame import Surface, display

from snakegame import validation, util, constants


class WindowManager:
    """
    Manages basic window operations.

    Attributes
    ----------
    __window : Surface
        The surface to use as the game's main display window.
    __color : tuple[int, int, int]
        The RGB color tuple used to fill the game's display window.
    __applied_blur : bool
        Indicates whether blur has already been applied to a screenshot.
    """

    def __init__(
            self,
            window: Surface,
            color: tuple[int, int, int]=constants.LIGHT_GREEN_1
    ):
        """
        initialize the WindowManager.

        Parameters
        ----------
        window : Surface
            The window that will be managed.
        color : tuple[int, int, int], optional
            The RGB color tuple used to fill the game's display window (default is constants.LIGHT_GREEN_1).

        Raises
        ------
        ValueError
            If the 'color' is not in the RGB range (0-255, 0-255, 0-255).
        """
        self.__window = window
        self.__color = validation.is_valid_rgb(color, "'color' out of RGB range!")
        self.__applied_blur = False

    def get_window(self) -> Surface:
        """
        Returns the Pygame Surface object that represents the game window.

        Returns
        -------
        window : Surface
            The game window.
        """
        return self.__window

    def get_window_center(self) -> tuple[int, int]:
        """
        Returns the coordinate of the window's center.
        """
        return self.__window.get_width() // 2, self.__window.get_height() // 2

    @staticmethod
    def update_window() -> None:
        """Calls the Pygame display's update() method to update the game window."""
        display.update()

    def draw_window(self) -> None:
        """Fills the game window with the background color specified by the color attribute."""
        self.__window.fill(self.__color)

    def apply_blur(self, radius: int=7) -> None:
        """
        Applies a blur to a screenshot of the current window. To use this effect
        more than once, you need to exit the blur state.

        Parameters
        ----------
        radius : int, optional
            Indicates the intensity of the blur (default value is 7).

        Raises
        ------
        ValueError
                If 'radius' is less than 1.
        """
        if not self.__applied_blur:
            print_screen = self.__window.copy()
            screen_with_blur = util.apply_blur(print_screen, radius)
            self.__window.blit(screen_with_blur, (0, 0))

            self.__applied_blur = True

    def reset_blur_state(self) -> None:
        """
        Resets the blur state so the effect can be applied to other screenshots.
        """
        self.__applied_blur = False
