import itertools
from collections import Counter, defaultdict
import re
import math


REGEX = re.compile(r'(.*):.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)')


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name


class Recipe:
    def __init__(self, ingredients):
        self.raw_ingredients = ingredients
        self.ingredients = Counter(ingredients)

    def score(self):
        totals = defaultdict(int)
        for ingredient, quantity in self.ingredients.items():
            for comp in ['capacity', 'durability', 'flavor', 'texture']:
                new_val = getattr(ingredient, comp) * quantity
                totals[comp] += new_val
        totals = [max(val, 0) for val in totals.values()]
        return math.prod(totals)

    @property
    def calories(self):
        return sum(ingredient.calories for ingredient in self.raw_ingredients)


def _parse_data(ingredients):
    regexes = [re.search(REGEX, row).groups() for row in ingredients]
    ingredients = [Ingredient(*row) for row in regexes]
    return ingredients


def part_a(data):
    ingredients = data.split('\n')
    components = _parse_data(ingredients)

    possible_ingredients = itertools.combinations_with_replacement(components, 100)
    possible_recipes = (Recipe(ingredients) for ingredients in possible_ingredients)
    return max(recipe.score() for recipe in possible_recipes)


def part_b(data, **_):
    ingredients = data.split('\n')
    components = _parse_data(ingredients)

    possible_ingredients = itertools.combinations_with_replacement(components, 100)
    possible_recipes = (Recipe(ingredients) for ingredients in possible_ingredients)
    possible_recipes = (recipe for recipe in possible_recipes if recipe.calories == 500)
    return max(recipe.score() for recipe in possible_recipes)
