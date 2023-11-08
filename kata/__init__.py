import re
import typing

__all__ = [
    "array_filter",
    "array_map",
    "camel_case_keys",
    "fizz_buzz",
    "get_dict_item",
    "get_item_case_insensitive",
    "snake_case_keys",
]


def fizz_buzz(count: int) -> list[str]:
    """
    Returns an array with ``count`` items where each item is one of the following:

    - If the item's index is divisible by 3: "Fizz"
    - If the item's index is divisible by 5: "Buzz"
    - If the item's index is divisible by 3 and 5: "FizzBuzz"
    - If the item's index is not divisible by 3 nor 5: ""
    """
    if count < 1:
        raise ValueError("Count must be >= 1")

    return [
        ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
        for i in range(count)
    ]


def get_dict_item(the_dict: dict, key: str, default: typing.Any) -> typing.Any:
    """
    Given a dict, a key, and a default value, attempts to return the item from
    the dict with the matching key.

    If the key does not exist in the dict, the default value is returned
    instead.
    """
    try:
        return the_dict[key]
    except KeyError:
        return default


def array_map(array: list, fn: typing.Callable) -> list:
    """
    Given a list of items and a function, returns a new list containing the
    results of calling the function on each item in the original list.

    In other words, port the ``Array.prototype.map()`` method from TypeScript
    into Python (:
    """
    return [fn(item) for item in array]


def array_filter(array: list, fn: typing.Callable) -> list:
    """
    Given a list of items and a function, calls the function on each item in
    the list and returns a new list containing only the items where the function
    returned True.

    In other words, port the ``Array.prototype.filter()`` method from TypeScript
    into Python (:
    """
    return [item for item in array if fn(item)]


def snake_case_keys(values: dict) -> dict:
    """
    Converts the keys in a dict from camelCase to snake_case.

    Hint: https://docs.python.org/3/library/re.html#re.sub
    """
    # https://regex101.com/r/4ln1F9/1
    camel_case_re = r"(?<=[a-z])[A-Z]"
    return {
        (
            re.sub(camel_case_re, lambda groups: f"_{groups[0].lower()}", key)
            if isinstance(key, str)
            else key
        ): value
        for key, value in values.items()
    }


def camel_case_keys(values: dict) -> dict:
    """
    Converts the keys in a dict from snake_case to camelCase.
    """
    # https://regex101.com/r/FZJ82P/1
    snake_case_re = r"_([a-z])"
    return {
        (
            re.sub(snake_case_re, lambda groups: groups[1].upper(), key)
            if isinstance(key, str)
            else key
        ): value
        for key, value in values.items()
    }


def get_item_case_insensitive(
    the_dict: dict[str, typing.Any], search_key: str
) -> typing.Any:
    """
    Iterates through ``the_dict`` until it finds the first item whose key is a
    case-insensitive match for ``key``.

    All keys in ``the_dict`` are strings.

    :raises: KeyError if no matches are found.
    """
    try:
        return the_dict[search_key]
    except KeyError:
        ci_search_key = search_key.lower()

        for key, value in the_dict.items():
            if key.lower() == ci_search_key:
                return value

        raise KeyError(search_key)
