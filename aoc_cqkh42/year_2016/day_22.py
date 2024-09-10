from functools import cached_property
import itertools
from dataclasses import dataclass, field, replace

import more_itertools
from frozendict import frozendict
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.graph.a_star import AStar, AStarBaseNode


PARSER = parse.compile(
    r'/dev/grid/node-x{test[x]:d}-y{test[y]:d}{:s}{test[size]:d}T{:s}{test[used]:d}'
)


@dataclass(frozen=True)
class Cell:
    size: int
    used: int

    @property
    def avail(self):
        return self.size - self.used

    def change_data(self, volume):
        return replace(self, used=self.used+volume)


@dataclass(frozen=True)
class Grid(AStarBaseNode):
    current_location: tuple
    empty_location: tuple
    grid: frozendict = field(default_factory=lambda: frozendict())
    distance: int = field(default=0, hash=False, compare=False)
    h: int = field(default=0)

    def __iter__(self):
        yield from self.grid

    def __getitem__(self, item):
        return self.grid.get(item)

    def is_valid(self):
        return True

    def move_data(self, origin: tuple, target: tuple):
        origin_cell = self[origin]
        volume = origin_cell.used
        new_origin = origin_cell.change_data(-volume)
        new_target = self[target].change_data(volume)
        new_grid = self.grid.delete(origin).delete(target).set(origin, new_origin).set(target, new_target)

        d = abs(origin[0] - self.current_location[0]) + abs(origin[1] - self.current_location[1])
        return replace(self, grid=new_grid, distance=self.distance+1, h=d)

    def is_target(self):
        return self.current_location == (0, 0)

    def neighbours(self):
        iterations = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # c = (
        #     (self.empty, self.empty[0])
        # )
        c = (
            ((self_x, self_y), (self_x + x, self_y + y))
            for ((self_x, self_y), (x, y))
            in itertools.product(self, iterations)
        )
        c = ((self_, target) for self_, target in c if self[target])
        c = ((self_, target) for self_, target in c if self[target].avail >= self[self_].used)
        for self_, target in c:
            moved = self.move_data(self_, target)
            if self_ == self.current_location:
                new_current_location = target
                yield replace(moved, current_location=new_current_location)
            else:
                yield moved


class Solution(BaseSolution):
    def _process_data(self):
        rows = PARSER.findall(self.input_)
        cells = [
            (row.named['test']) for row in rows
        ]
        cells = frozendict({
            (cell['x'], cell['y']): Cell(cell['size'], cell['used']) for cell in cells
        })
        max_x = max(x for (x, y) in cells)

        empty = [k for k, v in cells.items() if v.used == 0][0]

        nodes = Grid((max_x, 0), empty, cells, 0)
        return nodes

    @cached_property
    def possible_combinations(self):
        return [
            (node_a, node_b)
            for node_a, node_b in itertools.combinations(self.processed.grid, 2) if
            (self.processed.grid[node_a].used and self.processed.grid[node_a].used <= self.processed.grid[node_b].avail) or
            (self.processed.grid[node_b].used and self.processed.grid[node_b].used <= self.processed.grid[node_a].avail)
        ]

    def part_a(self):
        return len(self.possible_combinations)

    def part_b(self):
        # raise
        in_game = set(more_itertools.flatten(a for a in self.possible_combinations))
        in_game = frozendict({i: self.processed.grid[i] for i in in_game})
        self.processed = replace(self.processed, grid=in_game)
        # self.processed.grid = in_game
        # return
        solver = AStar(self.processed)
        answer = solver.run()
        print(len(solver.visited))
        return answer


if __name__ == "__main__":
    # started at 21:40
    s = submit_answers(Solution, 22, 2016)
