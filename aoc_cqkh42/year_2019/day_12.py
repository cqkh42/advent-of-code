import math
import re

from aoc_cqkh42.helpers.base_solution import BaseSolution

_coords = ["x", "y", "z"]

#todo coords
class Planet:
    def __init__(self, positions):
        self.positions = dict(zip(_coords, positions))
        self.velocities = dict(zip(_coords, (0, 0, 0)))

    def pos(self):
        return self.positions["x"], self.positions["y"], self.positions["z"]

    def vel(self):
        return (
            self.velocities["x"], self.velocities["y"], self.velocities["z"])

    def pot(self):
        values = self.pos()
        absolutes = [abs(val) for val in values]
        return sum(absolutes)

    def kin(self):
        values = self.vel()
        absolutes = [abs(val) for val in values]
        return sum(absolutes)


def list_to_planets(list_):
    regex = re.compile("(?P<x>-{0,1}\\d+).+?(?P<y>-{0,1}\\d+).+?(?P<z>-{0,1}\\d+)")
    planets = [re.search(regex, line).groups() for line in list_]
    coords = [[int(coord) for coord in planet] for planet in planets]
    planets = [Planet(coord) for coord in coords]
    return planets


import itertools


def run_step(planets, axis):
    pairs = itertools.combinations(planets, 2)
    for planet_a, planet_b in pairs:
        if planet_a.positions[axis] == planet_b.positions[axis]:
            continue
        bool_val = planet_a.positions[axis] > planet_b.positions[axis]
        to_add = (-1) ** (1+bool_val)

        planet_a.velocities[axis] -= to_add
        planet_b.velocities[axis] += to_add

    for planet in planets:
        planet.positions[axis] += planet.velocities[axis]
    return planets


def run_steps(planets, steps):
    for _ in range(steps):
        for axis in ["x", "y", "z"]:
            planets = run_step(planets, axis)
    return planets


def find_cycle_point(planets, axis):
    initial_locations = tuple(planet.positions[axis] for planet in planets)
    convergence_point = 0
    while True:
        convergence_point += 1
        planets = run_step(planets, axis)
        locations = tuple(planet.positions[axis] for planet in planets)
        velocities = tuple(planet.velocities[axis] for planet in planets)
        if locations == initial_locations and not any(velocities):
            return convergence_point
    return cycle_points


from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=1_000_000)
def prime_factorize(num):
    factors = defaultdict(int)
    while num >= 2:
        until = int(num**0.5) + 1
        for factor in range(2, until):
            if not num % factor:
                factors[factor] += 1
                break
        else:
            factors[num] += 1
            return factors
        num //= factor


class Solution(BaseSolution):
    def part_a(self):
        planets = list_to_planets(self.lines)
        results = run_steps(planets, 1000)
        result = sum([planet.pot() * planet.kin() for planet in results])
        return result

    def part_b(self):
        planets = list_to_planets(self.lines)
        x = find_cycle_point(planets, "x")
        y = find_cycle_point(planets, "y")
        z = find_cycle_point(planets, "z")

        x = prime_factorize(x)
        y = prime_factorize(y)
        z = prime_factorize(z)

        first = {}
        first_vals = set(x)
        first_vals.update(y)
        first_vals.update(z)
        for value in first_vals:
            first[value] = max(x.get(value, 1), y.get(value, 1),
                               z.get(value, 1))
        zz = [k ** v for k, v in first.items()]
        return math.prod(zz)
