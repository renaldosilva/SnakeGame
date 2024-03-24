from typing import Any

from pygame import Rect

from snakegame.animation.animation import Animation
from snakegame.enuns.animation_stage import AnimationStage


class Click(Animation):
    """
    An animation that simulates a button being clicked.

    Attributes
    ----------
    __bottom_shape : pygame.Rect
        The bottom shape of the button.
    __click_stage : AnimationStage
        The current stage of the click animation.
    """

    def __init__(
            self,
            top_shape: Rect,
            bottom_shape: Rect,
            secondary_shapes: list[Rect]=None
    ):
        """
        Initializes the click object.

        Parameters
        ----------
        top_shape : pygame.Rect
            The top shape of the button.
        bottom_shape : pygame.Rect
            The bottom shape of the button.
        secondary_shapes : list of pygame.Rect, optional
            The list of secondary shapes of the button.
        """
        super().__init__(top_shape, secondary_shapes)
        self.__bottom_shape = bottom_shape
        self.__click_stage = AnimationStage.NONE

    def animate(self, extra: tuple[Any, ...]=None) -> None:
        """
        Animates the button click based on the given parameters.

        Parameters
        ----------
        extra : tuple[Any, ...]
            A tuple containing the following values:
            - selector_over_button: bool, whether the selector is over the button.
            - is_clicking: bool, whether the button is being clicked.
        """
        selector_over_button = extra[0]
        is_clicking = extra[1]

        if selector_over_button and is_clicking:
            self.__start_click()
        elif self.__click_stage == AnimationStage.RUNNING:
            self.__end_click()
        else:
            self.__click_stage = AnimationStage.NONE

    def reload_click(
            self,
            top_shape: Rect,
            bottom_shape: Rect,
            secondary_shapes: list[Rect]=None
    ) -> None:
        """
        Reloads the button click with new shapes.

        Parameters
        ----------
        top_shape : pygame.Rect
            The top shape of the button.
        bottom_shape : pygame.Rect
            The bottom shape of the button.
        secondary_shapes : list of pygame.Rect, optional
            The list of secondary shapes of the button.
        """
        super().reload_animation(top_shape, secondary_shapes)
        self.__bottom_shape = bottom_shape

    def click_done(self) -> bool:
        """
        Checks if the click animation is finished.

        Returns
        -------
        result: bool
            Whether the click animation is finished.
        """
        return self.__click_stage == AnimationStage.FINISHED

    def __start_click(self) -> None:
        new_coordinate = self.__bottom_shape.x, self.__bottom_shape.y
        super().set_current_coordinate(new_coordinate)
        self.__click_stage = AnimationStage.RUNNING

    def __end_click(self) -> None:
        super().restore_origin_coordinate()
        self.__click_stage = AnimationStage.FINISHED
