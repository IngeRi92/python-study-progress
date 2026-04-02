"""Find people who are taller than the height limit."""


def find_people_taller_than_limit(people_dict: dict, height_limit: int) -> list:
    """
    Return a list of names that are taller than the given limit.

    find_people_taller_than_limit({"Tom": 182, "Mari": 175, "John": 190}, 185) => "John"

    :param people_dict: dictionary with people's names and heights
    :param height_limit: integer height limit
    :return list of names that are taller than the given height limit.
    """
    taller_people = []
    for name, height in people_dict.items():
        if height > height_limit:
            taller_people.append(name)
    return taller_people


if __name__ == "__main__":
    print(
        find_people_taller_than_limit({"Tom": 182, "Mari": 175, "John": 190}, 185)
    )  # => ["John"]
    print(find_people_taller_than_limit({}, 150))  # => []
    print(find_people_taller_than_limit({"Tom": 182, "Mari": 156, "Karl": 170}, 156))
    # => ["Tom", "Karl"]
    print(find_people_taller_than_limit({"Pille": 167, "Kalle": 169}, 170))  # => []
