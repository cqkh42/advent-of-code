import itertools
from typing import Self, Any

import more_itertools
from isort.wrap_modes import vertical

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Maze:
    def __init__(self, maze):
        for y_index, line in enumerate(maze):
            if '^' in line:
                self.start_location = self.current_location = (line.index('^'), y_index)
        self.visited = set()
        self.current_direction = 'N'
        self.maze = list(maze)
        self.is_loop = False

    def move(self):
        next_direction = {
            'N':'E', 'E': 'S', 'S': 'W', 'W': 'N'
        }
        x, y = self.current_location
        if self.current_direction == 'N':
            new_x, new_y = x, y-1
        elif self.current_direction == 'E':
            new_x, new_y = x+1, y
        elif self.current_direction == 'S':
            new_x, new_y = x, y+1
        else:
            new_x, new_y = x-1, y
        if new_x < 0 or new_y < 0:
            raise IndexError
        elif self.maze[new_y][new_x] == '#':
            self.current_direction = next_direction[self.current_direction]
        else:
            self.current_location = new_x, new_y

    def run(self):
        while True:
            try:
                if (self.current_direction, self.current_location) in self.visited:
                    self.is_loop = True
                    return
                self.visited.add((self.current_direction, self.current_location))
                self.move()
            except IndexError:
                return

class Solution(BaseSolution):
    def _parse_line(self, line: str):
        return list(line)

    def part_a(self):
        self.base_maze = Maze(self.parsed_lines)
        maze = self.base_maze
        maze.run()
        return len({location for direction, location in maze.visited})

    def part_b(self):
        nodes = set()
        locations = {location for direction, location in self.base_maze.visited if location != self.base_maze.start_location}
        for x, y in locations:
            maze = Maze([list(line) for line in self.lines])
            maze.maze[y][x] = '#'
            maze.run()

            if maze.is_loop:
                nodes.add((x, y))
        print(len(nodes))
        return len(nodes)


if __name__ == "__main__":
    submit_answers(Solution,6, 2024)
