import importlib
from dataclasses import dataclass
from functools import cached_property

import parse

# TODO do I need to abstract out binary search?
# TODO how many places can we use more_itertools

NUM_PARSER = parse.compile('{num:d}')


@dataclass
class BaseSolution:
    data: str

    def __post_init__(self):
        self.parsed_data = self.parse_data()

    def parse_data(self):
        return self.data

    @cached_property
    def lines(self):
        return self.data.split('\n')

    @cached_property
    def numbers(self):
        return tuple(result['num'] for result in NUM_PARSER.findall(self.data))

    def part_a(self):
        return None

    def part_b(self):
        return None


def answer(year, day, data):
    module_string = f'aoc_cqkh42.year_{year}.day_{day:>02}'
    module = importlib.import_module(module_string)

    solution = module.Solution(data)
    answer_a = solution.part_a()
    answer_b = solution.part_b()

    return answer_a, answer_b
