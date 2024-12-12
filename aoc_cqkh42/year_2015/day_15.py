import itertools

import numpy as np
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def get_ratios(num_ingredients):
    master_ratios = itertools.combinations_with_replacement(
        range(1, 101), num_ingredients
    )
    master_ratios = [ratio for ratio in master_ratios if sum(ratio) == 100]
    master_ratios = (itertools.permutations(i) for i in master_ratios)
    master_ratios = [
        np.array(ratio).reshape(-1, 1)
        for ratio in itertools.chain.from_iterable(master_ratios)
    ]
    return np.stack(master_ratios)


class Solution(BaseSolution):
    def _parse(self):
        ingredients = np.stack(self.line_numbers)
        recipes = get_ratios(len(ingredients)) * ingredients
        return recipes.sum(-2)

    def output_answer(self, recipe):
        return recipe.clip(min=0).prod(1).max()

    def part_a(self):
        return self.output_answer(self.parsed[:, :-1])

    def part_b(self):
        return self.output_answer(self.parsed[self.parsed[:, -1] == 500, :-1])


if __name__ == "__main__":
    submit_answers(Solution, 15, 2015)
