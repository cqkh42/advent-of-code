from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    index = 0

    def _process_data(self: Self) -> Any:
        return int(self.input_) + 1

    def _do_step(self, step):
        self.index += self.processed
        self.index %= step

    def part_a(self):
        array = [0]
        for step in range(1, 2018):
            self._do_step(step)
            array.insert(self.index, step)
        return array[self.index+1]


    def part_b(self):
        last_step = 0
        for step in range(2018, 50_000_001):
            self._do_step(step)
            if not self.index:
                last_step = step
        return last_step


if __name__ == "__main__":
    submit_answers(Solution, 17, 2017)