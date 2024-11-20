from dataclasses import dataclass, field
from typing import Set, Tuple

from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Directory:
    name: Tuple[str, ...]
    files: Set[str] = field(default_factory=set)
    children: list = field(default_factory=list)

    def file_size(self):
        return sum(file[0] for file in self.files)

    @property
    def parent(self):
        return self.name[:-1]

    def total_size(self):
        child_size = sum(dir_.total_size() for dir_ in self.children)
        return self.file_size() + child_size


class Solution(BaseSolution):
    cur_dir = Directory(tuple('/'))
    directories = {}

    def cd(self, dir_):
        if dir_ == '..':
            self.cur_dir = self.directories[self.cur_dir.parent]
        else:
            new_path = (*self.cur_dir.name, dir_)
            self.cur_dir = self.directories[new_path]

    def create_dir(self, name: str):
        d = Directory((*self.cur_dir.name, name))
        self.directories[d.name] = d
        return d

    def _parse(self):
        self.directories[self.cur_dir.name] = self.cur_dir
        for line in self.lines[1:]:
            match line.split():
                case ['$', 'cd', dir_]:
                    self.cd(dir_)
                case ['dir', dir_]:
                    self.cur_dir.children.append(self.create_dir(dir_))
                case ['$', 'ls']:
                    continue
                case _:
                    size, name = line.split()
                    self.cur_dir.files.add((int(size), name))
        return [dir_.total_size() for dir_ in self.directories.values()]

    def part_a(self):
        return sum(dir_ for dir_ in self.parsed if dir_ <= 100000)

    def part_b(self):
        to_free = 30000000 - 70000000 + max(self.parsed)
        return min(dir_ for dir_ in self.parsed if dir_ >= to_free)
