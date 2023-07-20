from snakegame import constants, validation, util


class RecordManager:
    """
    Manage game record. You can read or write a new record.

    Attributes
    ----------
    __record_path : str
        The path to the record file.
    __record : int
        The record.
    """

    def __init__(
            self,
            record_path: str=constants.RECORD
    ):
        """
        initialize the RecordManager.

        Parameters
        ----------
        record_path : str, optional
            The path to the record file (default is constants.RECORD).

        Raises
        ------
        FileNotFoundError
            If the 'record_path' is not found.
        """
        self.__record_path = validation.is_valid_path(record_path, "'record path' not found!")
        self.__record = self.get_record()

    def set_record(self, new_record: int) -> None:
        """
        Overwrite the record if the new one is greater.

        Parameters
        ----------
        new_record : int
            The new record.
        """
        if new_record > self.__record:
            util.overwrite_txt(self.__record_path, str(new_record))

    def get_record(self) -> int:
        """
        Return the record.

        Returns
        -------
        record : int
            The record.
        """
        record = util.read_txt(self.__record_path)[0]
        return int(record)

    def reset_record(self) -> None:
        """Reset the record."""
        util.overwrite_txt(self.__record_path, "0")
