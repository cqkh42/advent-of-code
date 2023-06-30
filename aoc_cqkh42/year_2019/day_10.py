import math

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse_data(self):
        asteroids = set()
        for y_index, row in enumerate(self.lines):
            for x_index, item in enumerate(row):
                if item == '#':
                    asteroids.add((x_index, y_index))
        return asteroids

    def _asteroids_in_sight(self, origin):
        in_sight = {}
        for asteroid in self.parsed_data:
            angle = _angle(origin, asteroid)
            if angle not in in_sight:
                in_sight[angle] = asteroid
            else:
                in_sight[angle] = min(
                    in_sight[angle], asteroid,
                    key=lambda asteroid: (asteroid[0] - origin[0]) ** 2 + (
                                asteroid[1] - origin[1]) ** 2)
        in_sight = set(in_sight.values())
        in_sight.remove(origin)
        return in_sight

    def part_a(self):
        in_sight = (self._asteroids_in_sight(origin) for origin in
                    self.parsed_data)
        counts = (len(asteroids) for asteroids in in_sight)
        return max(counts)

    def part_b(self):
        in_sight = {
            origin: self._asteroids_in_sight(origin) for origin in
            self.parsed_data
        }
        centre = max(in_sight, key=lambda key: len(in_sight[key]))
        in_sight = in_sight[centre]
        to_destroy = 200
        if len(in_sight) <= to_destroy:
            to_destroy -= len(in_sight)
            in_sight = self._asteroids_in_sight(centre)
        else:
            in_sight = sorted(in_sight, key=lambda x: _angle(centre, x))
            return (in_sight[to_destroy - 1][0] * 100) + \
                in_sight[to_destroy - 1][1]
        return False


def _angle(origin, other):
    if other == origin:
        return -180
    x = other[0] - origin[0]
    y = other[1] - origin[1]
    angle = math.atan2(x, y) * 180 / math.pi
    return 180 - angle
