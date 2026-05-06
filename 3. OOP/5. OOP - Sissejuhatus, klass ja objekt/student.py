"""Simple oop."""


class Student:
    """Represent a student."""

    def __init__(self, name: str, finished: bool = False):
        """Initialize a Student object with name and completion status.

        :param name: The student's name.
        :param finished: Completion status. Defaults to False.
        """
        self.name = name
        self.finished = finished
