from typing import Self, Any
import itertools
from collections import Counter
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Cart:
    def __init__(self, grid, current, orientation):
        self.grid = grid
        self.current = current
        self.orientation = orientation
        self.turns = itertools.cycle(["left", "straight", "right"])

    def __gt__(self, other):
        return self.current > other.current
    def turn(self):
        way = next(self.turns)
        mapping = {
            ("^", "left"): "<",
            ("^", "right"): ">",
            ("v", "left"): ">",
            ("v", "right"): "<",
            ("<", "left"): "v",
            ("<", "right"): "^",
            (">", "left"): "^",
            (">", "right"): "v",
        }
        if way != "straight":
            self.orientation = mapping[(self.orientation, way)]
        if self.orientation == "^":
            self.current = (self.current[0], self.current[1] - 1)
        elif self.orientation == "v":
            self.current = (self.current[0], self.current[1] + 1)
        elif self.orientation == "<":
            self.current = (self.current[0]-1, self.current[1])
        elif self.orientation == ">":
            self.current = (self.current[0]+1, self.current[1])



    def move(self):
        if self.grid[self.current] == "|" and self.orientation == "v":
            self.current = (self.current[0], self.current[1] + 1)
        elif self.grid[self.current] == "|" and self.orientation == "^":
            self.current = (self.current[0], self.current[1] - 1)
        elif self.grid[self.current] == "/" and self.orientation == "^":
            self.current = (self.current[0]+1, self.current[1])
            self.orientation = ">"
        elif self.grid[self.current] == "/" and self.orientation == "<":
            self.current = (self.current[0], self.current[1] + 1)
            self.orientation = "v"
        elif self.grid[self.current] == "/" and self.orientation == ">":
            self.current = (self.current[0], self.current[1]-1)
            self.orientation = "^"
        elif self.grid[self.current] == "/" and self.orientation == "v":
            self.current = (self.current[0]-1, self.current[1])
            self.orientation = "<"

        elif self.grid[self.current] == "\\" and self.orientation == "^":
            self.current = (self.current[0] - 1, self.current[1])
            self.orientation = "<"
        elif self.grid[self.current] == "\\" and self.orientation == "<":
            self.current = (self.current[0], self.current[1] - 1)
            self.orientation = "^"
        elif self.grid[self.current] == "\\" and self.orientation == ">":
            self.current = (self.current[0], self.current[1] + 1)
            self.orientation = "v"
        elif self.grid[self.current] == "\\" and self.orientation == "v":
            self.current = (self.current[0] + 1, self.current[1])
            self.orientation = ">"

        elif self.grid[self.current] == "-" and self.orientation == "<":
            self.current = (self.current[0] - 1, self.current[1])
        elif self.grid[self.current] == "-" and self.orientation == ">":
            self.current = (self.current[0] + 1, self.current[1])
        elif self.grid[self.current] == "+":
            self.turn()
        else:
            raise KeyError (self.current, self.grid[self.current], self.orientation)

class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        grid = {}
        carts = []
        for y, row in enumerate(self.lines):
            for x, char in enumerate(row):
                if char in r"/\|-+":
                    grid[(x, y)] = char
                elif char in "^v":
                    carts.append(((x, y), char))
                    grid[(x, y)] = "|"
                elif char in "<>":
                    carts.append(((x, y), char))
                    grid[(x, y)] = "-"
        return [Cart(grid, current, orientation) for current, orientation in carts]




    def part_a(self):
        while True:
            carts = sorted(self.parsed)
            for cart in carts:
                cart.move()
            locations = Counter(cart.current for cart in carts)
            if locations.most_common()[0][1] > 1:
                x, y =locations.most_common()[0][0]
                return f"{x},{y}"

    def prune(self):
        locations = Counter(cart.current for cart in self.parsed)
        crash = {k for k in locations if locations[k] > 1}
        self.parsed = [cart for cart in self.parsed if cart.current not in crash]


    def part_b(self):
        self.prune()
        while True:
            carts = sorted(self.parsed)
            for cart in carts:
                cart.move()
                self.prune()
            if len(self.parsed) == 1:
                x, y = self.parsed[0].current
                return f"{x},{y}"

if __name__ == "__main__":
    submit_answers(Solution, 13, 2018, user="google")
