"""
Solutions for day 4 of 2020's Advent of Code

"""
import re

import parse

HCL_REGEX = re.compile(r'#[0-9a-f]{6}')
PID_REGEX = re.compile(r'\d{9}\b')


def _valid_byr(year) -> bool:
    try:
        return 1920 <= int(year) <= 2002
    except ValueError:
        return False


def _valid_iyr(year) -> bool:
    return 2010 <= int(year) <= 2020


def _valid_eyr(year) -> bool:
    return 2020 <= int(year) <= 2030


def _valid_hgt(height) -> bool:
    if height.endswith('cm'):
        return 150 <= int(height[:-2]) <= 193
    elif height.endswith('in'):
        return 59 <= int(height[:-2]) <= 76
    return False


def _valid_hcl(color) -> bool:
    return bool(HCL_REGEX.match(color))


def _valid_ecl(color) -> bool:
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def _valid_pid(pid) -> bool:
    return bool(PID_REGEX.match(pid))


class _Passport:
    def __init__(self, passport):
        self.rows = dict(parse.findall(r'{:S}:{:S}', passport))

    @property
    def complete(self):
        return set(self._test_functions).issubset(self.rows)

    def _test_attribute(self, attribute):
        func = self._test_functions[attribute]
        return func(self.rows[attribute])

    @property
    def valid(self):
        if not self.complete:
            return False
        return all(self._test_attribute(attr) for attr in self._test_functions)

    _test_functions = {
        'byr': _valid_byr,
        'iyr': _valid_iyr,
        'eyr': _valid_eyr,
        'hgt': _valid_hgt,
        'hcl': _valid_hcl,
        'ecl': _valid_ecl,
        'pid': _valid_pid,
    }


def part_a(data) -> int:
    """
    Solution for part a

    Parameters
    ----------
    data: str

    Returns
    -------
    answer: int

    """
    passports = (_Passport(row) for row in data.split('\n\n'))
    complete = (passport.complete for passport in passports)
    return sum(complete)


def part_b(data, **_) -> int:
    """
    Solution for part b

    Parameters
    ----------
    data: str

    Returns
    -------
    answer: int

    """
    passports = (_Passport(row) for row in data.split('\n\n'))
    valid = (passport.valid for passport in passports)
    return sum(valid)
