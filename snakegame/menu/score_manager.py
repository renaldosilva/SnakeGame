from snakegame import constants, validation, util


class ScoreManager:
    """
    Manage game score. You can read or write a new score.

    Attributes
    ----------
    __score_path : str
        The path to the record file.
    __score : int
        The record.
    """

    def __init__(
            self,
            score_path: str=constants.SCORE
    ):
        """
        initialize the ScoreManager.

        Parameters
        ----------
        score_path : str, optional
            The path to the score file (default is constants.SCORE).

        Raises
        ------
        FileNotFoundError
            If the 'record_path' is not found.
        """
        self.__score_path = validation.is_valid_path(score_path, "'score path' not found!")
        self.__score = self.get_score()

    def set_score(self, new_score: int) -> None:
        """
        Overwrite the score if the new one is greater.

        Parameters
        ----------
        new_score : int
            The new score.
        """
        if new_score > self.__score:
            util.overwrite_txt(self.__score_path, str(new_score))

    def get_score(self) -> int:
        """
        Return the score.

        Returns
        -------
        score : int
            The score.
        """
        score = util.read_txt(self.__score_path)[0]
        return int(score)

    def reset_score(self) -> None:
        """Reset the score."""
        util.overwrite_txt(self.__score_path, "0")
