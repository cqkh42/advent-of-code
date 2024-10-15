import itertools

import functools
import itertools
from dataclasses import dataclass, field
from typing import Self, Any
from collections import defaultdict

from frozendict import frozendict

import more_itertools
import parse
from functools import cached_property
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers


@functools.cache
def stack_weight(name, programs):
    program = programs[name]
    if not program.dependencies:
        return program.weight
    else:
        return sum(stack_weight(dependency, programs) for dependency in program.dependencies) + program.weight

@dataclass(frozen=True)
class Program:
    name: str
    weight: int
    dependencies: tuple[str]

NO_DEPENDENCY_PARSER = parse.compile('{:l} ({:d})')

def parse_line(line):
    name, weight = NO_DEPENDENCY_PARSER.parse(line[0])
    if len(line) > 1:
        dependencies = tuple(line[1].split(', '))
    else:
        dependencies = tuple()
    return name, Program(name, weight, dependencies)

class Solution(BaseSolution):
    def _process_data(self: Self) -> frozendict[str, Program]:
        lines = [line.split(' -> ') for line in self.lines]
        return frozendict(parse_line(line) for line in lines)

    def part_a(self):
        all_dependencies = (program.dependencies for program in self.processed.values())
        all_dependencies = itertools.chain.from_iterable(all_dependencies)
        difference = set(self.processed).difference(all_dependencies)
        return more_itertools.one(difference)

    def part_b(self):
        print()
        stack_weights = {program: stack_weight(program, self.processed) for program in self.processed}
        for program in sorted(self.processed, key=lambda program: len(self.processed[program].dependencies), reverse=True):
            d = defaultdict(list)
            dependencies = self.processed[program].dependencies

            for dependency in dependencies:
                d[stack_weights[dependency]].append(dependency)
            if len(d) > 1:
                bad_one = [i for i in d.values() if len(i) == 1][0][0]
                good_one = [i for i in d.values() if len(i) != 1][0][0]
                change_needed = stack_weights[good_one] - stack_weights[bad_one]
                return self.processed[bad_one].weight + change_needed

if __name__ == "__main__":
    submit_answers(Solution, 7, 2017)
