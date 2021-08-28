# TODO this is messy using counters - can be better

import itertools
import math
from collections import Counter

import parse

from aoc_cqkh42 import BaseSolution


PARSER = parse.compile('capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}')


class Solution(BaseSolution):
    def parse_data(self):
        ingredients = PARSER.findall(self.data)
        recipes = itertools.combinations_with_replacement(ingredients, 100)
        return list(recipes)

    def part_a(self):
        return max(_score_recipe(recipe) for recipe in self.parsed_data)

    def part_b(self):
        return max(_score_recipe(recipe, 500) for recipe in self.parsed_data)


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
