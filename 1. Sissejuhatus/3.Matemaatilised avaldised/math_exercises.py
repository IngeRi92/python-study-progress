"""Math exercises."""
import math

# Time converter
total_seconds = 37810
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Trigonometry calculator
angle_deg = 339
angle_rad = math.radians(angle_deg)
sine = round(math.sin(angle_rad), 1)
cosine = round(math.cos(angle_rad), 1)

# Greetings
lots_of_heys = "Hey" * 87

# Adding numbers
num1 = 81
num2 = 69
string_numbers = str(num1) + str(num2)
