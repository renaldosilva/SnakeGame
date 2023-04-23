import pygame
from pygame.mixer import Sound

from snakegame import validation, constants

class SoundManager:
    """
    Manages game sounds. You can control overall volume and get specific sounds.

    Attributes
    ----------
    __current_volume : int {0, 1, 2, 3, 4, 5, 6 ,7, 8, 9, 10}
        The current volume of the game.
    __sounds: dict[str, Sound]
        The sounds of the game accompanied by their names.
        Names must match this list:
            - click;
            - menu;
            - scroll.
    """

    SOUND_NAMES = [
        "click",
        "menu",
        "scroll"
    ]
    """Manager sound name list.
    """

    def __init__(
            self,
            initial_volume: int=constants.INITIAL_VOLUME,
            sound_paths: dict[str, str]=constants.SOUNDS
    ):
        """
        initialize the SoundManager.

        Parameters
        ----------
        initial_volume : int {0, 1, 2, 3, 4, 5, 6 ,7, 8, 9, 10}, optional
            The initial volume of the game (default is constants.INITIAL_VOLUME).
        sound_paths: dict[str, str], optional
            The paths of sounds accompanied by their names.
            Names must match this list (default is constants.SOUNDS):
                - click;
                - menu;
                - scroll.

        Raises
        ------
        ValueError
            If the sound names are insufficient or incorrect and
            if the initial volume is out of range (1-3).
        FileNotFoundError
            If the 'sound_paths' are not found.
        """
        pygame.mixer.init()
        self.__current_volume = self.__check_initial_volume(initial_volume)
        self.__sounds = self.__load_sounds(self.__check_sound_paths(sound_paths))

    def get_click_sound(self) -> Sound:
        """
        Get button click sound.

        Returns
        -------
        Sound
            The click sound.
        """
        return self.__sounds["click"]

    def get_menu_background_sound(self) -> Sound:
        """
        Get menu background sound.

        Returns
        -------
        Sound
            The menu background sound.
        """
        return self.__sounds["menu"]

    def get_menu_scroll_sound(self) -> Sound:
        """
        Get menu scroll sound.

        Returns
        -------
        Sound
            The menu scroll sound.
        """
        return self.__sounds["scroll"]

    def volume_up(self) -> None:
        """Increase the volume level by 10%."""
        if self.__current_volume < 10:
            self.__current_volume += 1
            self.__apply_volume()

    def volume_down(self) -> None:
        """Decreases the volume level by 10%."""
        if 0 < self.__current_volume:
            self.__current_volume -= 1
            self.__apply_volume()

    def __apply_volume(self) -> None:
        for music in self.__sounds.values():
            music.set_volume(self.__current_volume * 0.1)

    def __load_sounds(self, sound_paths: dict[str, str]) -> dict[str, Sound]:
        musics = {}
        for name in sound_paths.keys():
            music = pygame.mixer.Sound(sound_paths[name])
            music.set_volume(self.__current_volume * 0.1)
            musics[name] = music

        return musics

    def __check_sound_paths(self, sound_paths: dict[str, str]) -> dict[str, str]:
        validation.check_paths(list(sound_paths.values()), "'path_of_music' not found!")
        self.__check_sound_names(list(sound_paths.keys()))

        return sound_paths
    @staticmethod
    def __check_sound_names(sound_names: list[str]) -> None:
        for name in sound_names:
            if name not in SoundManager.SOUND_NAMES:
                raise ValueError(
                    "Sound name error! Names must match this list: ["
                    + ", ".join(SoundManager.SOUND_NAMES) + "]."
                )

        if len(set(sound_names)) < len(SoundManager.SOUND_NAMES):
            raise ValueError(
                "Insufficient sounds! Names must match this list: ["
                + ", ".join(SoundManager.SOUND_NAMES) + "]."
            )

    @staticmethod
    def __check_initial_volume(initial_volume: float) -> float:
        if not (0 <= initial_volume <= 10):
            raise ValueError("The volume must be between 0 and 10!")

        return initial_volume


# Initialize the sound manager.
sound_manager = SoundManager()
