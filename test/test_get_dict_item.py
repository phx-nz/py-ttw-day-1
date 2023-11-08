import kata


def test_get_dict_item_exists():
    """Extracting an existing value with :py:func:`kata.get_dict_item`"""
    expected = "bar"

    actual = kata.get_dict_item(
        {"foo": expected, "baz": "luhrmann"},
        "foo",
        "default value",
    )

    assert actual == expected


def test_get_dict_item_not_exists():
    """
    Trying to access a nonexistent key with :py:func:`kata.get_dict_item`, so it returns
    the default value instead.
    """
    default = "default value"

    actual = kata.get_dict_item(
        {"foo": "bar", "baz": "luhrmann"},
        "something completely different",
        default,
    )

    assert actual == default
