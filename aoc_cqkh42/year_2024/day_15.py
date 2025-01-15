import copy
from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

mapper = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1)
}

def stretch_line(line):
    return line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')

class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        grid_lines = []
        directions = []
        for line in self.lines:
            if line.startswith('#'):
                grid_lines.append(line)
            if not line:
                continue
            elif line[0] in '<>v^':
                directions.extend(line)
        self.directions = directions

        return grid_lines

    def move(self, location, x, y):
        current_x, current_y = location
        new_location = (current_x + x, current_y + y)
        if self.grid[new_location] == '#':
            raise IndexError
        elif self.grid[new_location] == '.':
            self.grid[location], self.grid[new_location] = '.', self.grid[location]
        elif self.grid[new_location] == 'O':
            self.move(new_location, x, y)
            return self.move(location, x, y)

    def big_move(self, location, grid, x, y):
        grid = {k:v for k, v in grid.items()}
        return self.move_b(location, grid, x, y)

    def move_b(self, location, grid, x, y):
        current_x, current_y = location
        new_location = (current_x + x, current_y + y)
        if grid[new_location] == '#':
            raise IndexError

        elif grid[new_location] in '[]' and x != 0:
            self.move_b(new_location, grid, x, y)
            return self.move_b(location, grid, x, y)
        elif grid[new_location] == '[' and y != 0:
            self.move_b(new_location, grid, x, y)
            self.move_b((new_location[0]+1, new_location[1]), grid, x, y)
            return self.move_b(location, grid, x, y)
        elif grid[new_location] == ']' and y != 0:
            self.move_b(new_location, grid, x, y)
            self.move_b((new_location[0]-1, new_location[1]), grid, x, y)
            return self.move_b(location, grid, x, y)
        elif grid[new_location] == '.':
            grid[location], grid[new_location] = '.', grid[
                location]
        return grid

    def part_a(self):
        self.grid = {}
        for y_index, row in enumerate(self.parsed):
            for x_index, val in enumerate(row):
                if val == '@':
                    current = (x_index, y_index)
                self.grid[(x_index, y_index)] = val


        for direction in self.directions:
            x, y = mapper[direction]
            try:
                self.move(current, x, y)
                current = current[0] + x, current[1]+y
            except IndexError:
                continue

        return sum((x + 100*y) for (x, y), v in self.grid.items() if v == 'O')


    def part_b(self):
        new_lines = [stretch_line(line) for line in self.parsed]

        grid = {}
        for y_index, row in enumerate(new_lines):
            for x_index, val in enumerate(row):
                if val == '@':
                    current = (x_index, y_index)
                grid[(x_index, y_index)] = val

        for direction in self.directions:
            x, y = mapper[direction]
            try:
                grid = self.big_move(current, grid, x, y)
                current = current[0] + x, current[1]+y
            except IndexError:
                continue
        return sum(
            (x + 100 * y) for (x, y), v in grid.items() if v == '[')



if __name__ == "__main__":
    submit_answers(Solution,15, 2024)
