import itertools
import math
from collections import Counter

import parse

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return list(_create_recipes(self.data))

    def part_a(self):
        return max(_score_recipe(recipe) for recipe in self.parsed_data)

    def part_b(self):
        return max(_score_recipe(recipe, 500) for recipe in self.parsed_data)


p = parse.compile('capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}')


def _create_recipes(data):
    ingredients = p.findall(data)
    recipes = itertools.combinations_with_replacement(ingredients, 100)
    return recipes


def _score_recipe(recipe, calories=None):
    recipe = Counter(recipe)
    item_scores = (
        [attr * quantity for attr in attrs]
        for attrs, quantity in recipe.items()
    )
    attr_scores = [sum(i) for i in zip(*item_scores)]
    if min(attr_scores) <= 0 or (calories and attr_scores[-1] != calories):
        return 0
    else:
        return math.prod(attr_scores[:4])
