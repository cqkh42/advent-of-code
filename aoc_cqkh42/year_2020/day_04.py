"""
Solutions for day 4 of 2020's Advent of Code

"""
import re

KEY_VALUE_REGEX = re.compile(r'(\w+):([#a-z0-9]+)\s?')
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
    test_functions = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passport_dicts = (
        dict(KEY_VALUE_REGEX.findall(passport))
        for passport in data.split('\n\n')
    )
    complete_passports = (
        test_functions.issubset(passport) for passport in passport_dicts
    )
    return sum(complete_passports)


def part_b(data, **_) -> int:
    test_functions = {
        'byr': _valid_byr,
        'iyr': _valid_iyr,
        'eyr': _valid_eyr,
        'hgt': _valid_hgt,
        'hcl': _valid_hcl,
        'ecl': _valid_ecl,
        'pid': _valid_pid,
    }
    passport_dicts = (
        dict(KEY_VALUE_REGEX.findall(passport))
        for passport in data.split('\n\n')
    )
    valid_passports = (
        all(test_functions[attr](passport[attr]) for attr in test_functions)
        for passport in passport_dicts
        if set(test_functions).issubset(passport)
    )
    return sum(valid_passports)
