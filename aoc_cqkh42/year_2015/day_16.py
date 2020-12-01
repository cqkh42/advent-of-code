import re

def part_a(data):
    sues = {}
    for sue in data.split('\n'):
        sue, *bits = re.search('Sue (\d+): (.*?): (\d+), (.*?): (\d+), (.*?): (\d+)', sue).groups()
        sues[sue] = dict(zip(bits[::2], [int(num) for num in bits[1::2]]))

    auntie = {
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

    return [sue for sue in sues if all(item == auntie[key] for key, item in sues[sue].items())][0]


def part_b(data, **_):
    sues = {}
    for sue in data.split('\n'):
        sue, *bits = re.search('Sue (\d+): (.*?): (\d+), (.*?): (\d+), (.*?): (\d+)', sue).groups()
        sues[sue] = dict(zip(bits[::2], [int(num) for num in bits[1::2]]))

    good_sues = [
        sue for sue in sues if
        sues[sue].get('children', 3) == 3 and
        sues[sue].get('cats', 8) > 7 and
        sues[sue].get('samoyeds', 2) == 2 and
        sues[sue].get('pomeranians', 2) < 3 and
        sues[sue].get('akitas', 0) == 0 and
        sues[sue].get('vizslas', 0) == 0 and
        sues[sue].get('goldfish', 4) < 5 and
        sues[sue].get('trees', 4) > 3 and
        sues[sue].get('cars', 2) == 2 and
        sues[sue].get('perfumes', 1) == 1
    ]
    return good_sues[0]
