import itertools

import numpy as np
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

PARSER = parse.compile(
    "capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}"
)


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
    def _process_data(self):
        ingredients = PARSER.findall(self.input_)
        ingredients = [np.array(list(i)) for i in ingredients]
        ingredients = np.stack(ingredients)

        recipes = get_ratios(len(ingredients)) * ingredients
        return recipes.sum(-2)

    def part_a(self):
        recipe = self.processed[:, :-1]
        return str(recipe.clip(min=0).prod(1).max())

    def part_b(self):
        recipe = self.processed[self.processed[:, -1] == 500, :-1]
        return str(recipe.clip(min=0).prod(1).max())

if __name__ == "__main__":
    submit_answers(Solution, 15, 2015)