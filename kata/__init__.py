import typing

__all__ = [
    "array_filter",
    "array_map",
    "camel_case_keys",
    "fizz_buzz",
    "get_dict_item",
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


def get_dict_item(the_dict: dict, key: str, default: typing.Any) -> typing.Any:
    """
    Given a dict, a key, and a default value, attempts to return the item from
    the dict with the matching key.

    If the key does not exist in the dict, the default value is returned
    instead.
    """
    pass


def array_map(array: list, fn: typing.Callable) -> list:
    """
    Given a list of items and a function, returns a new list containing the
    results of calling the function on each item in the original list.

    In other words, port the ``Array.prototype.map()`` method from TypeScript
    into Python (:
    """
    pass


def array_filter(array: list, fn: typing.Callable) -> list:
    """
    Given a list of items and a function, calls the function on each item in
    the list and returns a new list containing only the items where the function
    returned True.

    In other words, port the ``Array.prototype.filter()`` method from TypeScript
    into Python (:
    """
    pass


def snake_case_keys(values: dict) -> dict:
    """
    Converts the keys in a dict from camelCase to snake_case.

    Hint: https://docs.python.org/3/library/re.html#re.sub
    """
    # https://regex101.com/r/4ln1F9/1
    camel_case_re = r"(?<=[a-z])[A-Z]"
    pass


def camel_case_keys(values: dict) -> dict:
    """
    Converts the keys in a dict from snake_case to camelCase.
    """
    # https://regex101.com/r/FZJ82P/1
    snake_case_re = r"_([a-z])"
    pass
