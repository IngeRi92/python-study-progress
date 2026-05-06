"""Regex, yay."""
import re


def find_a_triplets(string):
    """Find letter a triplets."""
    return re.findall(r"aaa", string)


def find_words(string):
    """Find words consiting of one capital letter and atleast one non-capital letter."""
    return re.findall(r"[A-ZÕÄÖÜ][a-zõäöü]+", string)


def find_address(string):
    """Find address consisting of street name with one word, a space, and a house number."""
    return re.findall(r"[A-ZÕÄÖÜ][a-zõäöü]+ \d+", string)


def find_birth_year_from_21st_century(string):
    """
    Find all birth years from 2001.

    All number combinations are seperated from each other with space.
    Only 4 digit numbers accepted.
    If there is a 5 digit not accepted.
    """
    return re.findall(r"\b(200[1-9]|20[1-9][0-9]|2100)\b", string)


def find_sentences(string):
    """
    Find sentences from string.

    Sentences start with a capital letter.
    Words have whitespaces, commas, colons or dashes in between.
    Words end with a punctuation.
    """
    pattern = r"[A-ZÕÄÖÜ][^.!?]*[.!?]+"
    return re.findall(pattern, string)


def capture_month_year_group(string):
    """
    Capture groups of month and year put together and a group of year separately.

    Months are represented as short 3-letter forms:
    January - Jan
    February - Feb
    March - Mar
    April - Apr
    etc...

    Jul 2003 - (Jul 2003) and (2003) as groups.
    March 2004 would not capture anything.
    """
    pattern = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4})"
    return list(re.finditer(pattern, string))


def born_month_and_year(string):
    """
    Return a list where each element is a sentence "Born in [month] in [year].".

    From string ("Jul 2003 Jan 2004 April 2005") return ["Born in Jul in 2003.", "Born in Jan in 2004."]
    Use groups.
    """
    pattern = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4})"
    matches = re.findall(pattern, string)
    return [f"Born in {m} in {y}." for m, y in matches]


def search_for_id_code(string):
    """
    Return a string with ID code if found. If ID code not found, return string with saying none.

    ID code must be from this century, so it must start with a 5 or 6.
    The second and third number are years, so in range 01 - 23.
    Fourth and fifth are the month numbers, so in range 01 - 12.
    Sixth and seventh are day numbers, so in range 01 - 31. NB! We will not check if it is
    February with more than 28 days.
    Last 4 digits can be anything.

    For example:
    From "ABCD50102034678efgh" it will take out 50102034678 and Return "Persons ID code is 50102034678.
    From "ABCD42503064578efgh" it will take nothing out, since year can't be 25 and Return "ID code cant be found.".
    NB! Use search.
    """
    pattern = (r"(5|6)(0[1-9]|1[0-9]|2[0-3])(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])(\d{4})")
    match = re.search(pattern, string)
    if match:
        return f"Persons ID code is {match.group(0)}."
    return "ID code can't be found."


if __name__ == '__main__':
    print(capture_month_year_group("Jul 2003 Jan 2004 April 2005"))
