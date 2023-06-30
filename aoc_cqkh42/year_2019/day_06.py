from collections import defaultdict

from aoc_cqkh42.helpers.base_solution import BaseSolution


def count_orbital_injections(object_1, object_2, orbits):
    orbits = dict(reversed(orbit.split(")")) for orbit in orbits)
    visited = defaultdict(dict)

    for planet in [object_1, object_2]:
        distance = -1
        planet_trace = planet
        while planet_trace != "COM":
            planet_trace = orbits[planet_trace]
            distance += 1
            visited[planet][planet_trace] = distance
    common_planets = set(
        visited[object_1]
    ).intersection(visited[object_2])
    distances = [
        visited[object_1][planet] + visited[object_2][planet]
        for planet in common_planets
    ]
    return min(distances)

def count_orbits(orbits):
    orbits = dict(reversed(orbit.split(")")) for orbit in orbits)
    planets = {*orbits, *orbits.values()}

    distances = {}

    for planet in planets:
        planet_trace = planet
        counter = 0
        while planet_trace != "COM":
            planet_trace = orbits[planet_trace]
            counter += 1
        distances[planet] = counter

    return sum(distances.values())


class Solution(BaseSolution):
    def part_a(self):
        return count_orbits(self.lines)

    def part_b(self):
        return count_orbital_injections("YOU", "SAN", self.lines)
