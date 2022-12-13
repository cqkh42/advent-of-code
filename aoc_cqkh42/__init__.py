from dataclasses import dataclass
import importlib

import parse

# TODO do I need to abstract out binary search?
# TODO how many places can we use more_itertools



@dataclass(init=False)
class BaseSolution:
    _lines = None
    _numbers = None

    def __init__(self, data):
        self.data = data
        self.parsed_data = self.parse_data()

    def parse_data(self):
        return self.data

    @property
    def lines(self):
        if self._lines is not None:
            return self._lines
        self._lines = self.data.split('\n')
        return self._lines

    @property
    def numbers(self):
        if self._numbers is not None:
            return self._numbers
        parser = parse.compile('{num:d}')
        self._numbers = tuple(result['num'] for result in parser.findall(self.data))
        return self._numbers

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
