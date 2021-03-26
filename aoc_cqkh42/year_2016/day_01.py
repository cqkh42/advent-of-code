from collections import defaultdict

import parse
from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return list(parse.findall(r'{:l}{:d}', self.data))

    compass = ('N', 'E', 'S', 'W')

    def direction(self, current, turn):
        incr = 1 if turn == 'R' else -1
        c_index = self.compass.index(current)
        new = (c_index + incr) % 4
        return self.compass[new]


    def part_a(self):
        travelled = defaultdict(int)

        current_direction = 'N'

        for change, distance in self.parsed_data:
            current_direction = self.direction(current_direction, change)
            travelled[current_direction] += distance

        return abs(travelled['E'] - travelled['W']) + abs(
            travelled['N'] - travelled['S'])

    def part_b(self):
        visited = {(0, 0)}
        travelled = defaultdict(int)
        current_direction = 'N'

        for change, distance in self.parsed_data:
            current_direction = self.direction(current_direction, change)
            for step in range(distance):
                travelled[current_direction] += 1
                at = ((travelled['E'] - travelled['W']),
                      (travelled['N'] - travelled['S']))
                if at in visited:
                    return abs(at[0]) + abs(at[1])
                visited.add(at)
