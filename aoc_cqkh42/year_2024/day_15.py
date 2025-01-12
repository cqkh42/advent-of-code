import copy

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def move(grid, location, x, y):
    current_x, current_y = location
    new_location = (current_x + x, current_y+y)
    if grid[new_location] == '#':
        raise IndexError
    elif grid[new_location] == '.':
        grid[new_location] = grid[location]
        grid[location] = '.'
        return grid
    elif grid[new_location] == 'O':
        new_grid = move(grid, new_location,x,y)
        return move(new_grid, location, x, y)

class Solution(BaseSolution):
    def part_a(self):
        grid_lines = []
        directions = []
        for line in self.lines:
            if line.startswith('#'):
                grid_lines.append(line)
            if not line:
                continue
            elif line[0] in '<>v^':
                directions.extend(line)

        grid = {}
        for y_index, row in enumerate(grid_lines):
            for x_index, val in enumerate(row):
                if val == '@':
                    current = (x_index, y_index)
                grid[(x_index, y_index)] = val

        mapper = {
            '<': (-1, 0),
            '>': (1, 0),
            'v': (0, 1),
            '^': (0, -1)
        }
        for direction in directions:
            x, y = mapper[direction]
            try:
                grid = move(grid, current, x, y)
                current = current[0] + x, current[1]+y
            except IndexError:
                continue

        total = 0
        for (x, y), v in grid.items():
            if v == 'O':
                total += 100*y
                total += x
                # print((x, y))
        return total


    def part_b(self):
        return


if __name__ == "__main__":
    submit_answers(Solution,15, 2024)
