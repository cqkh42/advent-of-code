import importlib


def answer(year: int, day: int, data: str):
    module_string = f"aoc_cqkh42.year_{year}.day_{day:>02}"
    module = importlib.import_module(module_string)

    solution = module.Solution(data)
    answer_a = solution.part_a()
    answer_b = solution.part_b()

    return answer_a, answer_b
