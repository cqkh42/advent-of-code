from collections import Counter

import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2019.computer import Computer


class Solution(BaseSolution):

    def part_a(self):
        computer = Computer(list(self.numbers), [])
        computer.run()
        results = computer.outputs
        chunks = more_itertools.chunked(results, 3)

        tiles = [chunk[2] for chunk in chunks]
        result = Counter(tiles)[2]
        return result

    def part_b(self):
        inputs = list(self.numbers)
        inputs[0] = 2
        computer = Computer(inputs, [])

        results = {}
        while True:
            try:
                computer.run()
            except IndexError:
                pass
            chunks = more_itertools.chunked(computer.outputs, 3)
            computer.outputs = []
            new_results = {tuple(i[:2]): i[2] for i in chunks}
            results.update(new_results)
            ball_x = [k for k, v in results.items() if v == 4][0][0]
            paddle_x = [k for k, v in results.items() if v == 3][0][0]
            if ball_x > paddle_x:
                computer.inputs.append(1)
            elif ball_x < paddle_x:
                computer.inputs.append(-1)
            else:
                computer.inputs.append(0)

            if not sum(i == 2 for i in results.values()):
                break
        result = results[(-1, 0)]
        return result
