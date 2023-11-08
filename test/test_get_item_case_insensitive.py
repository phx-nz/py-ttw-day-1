import kata


def test_single_match():
    """
    Using :py:func:`kata.get_item_case_insensitive` to get a value whose key is a
    case-insensitive match for the search value.
    """
    characters = {
        "indy": "protagonist",
        "marion": "g*dd*mn partner",
        "sallah": "sidekick",
    }

    assert kata.get_item_case_insensitive(characters, "INDY") == "protagonist"


def test_multiple_possible_matches():
    """
    If there are multiple possible matches, only the first one is returned.
    """
    phrases = {
        "hello world": "speak up",
        "Hello World": "no need to be so formal",
        "Hello world": "well why didn't you say so",
    }

    assert kata.get_item_case_insensitive(phrases, "HELLO WORLD") == "speak up"


def test_exact_match_preferred():
    """
    If one of the keys is an exact match for the search value, that item's value is
    returned, even if there are case-insensitive matches that appear earlier in the
    dict.
    """
    phrases = {
        "hello world": "speak up",
        "Hello World": "no need to be so formal",
        "HELLO WORLD": "stop shouting",
        "Hello world": "well why didn't you say so",
    }

    assert kata.get_item_case_insensitive(phrases, "HELLO WORLD") == "stop shouting"
