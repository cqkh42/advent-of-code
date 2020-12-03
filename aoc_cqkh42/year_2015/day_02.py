import itertools
import math


class _Present:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    @property
    def corners(self):
        return itertools.combinations((self.x, self.y, self.z), 2)

    def paper(self):
        sides = [math.prod(corner) for corner in self.corners]
        return min(sides) + sum(sides)*2

    def ribbon(self):
        perms = (sum(corner) for corner in self.corners)
        return min(perms)*2 + math.prod((self.x, self.y, self.z))


def part_a(data):
    presents = data.split('\n')
    presents = (_Present(*data.split('x')) for data in presents)
    return sum(present.paper() for present in presents)


def part_b(data, **_):
    presents = data.split('\n')
    presents = (_Present(*data.split('x')) for data in presents)
    return sum(present.ribbon() for present in presents)
