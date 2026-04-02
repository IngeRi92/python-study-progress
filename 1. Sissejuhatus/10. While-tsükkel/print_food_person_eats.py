"""Yummy yummy."""


def print_food_person_eats(foods: list, many_can_eat: int):
    """
    Print foods that have been eaten by the person.

    Given a list of foods, a person can eat only a certain number of items. Starting from the beginning of the list,
    the function simulates the person eating the specified number of foods by printing out "Eating [food]". Print out
    every food the person eats before reaching the limit.

    :param foods: List of foods on the table
    :param many_can_eat: An integer that shows how many items can be eaten by person
    :return: Nothing
    """
    eaten = 0
    while eaten < many_can_eat and eaten < len(foods):
        print(f"Eating {foods[eaten]}")
        eaten += 1


if __name__ == "__main__":
    print_food_person_eats(["pineapple", "bread", "muffin", "grape", "cheese"], 2)
    """"
    Eating pineapple
    Eating bread
    """
