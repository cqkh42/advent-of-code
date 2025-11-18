from typing import Self, Any
import itertools
from collections import Counter
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
import re
from collections import deque

class Solution(BaseSolution):
    recipes = [3,7]
    elf_1 = 0
    elf_2 = 1
    count = 2
    def step(self):
        a, b = divmod(self.recipes[self.elf_1] + self.recipes[self.elf_2], 10)
        valid = (a, b) if a else (b,)
        self.count += len(valid)
        self.recipes.extend(valid)
        self.elf_1 = (1 + self.elf_1 + self.recipes[self.elf_1]) % self.count
        self.elf_2 = (1 + self.elf_2 + self.recipes[self.elf_2]) % self.count
        return valid

    def part_a(self, steps: int = None) -> str:
        steps = steps or self.number
        while self.count < steps+10:
            self.step()
        return "".join(str(num) for num in self.recipes[steps:steps+10])

    def part_b(self):
        # secondly, try a dict look up
        recipe_str = "".join(str(num) for num in self.recipes)
        if self.input_ in recipe_str:
            raise NotADirectoryError
        recipe_str = recipe_str[-10:]
        while self.input_ not in recipe_str:
            added = self.step()
            if len(added) == 1:
                recipe_str = f"{recipe_str[-9:]}{added[0]}"
            else:
                recipe_str = f"{recipe_str[-8:]}{added[0]}{added[1]}"
        return self.count - (len(self.input_) + (not recipe_str.endswith(self.input_)))

if __name__ == "__main__":
    submit_answers(Solution, 14, 2018)
