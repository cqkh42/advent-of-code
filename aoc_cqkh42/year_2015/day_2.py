import itertools
import math


class Present:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def paper(self):
        sides = [(self.x * self.y), (self.x * self.z), (self.y * self.z)]
        return min(sides) + sum(sides)*2

    def ribbon(self):
        perms = ((self.x + self.y), self.x + self.z, self.y + self.z)
        return min(perms)*2 + (self.x * self.y * self.z)


def part_a(data):
    presents = data.split('\n')
    presents = (Present(*data.split('x')) for data in presents)
    return sum(present.paper() for present in presents)


def part_b(data, **_):
    presents = data.split('\n')
    presents = (Present(*data.split('x')) for data in presents)
    return sum(present.ribbon() for present in presents)
