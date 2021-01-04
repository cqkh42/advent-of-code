import numpy as np


def part_a(data):
    target = int(data)
    n = 1000000
    houses = np.ones(n)
    houses *= 10
    for elf in range(2, n):
        houses[elf::elf] += (elf * 10)
    return np.argmax(houses > target)


def part_b(data, **_):
    target = int(data)
    n = 1000000
    houses = np.ones(n)
    houses *= 11
    for elf in range(2, n):
        houses[elf:(elf*50)+1:elf] += (elf * 11)
    return np.argmax(houses > target)
