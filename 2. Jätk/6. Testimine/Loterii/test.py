"""Test cases for lottery."""
from lottery import lottery


def test_lottery_all_fives():
    """Return 10 if all numbers are 5."""
    assert lottery(5, 5, 5) == 10


def test_lottery_all_same_not_five():
    """Return 5 if all numbers are the same but not 5."""
    assert lottery(2, 2, 2) == 5


def test_lottery_one_is_different_than_a():
    """Return 1 if both b and c are different than a."""
    assert lottery(3, 4, 5) == 1


def test_lottery_b_equals_a():
    """Return 0 if b equals a."""
    assert lottery(2, 2, 3) == 0


def test_lottery_c_equals_a():
    """Return 0 if c equals a."""
    assert lottery(4, 5, 4) == 0


def test_lottery_all_same_negative():
    """Return 5 if all numbers are the same negative number."""
    assert lottery(-1, -1, -1) == 5


def test_lottery_all_same_zero():
    """Return 5 if all numbers are zero."""
    assert lottery(0, 0, 0) == 5


def test_lottery_b_c_same_a_different():
    """Return 1 if b and c are the same and different from a."""
    assert lottery(1, 2, 2) == 1
