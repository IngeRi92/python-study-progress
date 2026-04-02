"""Test cases for fruit order."""
from fruit_order import fruit_order


def test_fruit_order_zero_amount_zero_big():
    """Return 0 if only small baskets are given."""
    assert fruit_order(2, 0, 0) == 0


def test_fruit_order__all_zero():
    """Return 0 if all inputs are zero."""
    assert fruit_order(0, 0, 0) == 0


def test_fruit_order__zero_amount_zero_small():
    """Return 0 if only big baskets are given."""
    assert fruit_order(0, 2, 0) == 0


def test_fruit_order__zero_amount_others_not_zero():
    """Return 0 if amount is zero and both basket types are given."""
    assert fruit_order(3, 4, 0) == 0


def test_fruit_order__only_big_exact_match():
    """Return 0 if only big baskets are given and they exactly match the order."""
    assert fruit_order(0, 3, 15) == 0


def test_fruit_order__only_big_not_enough_but_multiple_of_5():
    """Return -1 if only big baskets are given but they are not enough to fulfill the order."""
    assert fruit_order(0, 2, 15) == -1


def test_fruit_order__only_big_not_enough():
    """Return -1 if only big baskets are given but they cannot fulfill the order."""
    assert fruit_order(0, 2, 14) == -1


def test_fruit_order__only_big_more_than_required_no_match():
    """Return -1 if only big baskets are given and they exceed the order without matching."""
    assert fruit_order(0, 4, 16) == -1


def test_fruit_order__only_small_match_more_than_5_smalls():
    """Return correct number of small baskets if only small baskets are given and they match the order."""
    assert fruit_order(7, 0, 7) == 7


def test_fruit_order__only_small_not_enough_more_than_5_smalls():
    """Return -1 if only small baskets are given but they are not enough to fulfill the order."""
    assert fruit_order(8, 0, 12) == -1


def test_fruit_order__only_small_exact_match():
    """Return correct number of small baskets if only small baskets are given and they exactly match the order."""
    assert fruit_order(5, 0, 5) == 5


def test_fruit_order__only_small_not_enough():
    """Return -1 if only small baskets are given but they cannot fulfill the order."""
    assert fruit_order(3, 0, 5) == -1


def test_fruit_order__match_with_more_than_5_smalls():
    """Return correct number of small baskets when both basket types are given and they match the order."""
    assert fruit_order(7, 2, 17) == 7


def test_fruit_order__all_positive_exact_match():
    """Return correct number of small baskets when both basket types are given and they exactly match the order."""
    assert fruit_order(4, 3, 19) == 4


def test_fruit_order__use_all_smalls_some_bigs():
    """Return correct number of small baskets when both basket types are given and all smalls are used."""
    assert fruit_order(3, 9, 23) == 3


def test_fruit_order__use_some_smalls_all_bigs():
    """Return correct number of small baskets when both basket types are given and all bigs are used."""
    assert fruit_order(4, 3, 19) == 4


def test_fruit_order__not_enough():
    """Return -1 when both basket types are given but they cannot fulfill the order."""
    assert fruit_order(2, 2, 20) == -1


def test_fruit_order__enough_bigs_not_enough_smalls():
    """Return -1 when big baskets are enough but small baskets are not enough to fulfill the order."""
    assert fruit_order(1, 6, 29) == -1


def test_fruit_order__not_enough_with_more_than_5_smalls():
    """Return -1 when both basket types are given but they cannot fulfill the order."""
    assert fruit_order(10, 1, 35) == -1


def test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Return -1 when big baskets are enough but small baskets are not enough to fulfill the order with large numbers."""
    assert fruit_order(3, 1935, 9599) == -1


def test_fruit_order__match_large_numbers():
    """Return correct number of small baskets when both basket types are given with large numbers and they match the order."""
    assert fruit_order(558, 999, 5553) == 558


def test_fruit_order__only_big_more_than_required_match():
    """Return correct number of small baskets if only big baskets are given and they exceed the order requirements."""
    assert fruit_order(0, 4, 15) == 0


def test_fruit_order__only_small_more_than_required():
    """Return correct number of small baskets if only small baskets are given and they exceed the order requirements."""
    assert fruit_order(10, 0, 6) == 6


def test_fruit_order__use_some_smalls_some_bigs():
    """Return correct number of small baskets when both basket types are given and some of both are used."""
    assert fruit_order(3, 9, 22) == 2
