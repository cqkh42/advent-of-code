import functools
import itertools
from collections import defaultdict
from dataclasses import dataclass
from typing import Self

import more_itertools
import parse
from frozendict import frozendict

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


@functools.cache
def stack_weight(name, programs):
    program = programs[name]
    if not program.dependencies:
        return program.weight
    else:
        return (
            sum(
                stack_weight(dependency, programs)
                for dependency in program.dependencies
            )
            + program.weight
        )


@dataclass(frozen=True)
class Program:
    name: str
    weight: int
    dependencies: tuple[str]


NO_DEPENDENCY_PARSER = parse.compile("{:l} ({:d})")


def parse_line(line):
    name, weight = NO_DEPENDENCY_PARSER.parse(line[0])
    if len(line) > 1:
        dependencies = tuple(line[1].split(", "))
    else:
        dependencies = tuple()
    return name, Program(name, weight, dependencies)


class Solution(BaseSolution):
    def _parse(self: Self) -> frozendict[str, Program]:
        lines = [line.split(" -> ") for line in self.lines]
        return frozendict(parse_line(line) for line in lines)

    def part_a(self):
        all_dependencies = (program.dependencies for program in self.parsed.values())
        all_dependencies = itertools.chain.from_iterable(all_dependencies)
        difference = set(self.parsed).difference(all_dependencies)
        return more_itertools.one(difference)

    def part_b(self):
        stack_weights = {
            program: stack_weight(program, self.parsed) for program in self.parsed
        }
        for program in sorted(
            self.parsed,
            key=lambda program: len(self.parsed[program].dependencies),
            reverse=True,
        ):
            d = defaultdict(list)
            dependencies = self.parsed[program].dependencies

            for dependency in dependencies:
                d[stack_weights[dependency]].append(dependency)
            if len(d) > 1:
                bad_one = [i for i in d.values() if len(i) == 1][0][0]
                good_one = [i for i in d.values() if len(i) != 1][0][0]
                change_needed = stack_weights[good_one] - stack_weights[bad_one]
                return self.parsed[bad_one].weight + change_needed


if __name__ == "__main__":
    submit_answers(Solution, 7, 2017)
