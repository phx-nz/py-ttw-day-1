import kata


def test_happy_path():
    """
    Using :py:func:`kata.snake_case_keys` to translate all the keys in a dict.
    """
    actual = kata.snake_case_keys(
        {
            "fullName": "Henry Jones, Jr",
            "emailAddress": "hjones@marshall.edu",
            "yearOfBirth": 1899,
        }
    )

    assert actual == {
        "full_name": "Henry Jones, Jr",
        "email_address": "hjones@marshall.edu",
        "year_of_birth": 1899,
    }


def test_already_snake_case():
    """
    If all of the keys are already snake_case, then it's a no-op.
    """
    expected = {
        "full_name": "Henry Jones, Jr",
        "email_address": "hjones@marshall.edu",
        "year_of_birth": 1899,
    }

    assert kata.snake_case_keys(expected) == expected


def test_non_string_keys():
    """
    Any non-string keys are ignored.
    """
    actual = kata.snake_case_keys(
        {
            42: "answer",
            ("foo", "bar"): "baz",
            "controlGroup": "this one is not ignored",
        }
    )

    assert actual == {
        42: "answer",
        ("foo", "bar"): "baz",
        "control_group": "this one is not ignored",
    }
