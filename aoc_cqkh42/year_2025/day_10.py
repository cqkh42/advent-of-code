#!/usr/bin/python3
"""Solutions for day 10 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/10
"""
__all__ = ["Solution"]

import itertools
import math
import shapely

import networkx as nx
from typing import Self, Any
import re
import more_itertools
from dataclasses import dataclass
from collections import defaultdict

from pulp import PULP_CBC_CMD

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.coords import Coords
import pulp
import string
def chars():
    yield

def solve_line(line: str) -> int:
    """Solve the problem."""
    c = iter(string.ascii_lowercase)
    lights, *buttons, _ = line.split()
    lights = [int(char == "#") for char in lights[1:-1]]
    tidy_buttons = []
    button_vars = []

    problem = pulp.LpProblem("prob", pulp.LpMinimize)


    for button in buttons:
        nums = {int(num) for num in button[1:-1].split(",")}
        tidy_buttons.append(nums)
        v = pulp.LpVariable(next(c), lowBound=0, upBound=5,cat=pulp.const.LpInteger)
        button_vars.append(v)


    problem += pulp.lpSum(button_vars)

    light_vars = []
    for index, light in enumerate(lights):
        light_var = pulp.LpVariable(next(c),lowBound=0, upBound=5, cat=pulp.const.LpInteger)
        light_vars.append(light_var)
        triggers = [var for var, button in zip(button_vars, tidy_buttons) if index in button]
        problem += (pulp.lpSum(triggers) -(2*light_var)) == light

    problem.solve(PULP_CBC_CMD(msg=0))
    return problem.objective.value()

def solve_line_2(line: str) -> int:
    """Solve the problem."""
    c = iter(string.ascii_lowercase)
    _, *buttons, vals = line.split()
    vals = [int(char) for char in vals[1:-1].split(",")]
    tidy_buttons = []
    button_vars = []

    problem = pulp.LpProblem("prob", pulp.LpMinimize)


    for button in buttons:
        nums = {int(num) for num in button[1:-1].split(",")}
        tidy_buttons.append(nums)
        v = pulp.LpVariable(next(c), lowBound=0, upBound=sum(vals),cat=pulp.const.LpInteger)
        button_vars.append(v)


    problem += pulp.lpSum(button_vars)

    for index, val in enumerate(vals):
        triggers = [var for var, button in zip(button_vars, tidy_buttons) if index in button]
        problem += pulp.lpSum(triggers)  == val

    problem.solve(PULP_CBC_CMD(msg=0))
    return problem.objective.value()
class Solution(BaseSolution):
    """Solutions for day 10 of 2025's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        s = 0
        for index, line in enumerate(self.lines):
            solved = solve_line(line)
            s += solved
        return int(s)

    def part_b(self: Self) -> int:
        """Answer part b."""
        s = 0
        for index, line in enumerate(self.lines):
            solved = solve_line_2(line)
            s += solved
        return int(s)


if __name__ == "__main__":
    submit_answers(Solution, 10, 2025)
