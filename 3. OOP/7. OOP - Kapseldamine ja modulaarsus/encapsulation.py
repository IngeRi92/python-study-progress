"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name: str, id: int):
        """
        Create a new student.

        :param name: The name of the student.
        :param id: The id of the student.
        """
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self) -> int:
        """Return the id of the student."""
        return self.__id

    def set_name(self, name: str):
        """Set a new name for the student."""
        self.__name = name

    def get_name(self) -> str:
        """Return the current name of the student."""
        return self.__name

    def set_status(self, status: str):
        """
        Set a new status for the student.

        Status can be changed only to one of these values:
            Active, Expelled, Finished, Inactive.

        If status is not one of these values, do nothing.
        """
        if status in ["Active", "Expelled", "Finished", "Inactive"]:
            self.__status = status

    def get_status(self) -> str:
        """Return the current status of the student."""
        return self.__status
