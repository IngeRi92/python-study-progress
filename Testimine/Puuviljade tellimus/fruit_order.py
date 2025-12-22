"""Fruit order."""


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    max_big_baskets_needed = ordered_amount // 5
    big_baskets_used = min(big_baskets, max_big_baskets_needed)
    remaining_amount = ordered_amount - (big_baskets_used * 5)

    if remaining_amount <= small_baskets:
        return remaining_amount
    else:
        return -1
