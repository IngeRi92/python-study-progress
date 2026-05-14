"""Song contest system."""


class Song:
    """Song."""

    def __init__(self, name: str, genre: str, duration: float, difficulty: int):
        """
        Song object initialization.

        :param name: Song name.
        :param genre: Song genre.
        :param duration: Song duration.
        :param difficulty: Song difficulty.
        """
        self.name = name
        self.genre = genre
        self.duration = duration
        if difficulty > 10:
            self.difficulty = 10
        elif difficulty < 1:
            self.difficulty = 1
        else:
            self.difficulty = difficulty

    def __repr__(self):
        """
        Return song.

        :return: String in format "{name}, style: {genre}".
        """
        return f"{self.name}, style: {self.genre}"


class Contestant:
    """Contestant class."""

    def __init__(self, first_name: str, last_name: str, age: int, vocals: float):
        """
        Contestant object initialization.

        :param first_name: First name.
        :param last_name: Last name.
        :param age: Age.
        :param vocals: Vocals.
        """
        self.name = f"{first_name} {last_name}".title()
        self.age = age
        self.vocals = vocals
        self.song = None

    def __repr__(self):
        """
        Return contestant.

        :return: String with full name.
        """
        return self.name

    def choose_song(self, song_list: list[Song]) -> Song | None:
        """
        Choose song for the competition.

        Chosen song name must contain the most characters from the contestant full name.
        If there are no songs which contain at least one character of contestant's name, return None.

        If the contestant name is "ABC"
        Then
        "EFG" - would not match at all
        "ABC" and "ABCABC" and "CCAAB" have the most matches (all 3 characters from the name)
        "ABU ABBA" and "Baaky" have 2 matching characters.

        If multiple songs have the same number of matching characters, then any song is suitable
        (meaning it doesn't matter which one to choose - the first one is ok).

        :param song_list: List of songs to chose from.
        :return: Contestants song or None.
        """
        name_chars = set(self.name.lower().replace(" ", ""))
        best_song = None
        best_count = 0
        for song in song_list:
            song_chars = set(song.name.lower())
            count = len(song_chars & name_chars)
            if count > best_count:
                best_count = count
                best_song = song
        if best_count == 0:
            return None
        self.song = best_song
        return best_song


class Judge:
    """Judge."""

    def __init__(self, name: str, preferences: list[str]):
        """
        Judge object initialization.

        :param name: Name.
        :param preferences: Preferences.
        """
        self.name = name.title()
        self.preferences = preferences

    def __repr__(self):
        """
        Return judge.

        :return: String with judge name.
        """
        return self.name


class Competition:
    """Competition."""

    def __init__(self, minimum_age: int, maximum_age: int, suitable_genres: list):
        """
        Competition object initialization.

        :param minimum_age: Maximum age.
        :param maximum_age: Minimum age.
        :param suitable_genres: Suitable genres.
        """
        self.minimum_age = minimum_age
        self.maximum_age = maximum_age
        self.suitable_genres = suitable_genres
        self.contestants = []
        self.judges = []

    def add_contestant(self, contestant: Contestant) -> bool:
        """
        Register contestant.

        Can be registered if is Contestant and age and chosen song genre is allowed on the competition.

        :param contestant: Contestant.
        :return: Boolean.
        """
        if not isinstance(contestant, Contestant):
            return False
        if contestant.song is None:
            return False
        if contestant.song.genre not in self.suitable_genres:
            return False
        if not (self.minimum_age <= contestant.age <= self.maximum_age):
            return False
        self.contestants.append(contestant)
        return True

    def add_judge(self, judge: Judge) -> bool:
        """
        Add judge to the competition.

        Can be added only in case if he/she is Judge and likes the same genres that are allowed on the competition.
        All the judge's genres have to be allowed.

        :param judge: Judge.
        :return: Boolean.
        """
        if not isinstance(judge, Judge):
            return False
        for genre in judge.preferences:
            if genre not in self.suitable_genres:
                return False
        self.judges.append(judge)
        return True

    def create_order_of_performances(self) -> list[Contestant]:
        """
        Create order of performances.

        First ones to perform are the youngest. In case of same age, alphabetically by song name.

        :return: Order of performances.
        """
        sorted_list = []
        for contestant in self.contestants:
            sorted_list.append((contestant.age, contestant.song.name, contestant))
        sorted_list.sort()
        return [item[2] for item in sorted_list]

    def perform_song_rankings(self) -> dict:
        """
        Create ranking chart where key is song and value is ranking.

        Ranking = song difficulty * contestant vocals + 10 if judge likes that genre.

        :return: Rankings
        """
        rankings = {}
        for contestant in self.contestants:
            song = contestant.song
            ranking = song.difficulty * contestant.vocals
            for judge in self.judges:
                if song.genre in judge.preferences:
                    ranking += 10
            rankings[song] = ranking
        return rankings

    def get_suitable_genres(self) -> list:
        """
        Sort competition genres by name (a-z).

        :return: Sorted genres.
        """
        return sorted(self.suitable_genres)

    def get_contestants(self) -> list:
        """
        Sort contestants by names (a-z).

        :return: Sorted contestants.
        """
        sorted_list = []
        for contestant in self.contestants:
            sorted_list.append((contestant.name, contestant))
        sorted_list.sort()
        return [item[1] for item in sorted_list]

    def get_judges(self) -> list:
        """
        Sort Judges by names (a-z).

        :return: Sorted judges.
        """
        sorted_list = []
        for judge in self.judges:
            sorted_list.append((judge.name, judge))
        sorted_list.sort()
        return [item[1] for item in sorted_list]

    def get_judges_rankings_in_order(self) -> list[Song]:
        """
        Sort songs by judges rankings from best to worst.

        :return: Sorted songs.
        """
        rankings = self.perform_song_rankings()
        sorted_list = []
        for song, ranking in rankings.items():
            sorted_list.append((ranking, song))
        sorted_list.sort(reverse=True)
        return [item[1] for item in sorted_list]

    def get_winner(self) -> Song:
        """
        Return winner song by judges ranking.

        :return: Winner song.
        """
        rankings = self.perform_song_rankings()
        return max(rankings, key=rankings.get)


if __name__ == "__main__":
    # Song contest
    song1 = Song("Best day ever", "rock", 3.5, 15)
    song2 = Song("My enemy hair", "pop", 2.0, 5)
    song3 = Song("Kinda normal", "pop", 3.0, 7)
    song_list = [song1, song2, song3]

    bob = Contestant("bob", "Ernest", 20, 9)
    mari = Contestant("mari", "riisa", 9, 0)
    kiur = Contestant("Kiur", "norman", 15, 6)

    competition = Competition(10, 35, ["rock", "pop"])

    judge1 = Judge("Judy", ["Rock"])
    judge2 = Judge("emili", ["rock", "pop"])

    #  Choosing songs for competition
    print(bob.choose_song(song_list))  # Best day ever, style: rock
    print(mari.choose_song(song_list))  # My enemy hair, style: pop
    print(kiur.choose_song(song_list))  # Kinda normal, style: pop

    #  Register to competition
    print(competition.add_contestant(bob))  # True
    print(competition.add_contestant(mari))  # False
    print(competition.add_contestant(kiur))  # True

    #  Add judge to competition
    print(competition.add_judge(judge1))  # False
    print(competition.add_judge(judge2))  # True

    print(competition.create_order_of_performances())
    # [Kiur Norman, Bob Ernest]

    print(competition.perform_song_rankings())
    # {Best day ever, style: rock: 100, Kinda normal, style: pop: 52}

    print(competition.get_suitable_genres())  # ['pop', 'rock']

    print(competition.get_contestants())  # [Bob Ernest, Kiur Norman]

    print(competition.get_judges())  # [Emili]

    print(competition.get_judges_rankings_in_order())
    # [Best day ever, style: rock, Kinda normal, style: pop]

    print(competition.get_winner())  # Best day ever, style: rock
