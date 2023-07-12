import importlib

from aocd.models import Puzzle


def submit_answers(solution, day, year):
    puzzle = Puzzle(year=year, day=day)
    solution = solution(puzzle.input_data)
    puzzle.answer_a = solution.part_a()
    puzzle.answer_b = solution.part_b()


def answer(year: int, day: int, data: str):
    module_string = f"aoc_cqkh42.year_{year}.day_{day:>02}"
    module = importlib.import_module(module_string)

    solution = module.Solution(data)
    answer_a = solution.part_a()
    answer_b = solution.part_b()

    return answer_a, answer_b
