"""BMI calculator."""


def bmi_calculator(height, weight):
    """Calculate BMI and return weight category."""
    bmi = weight / (height**2)
    if bmi <= 18.5:
        return "Alakaaluline"
    elif bmi <= 25.0:
        return "Normaalkaalus"
    elif bmi <= 30.0:
        return "Ülekaaluline"
    else:
        return "Rasvunud"
