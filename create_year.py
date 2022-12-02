import pathlib

base_day = """from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        ...

    def part_b(self):
        ...      
"""

def create_puzzles(year):
    p = pathlib.Path.cwd()
    target_path = p / f'year_{year}'
    target_path.mkdir(exist_ok=True)
    (target_path / '__init__.py').touch(exist_ok=True)
    for day in range(1, 26):
        day_file = target_path / f'day_{day:02}.py'
        if not day_file.exists():
            day_file.write_text(base_day)
        else:
            raise FileExistsError(f'{day_file} already exists!')


if __name__ == '__main__':
    year = input('Which year are you creating? ')
    create_puzzles(year)
