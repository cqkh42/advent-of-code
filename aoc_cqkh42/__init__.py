from dataclasses import dataclass
import importlib


@dataclass(init=False)
class BaseSolution:
    def __init__(self, data):
        self.data = data
        self.parsed_data = self.parse_data()

    def parse_data(self):
        return self.data

    def part_a(self):
        return False

    def part_b(self):
        return False


def answer(year, day, data):
    module_string = f'aoc_cqkh42.year_{year}.day_{day:>02}'
    module = importlib.import_module(module_string)

    solution = module.Solution(data)
    answer_a = solution.part_a()
    answer_b = solution.part_b()

    return answer_a, answer_b
