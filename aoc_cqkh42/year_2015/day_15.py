import itertools
import math
import re
from collections import Counter

REGEX = re.compile(r'.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)')


def _create_recipes(data):
    rows = (REGEX.search(row).groups() for row in data.split('\n'))
    ingredients = (tuple(int(val) for val in values) for values in rows)
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


def part_a(data):
    recipes = _create_recipes(data)
    return max(_score_recipe(recipe) for recipe in recipes)


def part_b(data, **_):
    recipes = _create_recipes(data)
    return max(_score_recipe(recipe, 500) for recipe in recipes)
