import kata


def test_square():
    """
    Using :py:func:`kata.array_map` to square all of the values in an array.
    """
    squares = kata.array_map([1, 2, 3, 4, 5], lambda n: n**2)

    assert squares == [1, 4, 9, 16, 25]
