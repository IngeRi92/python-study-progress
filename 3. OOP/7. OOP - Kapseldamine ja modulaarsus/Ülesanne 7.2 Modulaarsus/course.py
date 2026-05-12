"""Course class with name and grades."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student


class Course:
    """Class representing a course with a name and student grades."""

    def __init__(self, name: str):
        """Initialize a course with a name and empty grade list."""
        self.name = name
        self.__grades: list[tuple[Student, int]] = []

    def add_grade(self, student: Student, grade: int):
        """Add a grade for the specified student."""
        self.__grades.append((student, grade))

    def get_grades(self) -> list[tuple[Student, int]]:
        """Return a list of (student, grade) tuples for this course."""
        return list(self.__grades)

    def get_average_grade(self) -> float:
        """Return the course average grade, or -1 if no grades exist."""
        if not self.__grades:
            return -1
        return sum(grade for _, grade in self.__grades) / len(self.__grades)

    def __repr__(self):
        """Return the course name as the representation."""
        return self.name
