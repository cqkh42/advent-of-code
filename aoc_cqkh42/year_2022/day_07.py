from aoc_cqkh42 import BaseSolution

from dataclasses import dataclass, field
from functools import cache
from frozendict import frozendict
from collections import defaultdict
from typing import List, Set, Tuple
import heapq

@dataclass
class Directory:
    name: Tuple[str]
    files: Set[str] = field(default_factory=set)
    children: Set = field(default_factory=set)

    def file_size(self):
        return sum(file[0] for file in self.files)


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
        return directories

    def total_size(self, dir_):
        return (
            self.parsed_data[dir_].file_size() +
            sum(
                self.total_size(dir_)
                for dir_ in self.parsed_data[dir_].children
            )
        )

    def part_a(self):
        k = (self.total_size(i) for i in self.parsed_data)
        return sum(i for i in k if i <= 100000)

    def part_b(self):
        used_space = self.total_size(('/',))
        available_space = 70000000 - used_space
        to_free = 30000000 - available_space
        k = (self.total_size(i) for i in self.parsed_data)
        k = (i for i in k if i >= to_free)
        return min(k)

