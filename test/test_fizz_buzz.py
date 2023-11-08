import kata


def test_happy_path():
    """
    Congratulations, you've passed the first technical interview!
    """
    assert kata.fizz_buzz(21) == [
        "FizzBuzz",  # 0 is (technically) divisible by both 3 and 5
        "",  # 1 not divisible by 3 nor 5
        "",  # 2 not divisible by 3 nor 5
        "Fizz",  # 3 is divisible by 3
        "",  # 4 not divisible by 3 nor 5
        "Buzz",  # 5 is divisible by 5
        "Fizz",  # 6 is divisible by 3
        "",  # 7 not divisible by 3 nor 5
        "",  # 8 not divisible by 3 nor 5
        "Fizz",  # 9 is divisible by 3
        "Buzz",  # 10 is divisible by 5
        "",  # 11 not divisible by 3 nor 5
        "Fizz",  # 12 is divisible by 3
        "",  # 13 not divisible by 3 nor 5
        "",  # 14 not divisible by 3 nor 5
        "FizzBuzz",  # 15 divisible by both 3 and 5
        "",  # 16 not divisible by 3 nor 5
        "",  # 17 not divisible by 3 nor 5
        "Fizz",  # 18 is divisible by 3
        "",  # 19 not divisible by 3 nor 5
        "Buzz",  # 20 is divisible by 5
    ]
