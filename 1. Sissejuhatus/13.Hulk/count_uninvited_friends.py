"""Count uninvited friends."""


def count_uninvited_friends(friends: list, invited: list) -> int:
    """
    How many friends were not invited.

    There is a list of friends and a list of invited people.
    The function returns the count of people who were not invited.

    No loops required.

    count_uninvited_friends(["mati", "kati"], []) => 2
    count_uninvited_friends(["mati", "kati"], ["kati"]) => 1
    count_uninvited_friends(["mati", "kati"], ["kati", "rein"]) => 1
    """
    return len(set(friends) - set(invited))


if __name__ == "__main__":
    # run this file to test the function
    print(count_uninvited_friends(["mati", "kati"], []))  # 2
    print(count_uninvited_friends(["mati", "kati"], ["kati"]))  # 1
