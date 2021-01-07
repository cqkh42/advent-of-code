import itertools


def part_a(data):
    holding = [row for row in data.split('\n') if '->' in row]
    lefts = {row.split()[0] for row in holding}
    rights = (row.split('-> ')[1] for row in holding)
    rights = [row.split(', ') for row in rights]
    rights = set(itertools.chain.from_iterable(rights))
    return lefts.difference(rights).pop()


def part_b(data, **_):
    return False