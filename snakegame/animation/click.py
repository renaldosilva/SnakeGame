from pygame import Rect

from snakegame.animation.animation import Animation
from snakegame.enuns.animation_stage import AnimationStage


class Click(Animation):
    """
    An animation that simulates a button being clicked.

    Attributes
    ----------
    bottom_shape : pygame.Rect
        The bottom shape of the button.
    click_stage : AnimationStage
        The current stage of the click animation.

    Methods
    -------
    animate(*extra) -> None
        Animates the button click based on the given parameters.
    reload_click(top_shape, bottom_shape, secondary_shapes=None) -> None
        Reloads the button click with new shapes.
    click_done() -> bool
        Checks if the click animation is finished.
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

    @property
    def bottom_shape(self) -> Rect:
        """
        Returns the bottom shape of the button.

        Returns
        -------
        bottom_shape: Rect
            The bottom shape.
        """
        return self.__bottom_shape

    @bottom_shape.setter
    def bottom_shape(self, bottom_shape: Rect) -> None:
        """
        Set the bottom shape of the button.

        Parameters
        ----------
        bottom_shape: Rect
            The new bottom shape.
        """
        self.__bottom_shape = bottom_shape

    @property
    def click_stage(self) -> AnimationStage:
        """
        Returns the click stage of the button.

        The click stage can be:
            NONE : int
                When it has not started yet.
            RUNNING : int
                When it is currently running.
            FINISHED : int
                When it has completed.

        Returns
        -------
        click_stage: AnimationStage
            The click stage.
        """
        return self.__click_stage

    def animate(self, *extra) -> None:
        """
        Animates the button click based on the given parameters.

        Parameters
        ----------
        *extra : tuple
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
    ):
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
        self.bottom_shape = bottom_shape

    def click_done(self) -> bool:
        """
        Checks if the click animation is finished.

        Returns
        -------
        result: bool
            Whether the click animation is finished.
        """
        return self.click_stage == AnimationStage.FINISHED

    def __start_click(self) -> None:
        new_coordinate = self.bottom_shape.x, self.bottom_shape.y
        super().set_current_coordinate(new_coordinate)
        self.__click_stage = AnimationStage.RUNNING

    def __end_click(self) -> None:
        super().restore_origin_coordinate()
        self.__click_stage = AnimationStage.FINISHED