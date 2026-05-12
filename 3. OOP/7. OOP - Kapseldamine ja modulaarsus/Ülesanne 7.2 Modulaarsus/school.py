"""School class which stores information about courses and students."""

from student import Student
from course import Course


class School:
    """School class that stores students and courses.

    The school holds a collection of students and courses, and it can
    assign grades for students on courses that belong to the school.
    """

    def __init__(self, name: str):
        """Create a school with the given name."""
        self.name = name
        self.students: list[Student] = []
        self.courses: list[Course] = []
        self._next_id = 1

    def add_course(self, course: Course):
        """Add a course to the school if it is not already present."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        """Add a student to the school and assign a unique id."""
        if student not in self.students:
            student.set_id(self._next_id)
            self._next_id += 1
            self.students.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Add a grade for a student in a course if both belong to this school."""
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self) -> list[Student]:
        """Return the list of students in the order they were added."""
        return list(self.students)

    def get_courses(self) -> list[Course]:
        """Return the list of courses in the order they were added."""
        return list(self.courses)

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        """Return students ordered by descending average grade."""

        def student_average(student: Student) -> float:
            return student.get_average_grade()

        return sorted(
            self.students,
            key=student_average,
            reverse=True,
        )
