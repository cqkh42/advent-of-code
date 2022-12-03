from dataclasses import dataclass
import importlib

import parse

# TODO do I need to abstract out binary search?


@dataclass(init=False)
class BaseSolution:
    def __init__(self, data):
        self.data = data
        self.parsed_data = self.parse_data()

    def parse_data(self):
        return self.data

    @property
    def lines(self):
        return self.data.split('\n')

    @property
    def numbers(self):
        parser = parse.compile('{num:d}')
        return [result['num'] for result in parser.findall(self.data)]

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
