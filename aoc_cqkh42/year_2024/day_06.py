import itertools
from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    directions = itertools.cycle('ESWN')
    current_direction = 'N'
    current_location = None

    def _parse(self: Self) -> Any:
        for y_index, line in enumerate(self.lines):
            if '^' in line:
                self.current_location = (line.index('^'), y_index)
                return
    def move(self):
        x, y = self.current_location
        if self.current_direction == 'N':
            new_x, new_y = x, y-1
        elif self.current_direction == 'E':
            new_x, new_y = x+1, y
        elif self.current_direction == 'S':
            new_x, new_y = x, y+1
        elif self.current_direction == 'W':
            new_x, new_y = x-1, y
        if self.lines[new_y][new_x] == '#':
            self.current_direction = next(self.directions)
        else:
            self.current_location = (new_x, new_y)


    def part_a(self):
        locations = set()
        while True:
            try:
                locations.add(self.current_location)
                self.move()
            except IndexError:
                return len(locations)

    def part_b(self):
        hash_locations = set()
        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                if value == '#':
                    hash_locations.add((x_index, y_index))

        # to find the missing top left corner,
        # you first need the bottom right corner
        # and one which is to the right and one which is above
        possibles = set()
        ps = itertools.permutations(hash_locations, 3)
        for a, b, c in ps:
            if c[0] == a[0] + 1 and b[1] == a[1] - 1: # missing is TL
                possibles.add((b[0], c[1]-1))
            elif b[0] == a[0] and c[1] == a[1]+1:  #missing is TR
                possibles.add((c[0]+1, b[1]+1))
            elif b[1] == a[1]+1 and c[0] == a[0]: # missnig is BR
                possibles.add((b[0]-1, c[1]+1))
            elif a[0] == b[0]+1 and a[1] == c[1]+1:  # missing is BL
                possibles.add((c[0], b[1]-1))
        print(possibles)

        # valid_ps = [a for a,b,c in ps if b[0] == a[0]+1 and c[1] == a[1]-1]
        # print(valid_ps)





if __name__ == "__main__":
    submit_answers(Solution,6, 2024)
