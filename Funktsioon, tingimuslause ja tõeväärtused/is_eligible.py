"""Special offer."""


def is_eligible(age, has_valid_id, is_student, is_employed):
    """Check if a person is eligible for a special offer.

    A person is eligible if they are at least 18 years old,
    have a valid ID, and are either a student or employed.
    """
    if age >= 18 and has_valid_id and (is_student or is_employed):
        return True
    return False
