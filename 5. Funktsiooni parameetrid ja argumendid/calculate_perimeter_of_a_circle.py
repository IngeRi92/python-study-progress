"""Circle's perimeter."""

import math


def calculate_perimeter_of_a_circle(radius: int) -> float:
    """Return the perimeter of a circle."""
    circle_perimeter = round(math.pi * 2 * radius, 2)
    return circle_perimeter
