"""Airlines operating today."""


def airlines_operating_today(schedule: dict, airline_names: dict) -> set:
    """
    Return a set of unique airline names that have flights operating today.

    Airline names are presented as a dictionary where the key is the airline code
    and the value is the corresponding airline name.

    Flight code contains 3 letters and 4 numbers. The 3-letter code indicates the airline code.
    So, the 3-letter code should be taken from the airline_names dictionary (key).

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :param airline_names: Dictionary containing airline codes and corresponding names.
    :return: Set of unique airline names operating today.
    """
    result = set()
    for flight in schedule.values():
        flight_code = flight[1]
        airline_code = flight_code[:3]
        result.add(airline_names[airline_code])
    return result


if __name__ == '__main__':
    schedule = {'08:00': ('Tallinn', 'OWL1234'), '10:35': ('Helsinki', 'BHM5678'), '09:00': ('Tallinn', 'OWL1235')}
    airlines = {"OWL": "Owlbear Airlines", "BHM": "Beholder's Majesty Airlines"}
    print(airlines_operating_today(schedule, airlines))  # {'Owlbear Airlines', "Beholder's Majesty Airlines"}
