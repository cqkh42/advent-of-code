import itertools

from aoc_cqkh42.helpers import aocr
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2019.computer import Computer


def calc_turn(direction, turn):
    t = 90 if turn else - 90
    return (direction + t) % 360


def move(position, direction):
    if direction == 0:
        position = (position[0], position[1] + 1)
    elif direction == 90:
        position = (position[0] + 1, position[1])
    elif direction == 180:
        position = (position[0], position[1] - 1)
    elif direction == 270:
        position = (position[0] - 1, position[1])

    return position


def process_square(computer, position, direction, results):
    computer.inputs = [results.get(position, 0)]
    computer.outputs = []
    while len(computer.outputs) < 2:
        computer.run_iteration()
    colour, turn = computer.outputs
    results[position] = colour
    direction = calc_turn(direction, turn)
    position = move(position, direction)
    return computer, position, direction, results


def run(inputs, start_colour):
    # start on a square
    position = (0, 0)
    direction = 0
    results = {position: start_colour}
    computer = Computer(list(inputs), [])
    while True:
        try:
            computer, position, direction, results = process_square(computer, position, direction, results)
        except StopIteration:
            return results


class Solution(BaseSolution):
    def part_a(self):
        return len(run(self.numbers, 0))

    def part_b(self):
        results = run(self.numbers, 1)
        xs, ys = zip(*results)

        rows = []
        for y in range(max(ys), min(ys) - 1, -1):
            row = [results.get((x, y)) for x in range(min(xs), max(xs) + 1)]
            rows.append(row)
        rows = [row[1:41] for row in rows]
        return aocr.word(itertools.chain.from_iterable(rows))
