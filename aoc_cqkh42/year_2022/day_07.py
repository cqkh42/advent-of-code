from aoc_cqkh42 import BaseSolution

from dataclasses import dataclass, field
from frozendict import frozendict
from typing import Set, Tuple


@dataclass
class Directory:
    name: Tuple[str]
    files: Set[str] = field(default_factory=set)
    children: Set = field(default_factory=set)

    def file_size(self):
        return sum(file[0] for file in self.files)


def total_size(dir_, directories):
    return (
        directories[dir_].file_size() +
        sum(
            total_size(dir_, directories)
            for dir_ in directories[dir_].children
        )
    )


class Solution(BaseSolution):
    def parse_data(self):
        directories = {}
        current_directory = ''

        for line in self.data.split('\n'):
            match line.split():
                case ['$', 'cd', '..']:
                    current_directory = directories[
                                            current_directory].name[:-1]
                case ['$', 'cd', new_directory]:
                    new_path = (*current_directory, new_directory)
                    if new_path not in directories:
                        directories[new_path] = Directory(new_path)
                    current_directory = new_path
                case ['dir', found_directory]:
                    directories[current_directory].children.add(
                        (*current_directory, found_directory))
                case ['$', 'ls']:
                    continue
                case _:
                    a, b = line.split()
                    a = int(a)
                    directories[current_directory].files.add((a, b))
        directories = frozendict(directories)
        return [total_size(i, directories) for i in directories]

    def total_size(self, dir_):
        return (
            self.parsed_data[dir_].file_size() +
            sum(
                self.total_size(dir_)
                for dir_ in self.parsed_data[dir_].children
            )
        )

    def part_a(self):
        return sum(dir_ for dir_ in self.parsed_data if dir_ <= 100000)

    def part_b(self):
        to_free = 30000000 - 70000000 + max(self.parsed_data)
        return min(dir_ for dir_ in self.parsed_data if dir_ >= to_free)
