import re

REGEX = re.compile(r'Sue \d+: (.*?): (\d+), (.*?): (\d+), (.*?): (\d+)')
# noinspection SpellCheckingInspection
AUNTIE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def _parse_sues(data):
    sue_list = (REGEX.search(sue).groups() for sue in data.split('\n'))
    sue_list = [
        dict(zip(bits[::2], [int(num) for num in bits[1::2]]))
        for bits in sue_list
    ]
    return sue_list


# noinspection SpellCheckingInspection
def _good_sue(sue):
    equals = ['children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes']
    equals = all(sue[attr] == AUNTIE[attr] for attr in equals if attr in sue)

    gt = ['cats', 'trees']
    gt = all(sue[attr] > AUNTIE[attr] for attr in gt if attr in sue)

    lt = ['pomeranians', 'goldfish']
    lt = all(sue[attr] < AUNTIE[attr] for attr in lt if attr in sue)
    return equals and gt and lt


def part_a(data):
    sues = _parse_sues(data)
    sue_is_good = [all(sue[key] == AUNTIE[key] for key in sue) for sue in sues]
    return sue_is_good.index(True) + 1


def part_b(data, **_):
    sues = _parse_sues(data)
    is_good_sue = [_good_sue(sue) for sue in sues]
    return is_good_sue.index(True) + 1
