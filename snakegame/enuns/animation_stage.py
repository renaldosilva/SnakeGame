from enum import Enum


class AnimationStage(Enum):
    """
    Enumeration representing the stage of an animation.

    Attributes
    ----------
    NONE : int
        Represents the animation when it has not started yet.
    RUNNING : int
        Represents the animation when it is currently running.
    FINISHED : int
        Represents the animation when it has completed.
    """

    NONE = 0
    RUNNING = 1
    FINISHED = 2
