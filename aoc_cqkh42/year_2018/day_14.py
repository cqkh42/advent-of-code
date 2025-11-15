from typing import Self, Any
import itertools
from collections import Counter
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
import re

class Solution(BaseSolution):
    recipes = [3, 7]
    elves = [0, 1]
    def part_a(self, steps: int = None) -> str:
        steps = steps or self.number
        while len(self.recipes) < steps+10:
            a, b = divmod(self.recipes[self.elves[0]] +self.recipes[self.elves[1]], 10)
            if a:
                self.recipes.append(a)
            self.recipes.append(b)
            self.elves[0] = (1+self.elves[0] + self.recipes[self.elves[0]])%len(self.recipes)
            self.elves[1] = (1+self.elves[1] + self.recipes[self.elves[1]])%len(self.recipes)
        return "".join(str(num) for num in self.recipes[steps:steps+10])

    def part_b(self):
        recipe_str = "".join(str(num) for num in self.recipes)
        for _ in range(50_000_000):
            a, b = divmod(self.recipes[self.elves[0]] + self.recipes[self.elves[1]], 10)
            if a:
                self.recipes.extend([a, b])
                recipe_str += f"{a}{b}"
            else:
                self.recipes.extend([b])
                recipe_str += str(b)
            self.elves[0] = (1 + self.elves[0] + self.recipes[self.elves[0]]) % len(self.recipes)
            self.elves[1] = (1 + self.elves[1] + self.recipes[self.elves[1]]) % len(self.recipes)
        a = re.sub(f"{self.input_}.*", "", recipe_str)
        return len(a)

if __name__ == "__main__":
    submit_answers(Solution, 14, 2018)
