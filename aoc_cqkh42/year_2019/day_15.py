# TODO A* class?
from collections import Counter

from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.year_2019.computer import Computer


def path_to_coordinate(path):
    counts = Counter(path)
    x = counts.get(4, 0) - counts.get(3, 0)
    y = counts.get(1, 0) - counts.get(2, 0)
    return x, y


def winning_computer(data):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]
    visited = set()
    queue = [[inputs, 0, 0, []]]

    while True:
        intcode, pointer, relative_base, path = queue.pop(0)
        this_location = path_to_coordinate(path)
        if this_location in visited:
            continue
        else:
            visited.add(this_location)

        for next_ in range(1, 5):
            c = Computer(intcode, [next_])
            c.pointer = pointer
            c.relative_base = relative_base
            try:
                c.run()
            except IndexError:
                pass
            if c.output == 2:
                result = len(path) + 1
                break

            elif c.output == 1:
                queue.append(
                    [c.intcode, c.pointer, c.relative_base, [*path, next_]])
        else:
            continue
        break
    return c, result


class Solution(BaseSolution):
    def part_a(self):
        c, result = winning_computer(self.data)
        return result

    def part_b(self):
        c, result = winning_computer(self.data)
        intcode_at_zero = c.intcode
        pointer_at_zero = c.pointer
        relative_base_at_zero = c.relative_base

        visited = {}
        queue = [[intcode_at_zero, pointer_at_zero, relative_base_at_zero, []]]

        while len(queue):
            intcode, pointer, relative_base, path = queue.pop(-1)
            this_location = path_to_coordinate(path)
            if this_location in visited:
                continue
            else:
                visited[this_location] = len(path)

            for next_ in range(1, 5):
                c = Computer(intcode, [next_])
                c.pointer = pointer
                c.relative_base = relative_base
                try:
                    c.run()
                except IndexError:
                    pass

                if c.output == 1:
                    queue.append(
                        [c.intcode, c.pointer, c.relative_base,
                         [*path, next_]])
            else:
                continue
        result = max(visited.values())
        return result
