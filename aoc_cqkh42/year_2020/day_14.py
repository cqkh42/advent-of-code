"""
Solutions for day 14 of 2020's Advent of Code

"""
import itertools
import re
from typing import Set

REGEX = re.compile(r'mem\[(\d+)] = (\d+)')


def _replace_floater(address) -> Set[str]:
    replaced = {
        address.replace('X', '0', 1), address.replace('X', '1', 1)
    }
    if address.count('X') == 1:
        return replaced
    else:
        new_ones = (_replace_floater(address) for address in replaced)
        return set(itertools.chain.from_iterable(new_ones))


def _mask_value(value, mask) -> int:
    value = f'{int(value):b}'.zfill(36)
    value = ''.join(v if m == 'X' else m for v, m in zip(value, mask))
    value = int(value, 2)
    return value


def _mask_address(address, mask) -> Set[int]:
    address = f'{int(address):b}'.zfill(36)
    address = ''.join(m if m != '0' else a for a, m in zip(address, mask))
    addresses = _replace_floater(address)
    return {int(address, 2) for address in addresses}


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
    memory = {}
    mask = None
    for row in data.split('\n'):
        if row.startswith('mask'):
            mask = row.split(' = ')[1]
        else:
            target, value = REGEX.match(row).groups()
            value = _mask_value(value, mask)
            memory[target] = value
    return sum(memory.values())


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
    memory = {}
    mask = None
    for row in data.split('\n'):
        if row.startswith('mask'):
            mask = row.split(' = ')[1]
        else:
            target, value = REGEX.match(row).groups()
            addresses = _mask_address(target, mask)
            for address in addresses:
                memory[address] = int(value)
    return sum(memory.values())
