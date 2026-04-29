"""List exercise."""


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    Examples:
    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]

    :param results_string: A string containing names and scores separated by commas.
                           Each entry has a score and optionally a name. Example: "ago 123,peeter 11"
    :param min_result: Minimum score to include a name in the result. Example: 10
    :return: A list of names with scores >= min_result, preserving input order. Example: ["ago", "peeter"]
    """
    if not results_string:
        return []
    names = []
    entries = results_string.split(",")
    for entry in entries:
        parts = entry.split()
        score = int(parts[-1])
        name_parts = parts[:-1]
        if name_parts and score >= min_result:
            name = " ".join(name_parts)
            names.append(name)
    return names


if __name__ == '__main__':
    print(get_names_from_results("ago 123,peeter 11", 0))  # ["ago", "peeter"]
    print(get_names_from_results("ago 123,peeter 11,33", 10))  # ["ago", "peeter"]  # 33 does not have the name
    print(get_names_from_results("ago 123,peeter 11", 100))  # ["ago"]
    print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11))  # ["ago", "peeter",  "kitty11!!"]
    print(get_names_from_results("ago 123,peeter 11,kusti riin 14", 12))  # ["ago", "kusti riin"]
