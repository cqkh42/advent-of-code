import pytest

from aoc_cqkh42.year_2017 import day_04


@pytest.mark.parametrize(
    "data, answer",
    [
        ("aa bb cc dd ee", True),
        ("aa bb cc dd aa", False),
        ("aa bb cc dd aaa", True),
    ],
)
def test__valid_passphrase_a(data, answer):
    assert day_04._valid_passphrase_a(data) == answer


@pytest.mark.parametrize(
    "data, answer",
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf abj", True),
        ("iiii oiii ooii oooi oooo", True),
        ("oiii ioii iioi iiio", False),
    ],
)
def test__valid_passphrase_b(data, answer):
    assert day_04._valid_passphrase_b(data) == answer
