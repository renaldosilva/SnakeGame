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
            The paths of sounds accompanied by their names (default is constants.SOUNDS).

        Raises
        ------
        FileNotFoundError
            If the 'sound_paths' are not found.
        """
        pygame.mixer.init()
        self.__current_volume = self.__check_initial_volume(initial_volume)
        self.__sounds = self.__load_sounds(self.__check_sound_paths(sound_paths))

    def play_sound(self, name: str, loops: int=0) -> None:
        """
        Play the sound, but only if the name exists.

        Parameters
        ----------
        name: str
            The name of the sound.
        loops: int, optional
            The number of times the sound will be repeated (default is 0).
        """
        sound = self.__sounds.get(name.lower())

        if sound:
            sound.play(loops)
            self.__sounds[name.lower()] = sound

    def stop_sound(self, name: str) -> None:
        """
        Stop the sound, but only if the name exists.

        Parameters
        ----------
        name: str
            The name of the sound.
        """
        sound = self.__sounds.get(name.lower())

        if sound is not None:
            sound.stop()

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

    def get_current_volume(self) -> int:
        """
        Returns the current volume level.

        Returns
        -------
        current_volume: int
            The volume level.
        """
        return self.__current_volume

    def __apply_volume(self) -> None:
        for music in self.__sounds.values():
            music.set_volume(self.__current_volume * 0.1)

    def __load_sounds(self, sound_paths: dict[str, str]) -> dict[str, Sound]:
        musics = {}
        for name in sound_paths.keys():
            music = pygame.mixer.Sound(sound_paths[name])
            music.set_volume(self.__current_volume * 0.1)
            musics[name.lower()] = music

        return musics

    @staticmethod
    def __check_sound_paths(sound_paths: dict[str, str]) -> dict[str, str]:
        validation.check_paths(list(sound_paths.values()), "'path_of_music' not found!")
        return sound_paths

    @staticmethod
    def __check_initial_volume(volume: int) -> int:
        if not (0 <= volume <= 10):
            raise ValueError("The volume must be between 0 and 10!")

        return volume
