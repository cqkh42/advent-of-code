import functools
import itertools
from dataclasses import dataclass, field, replace

import more_itertools
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.graph.a_star import AStar, AStarBaseNode


PARSER = parse.compile(
    r'/dev/grid/node-x{test[x]:d}-y{test[y]:d}{:s}{test[size]:d}T{:s}{test[used]:d}'
)


@dataclass(frozen=True)
class Cell:
    x: int
    y: int
    size: int
    used: int

    @property
    def avail(self):
        return self.size - self.used

    def change_data(self, volume):
        return replace(self, used=self.used+volume)


@functools.cache
def is_cell_valid(cell: Cell):
    return cell.x > 0 and cell.y > 0 and cell.avail > 0

@dataclass(frozen=True)
class Grid(AStarBaseNode):
    current_location: tuple
    grid: set = field(default_factory=lambda: frozenset())
    distance: int = field(default=0, hash=False, compare=False)

    def __iter__(self):
        yield from self.grid

    def __getitem__(self, item):
        x, y = item
        return more_itertools.only(
            cell for cell in self if cell.x == x and cell.y == y
        )

    def __len__(self):
        return len(self.grid)

    @property
    def h(self):
        return sum(self.current_location)

    def is_valid(self):
        return all(is_cell_valid(cell) for cell in self)

    def move_data(self, origin: Cell, target: Cell):
        volume = origin.used
        new_origin = origin.change_data(-volume)
        new_target = target.change_data(volume)
        new_grid = set(self.grid.difference({origin, target}))
        new_grid.add(new_origin)
        new_grid.add(new_target)
        return replace(self, grid=frozenset(new_grid), distance=self.distance+1)

    def is_target(self):
        return self.current_location == (0, 0)

    def neighbours(self):
        iterations = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for cell in self:
            for x, y in iterations:
                target_x = cell.x + x
                target_y = cell.y + y
                target_cell = self[target_x, target_y]
                # except IndexError:
                #     continue
                if not target_cell:
                    continue
                if target_cell.avail >= cell.used:
                    moved = self.move_data(cell, target_cell)
                    if (cell.x, cell.y) == self.current_location:
                        new_current_location = (target_x, target_y)
                        yield replace(moved, current_location=new_current_location)
                    else:
                        yield moved


class Solution(BaseSolution):
    def _process_data(self):
        rows = PARSER.findall(self.input_)
        cells = frozenset({Cell(**row.named['test']) for row in rows})
        max_x = max(cell.x for cell in cells)

        nodes = Grid((max_x, 0), cells)
        return nodes

    def part_a(self):
        viable = (
            (node_a.used and node_a.used <= node_b.avail) or
            (node_b.used and node_b.used <= node_a.avail)
            for node_a, node_b in itertools.combinations(self.processed, 2)
        )
        return sum(viable)

    def part_b(self):
        solver = AStar(self.processed).run()
        return solver


if __name__ == "__main__":
    # started at 21:40
    submit_answers(Solution, 22, 2016)
