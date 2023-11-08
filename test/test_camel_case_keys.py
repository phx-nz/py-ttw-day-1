import kata


def test_happy_path():
    """
    Using :py:func:`kata.camel_case_keys` to translate all the keys in a dict.
    """
    actual = kata.camel_case_keys(
        {
            "full_name": "Marcus Brody",
            "email_address": "mbrody@marshall.edu",
            "year_of_birth": 1878,
        }
    )

    assert actual == {
        "fullName": "Marcus Brody",
        "emailAddress": "mbrody@marshall.edu",
        "yearOfBirth": 1878,
    }


def test_already_camel_case():
    """
    If the dict keys are already camelCase, then it's a no-op.
    """
    expected = {
        "fullName": "Marcus Brody",
        "emailAddress": "mbrody@marshall.edu",
        "yearOfBirth": 1878,
    }

    assert kata.camel_case_keys(expected) == expected


def test_non_string_keys():
    """
    Any non-string keys are ignored.
    """
    actual = kata.camel_case_keys(
        {
            42: "answer",
            ("foo", "bar"): "baz",
            "control_group": "this one is not ignored",
        }
    )

    assert actual == {
        42: "answer",
        ("foo", "bar"): "baz",
        "controlGroup": "this one is not ignored",
    }
