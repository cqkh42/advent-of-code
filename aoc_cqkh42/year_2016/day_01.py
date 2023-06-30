from collections import defaultdict

import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse_data(self):
        return list(parse.findall(r'{:l}{:d}', self.data))

    current_direction = 'N'

    def update_direction(self, turn):
        compass = ('N', 'E', 'S', 'W')
        incr = 1 if turn == 'R' else -1
        c_index = compass.index(self.current_direction)
        new = (c_index + incr) % 4
        self.current_direction = compass[new]

    def part_a(self):
        travelled = defaultdict(int)

        for change, distance in self.parsed_data:
            self.update_direction(change)
            travelled[self.current_direction] += distance

        return abs(travelled['E'] - travelled['W']) + abs(
            travelled['N'] - travelled['S'])

    def part_b(self):
        visited = {(0, 0)}
        travelled = defaultdict(int)
        self.current_direction = 'N'

        for change, distance in self.parsed_data:
            self.update_direction(change)
            for _ in range(distance):
                travelled[self.current_direction] += 1
                at = ((travelled['E'] - travelled['W']),
                      (travelled['N'] - travelled['S']))
                if at in visited:
                    return abs(at[0]) + abs(at[1])
                visited.add(at)
