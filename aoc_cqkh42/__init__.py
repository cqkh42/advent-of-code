import importlib


def answer(year, day, data):
    module_string = f'aoc_cqkh42.year_{year}.day_{day:>02}'
    module = importlib.import_module(module_string)

    a = module.part_a(data)
    b = module.part_b(data, answer_a=a)
    return a, b
