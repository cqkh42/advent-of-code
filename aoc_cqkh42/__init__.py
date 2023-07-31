import importlib
import json
from pathlib import Path

from aocd.models import Puzzle, User


def get_user(user_name: str):
    file_name = Path.home() / ".config" / "aocd" / "tokens.json"
    mappings = json.loads(file_name.read_text())
    token = mappings[user_name]
    return User(token)


def submit_answers(solution, day, year, user=None):
    if user:
        user = get_user(user)
    puzzle = Puzzle(year=year, day=day, user=user)
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
