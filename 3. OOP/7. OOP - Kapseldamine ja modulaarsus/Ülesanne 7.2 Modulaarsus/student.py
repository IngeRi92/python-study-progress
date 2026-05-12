"""Student class with student name and grades."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from course import Course


class Student:
    """Class representing a student with a name, optional id, and grades."""

    def __init__(self, name: str):
        """Initialize a student with a name and empty grade list."""
        self.name = name
        self.id: int | None = None
        self.__grades: list[tuple[Course, int]] = []

    def set_id(self, id: int):
        """Set the student's unique identifier once if it has not been assigned."""
        if self.id is None:
            self.id = id

    def get_id(self) -> int | None:
        """Return the student's identifier, or None if it is not set."""
        return self.id

    def add_grade(self, course: Course, grade: int):
        """Add a grade for the specified course."""
        self.__grades.append((course, grade))

    def get_grades(self) -> list[tuple[Course, int]]:
        """Return a list of (course, grade) tuples for this student."""
        return list(self.__grades)

    def get_average_grade(self) -> float:
        """Return the student's average grade, or -1 if no grades exist."""
        if not self.__grades:
            return -1
        return sum(grade for _, grade in self.__grades) / len(self.__grades)

    def __repr__(self) -> str:
        """Return the student's name as the representation."""
        return self.name
