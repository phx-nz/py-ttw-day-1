import kata


def test_odds():
    """
    Using :py:func:`kata.array_filter` to pick out just the odd numbers in an array.
    """
    odd_numbers = kata.array_filter([*range(11)], lambda n: n % 2 == 1)

    assert odd_numbers == [1, 3, 5, 7, 9]
