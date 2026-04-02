"""Test cases for students study."""
from students_study import students_study


def test_students_study_during_day():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    assert students_study(12, True) is True


def test_students_study_during_day_no_coffee():
    """
    During the day, students do not study when there is no coffee.

    This case represents the time period of a day and no coffee is present.
    Expected result: False.
    """
    assert students_study(11, False) is False


def test_students_study_during_evening():
    """
    During the evening, students study regardless of coffee.

    This case represents the time period of an evening and no coffee is present.
    Expected result: True.
    """
    assert students_study(20, False) is True


def test_student_study__evening_coffee_true():
    """
    During the evening, students study when there is coffee.

    Expected result: True.
    """
    assert students_study(19, True) is True


def test_students_not_study_at_night():
    """
    During the night, students do not study even if there is coffee.

    This case represents the time period of night and coffee is present.
    Expected result: False.
    """
    assert students_study(2, True) is False


def test_students_not_study_at_night_no_coffee():
    """
    During the night, students do not study when there is no coffee.

    Expected result: False.
    """
    assert students_study(3, False) is False


def test_student_study__evening_edge_case_coffee_true():
    """
    During the evening edge case, students study when there is coffee.

    Expected result: True.
    """
    assert students_study(18, True) is True
    assert students_study(24, True) is True


def test_student_study__evening_edge_case_coffee_false():
    """
    During the evening edge case, students study when there is no coffee.

    Expected result: True.
    """
    assert students_study(18, False) is True
    assert students_study(24, False) is True


def test_student_study__night_edge_case_coffee_true():
    """
    During the night edge case, students do not study when there is coffee.

    Expected result: False.
    """
    assert students_study(1, True) is False
    assert students_study(4, True) is False


def test_student_study__night_edge_case_coffee_false():
    """
    During the night edge case, students do not study when there is no coffee.

    Expected result: False.
    """
    assert students_study(1, False) is False
    assert students_study(4, False) is False


def test_student_study__day_edge_case_coffee_true():
    """
    During the day edge case, students study when there is coffee.

    Expected result: True.
    """
    assert students_study(5, True) is True
    assert students_study(17, True) is True


def test_student_study__day_edge_case_coffee_false():
    """
    During the day edge case, students do not study when there is no coffee.

    Expected result: False.
    """
    assert students_study(5, False) is False
    assert students_study(17, False) is False
