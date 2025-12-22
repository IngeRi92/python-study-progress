"""Math calculations."""

import math

# Area of a circle
radius = 90
circle_area = round(math.pi * radius**2, 2)

# Area of an equilateral triangle
side = 58
triangle_area = round((side**2 * math.sqrt(3)) / 4)

# Calculate discriminant
a = 73
b = 11
c = 37
discriminant = b**2 - 4 * a * c

# Calculate hypotenuse length
a = 81
b = 44
c = math.sqrt(a**2 + b**2)

# Calculate cathetus length
c_side = 88
a_side = 43
b_side = math.sqrt(c_side**2 - a_side**2)
