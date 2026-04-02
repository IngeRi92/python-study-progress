"""Find the shortest way back in a taxicab geometry."""


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    moves = {"N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
    north_south = 0
    east_west = 0
    for move in path:
        ns_change, ew_change = moves[move]
        north_south += ns_change
        east_west += ew_change
    result = ""
    if north_south > 0:
        result += "S" * north_south
    elif north_south < 0:
        result += "N" * abs(north_south)
    if east_west > 0:
        result += "W" * east_west
    elif east_west < 0:
        result += "E" * abs(east_west)
    return result


if __name__ == "__main__":
    print(shortest_way_back("NNN"))  # "SSS"
    print(shortest_way_back("SS"))  # "NN"
    print(shortest_way_back("E"))  # "W"
    print(shortest_way_back("WWWW"))  # "EEEE"
    print(shortest_way_back(""))  # ""
    print(shortest_way_back("NESW"))  # ""
