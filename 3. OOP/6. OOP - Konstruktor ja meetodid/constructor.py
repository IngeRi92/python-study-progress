"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Initialize without parameters. Create firstname, lastname and age fields with default values."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname: str, lastname: str, age: int):
        """Initialize with parameters. Create firstname, lastname and age fields with given values."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == "__main__":
    # empty usage
    empty_obj = Empty()

    # 3 x person usage
    person1 = Person()
    person1.firstname = "Luke"
    person1.lastname = "Skywalker"
    person1.age = 28

    person2 = Person()
    person2.firstname = "Leia"
    person2.lastname = "Organa"
    person2.age = 28

    person3 = Person()
    person3.firstname = "Han"
    person3.lastname = "Solo"
    person3.age = 35

    # 3 x student usage
    student1 = Student("Anakin", "Skywalker", 22)
    student2 = Student("Obi-Wan", "Kenobi", 35)
    student3 = Student("Padme", "Amidala", 32)
