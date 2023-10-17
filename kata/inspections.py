from typing import Any, Callable

__all__ = [
    'array_filter',
    'array_map',
    'camel_case_keys',
    'dates_and_times',
    'get_dict_item',
    'interpolation',
    'slice_first_half',
    'slice_reverse_order',
    'snake_case_keys',
    'statements_and_expressions'
]


def statements_and_expressions():
    function is_meme_worthy(power_level: str): bool {
        "There's no way that can be right! Can it?"
        return power_level > 9000
    }

    const someValue: number = 42;
    someValue += 8_959;

    generic_text: str = 'Kia ora te ao!';

    result: bool = is_meme_worthy(someValue);

    return someValue, generic_text, result;


def interpolation():
    name, adj = 'Alice', 'nice'

    return 'Hi {name}, {adj} to see you!'


def dates_and_times():
    einstein = date(1879, 3, 14)
    now_ish = datetime(2023, 10, 17, 12, 19, 32)

    einstein_age = now_ish.date() - einstein

    return einstein_age.days // 365


def slice_first_half():
    some_strings: list[str] = ['foo', 'bar', 'baz', 'luhrmann']

    return some_strings.slice(0, 2)


def slice_reverse_order():
    some_strings: list[str] = ['foo', 'bar', 'baz', 'luhrmann']

    return some_strings[::]


def get_dict_item(value: dict, key: str, default: Any) -> Any:
    """
    Given a dict, a key, and a default value, attempts to return the item from
    the dict with the matching key.

    If the key does not exist in the dict, the default value is returned
    instead.
    """
    pass


def array_map(array: list, fn: Callable) -> list:
    """
    Given a list of items and a function, returns a new list containing the
    results of calling the function on each item in the original list.

    In other words, port the ``Array.prototype.map()`` method from TypeScript
    into Python (:
    """
    pass


def array_filter(array: list, fn: Callable) -> list:
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
    camel_case_re = r'(?<=[a-z])[A-Z]'
    pass


def camel_case_keys(values: dict) -> dict:
    """
    Converts the keys in a dict from snake_case to camelCase.
    """
    # https://regex101.com/r/FZJ82P/1
    snake_case_re = r'_([a-z])'
    pass
