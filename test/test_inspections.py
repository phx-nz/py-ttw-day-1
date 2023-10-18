from kata import inspections


def test_statements_and_expressions():
    assert inspections.statements_and_expressions() == (9_001, "Kia ora te ao!", True)


def test_interpolation():
    assert inspections.interpolation() == "Hi Alice, nice to see you!"


def test_dates_and_times():
    assert inspections.dates_and_times() == 144


def test_first_half():
    assert inspections.slice_first_half() == ["foo", "bar"]


def test_reverse_slice():
    assert inspections.slice_reverse_order() == ["luhrmann", "baz", "bar", "foo"]


def test_get_dict_item_exists():
    """Extracting an existing value with ``get_dict_item()``"""
    expected = "bar"
    actual = inspections.get_dict_item(
        {"foo": expected, "baz": "luhrmann"},
        "foo",
        "default value",
    )

    assert actual == expected


def test_get_dict_item_not_exists():
    """
    Trying to access a nonexistent key with ``get_dict_item()``, so it returns
    the default value instead.
    """
    expected = "default value"
    actual = inspections.get_dict_item(
        {"foo": "bar", "baz": "luhrmann"},
        "something completely different",
        expected,
    )

    assert actual == expected


def test_array_map():
    expected = [1, 4, 9, 16, 25]
    squares = inspections.array_map([1, 2, 3, 4, 5], lambda n: n**2)

    assert squares == expected


def test_array_filter():
    expected = [1, 3, 5, 7, 9]
    odd_numbers = inspections.array_filter([*range(11)], lambda n: n % 2 == 1)

    assert odd_numbers == expected


def test_snake_case_keys():
    expected = {
        "full_name": "Henry Jones, Jr",
        "email_address": "hjones@marshall.edu",
        "year_of_birth": 1899,
    }

    actual = inspections.snake_case_keys(
        {
            "fullName": "Henry Jones, Jr",
            "emailAddress": "hjones@marshall.edu",
            "yearOfBirth": 1899,
        }
    )

    assert actual == expected


def test_camel_case_keys():
    expected = {
        "fullName": "Marcus Brody",
        "emailAddress": "mbrody@marshall.edu",
        "yearOfBirth": 1878,
    }

    actual = inspections.camel_case_keys(
        {
            "full_name": "Marcus Brody",
            "email_address": "mbrody@marshall.edu",
            "year_of_birth": 1878,
        }
    )

    assert actual == expected
