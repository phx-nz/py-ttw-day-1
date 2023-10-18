import re
from datetime import date, datetime
from typing import Any, Callable

__all__ = [
    "array_filter",
    "array_map",
    "camel_case_keys",
    "dates_and_times",
    "get_dict_item",
    "interpolation",
    "slice_first_half",
    "slice_reverse_order",
    "snake_case_keys",
    "statements_and_expressions",
]


def statements_and_expressions():
    def is_meme_worthy(power_level: int) -> bool:
        """There's no way that can be right! Can it?"""
        return power_level > 9000

    some_value: int = 42
    some_value += 8_959

    generic_text: str = "Kia ora te ao!"

    result: bool = is_meme_worthy(some_value)

    return some_value, generic_text, result


def interpolation():
    name, adj = "Alice", "nice"

    return f"Hi {name}, {adj} to see you!"


def dates_and_times():
    einstein = date(1879, 3, 14)
    now_ish = datetime(2023, 10, 17, 12, 19, 32)

    einstein_age = now_ish.date() - einstein

    return einstein_age.days // 365


def slice_first_half():
    some_strings: list[str] = ["foo", "bar", "baz", "luhrmann"]

    return some_strings[:2]


def slice_reverse_order():
    some_strings: list[str] = ["foo", "bar", "baz", "luhrmann"]

    return some_strings[::-1]


def get_dict_item(the_dict: dict, key: str, default: Any) -> Any:
    """
    Given a dict, a key, and a default value, attempts to return the item from
    the dict with the matching key.

    If the key does not exist in the dict, the default value is returned
    instead.
    """
    try:
        return value[key]
    except KeyError:
        return default


def array_map(array: list, fn: Callable) -> list:
    """
    Given a list of items and a function, returns a new list containing the
    results of calling the function on each item in the original list.

    In other words, port the ``Array.prototype.map()`` method from TypeScript
    into Python (:
    """
    return [fn(item) for item in array]


def array_filter(array: list, fn: Callable) -> list:
    """
    Given a list of items and a function, calls the function on each item in
    the list and returns a new list containing only the items where the function
    returned True.

    In other words, port the ``Array.prototype.filter()`` method from TypeScript
    into Python (:
    """
    return [item for item in array if fn(item) is True]


def snake_case_keys(values: dict) -> dict:
    """
    Converts the keys in a dict from camelCase to snake_case.

    Hint: https://docs.python.org/3/library/re.html#re.sub
    """
    # https://regex101.com/r/4ln1F9/1
    camel_case_re = r"(?<=[a-z])[A-Z]"
    return {
        re.sub(camel_case_re, lambda match: f"_{match[0].lower()}", key): value
        for key, value in values.items()
    }


def camel_case_keys(values: dict) -> dict:
    """
    Converts the keys in a dict from snake_case to camelCase.
    """
    # https://regex101.com/r/FZJ82P/1
    snake_case_re = r"_([a-z])"
    return {
        re.sub(snake_case_re, lambda match: match[1].upper(), key): value
        for key, value in values.items()
    }
