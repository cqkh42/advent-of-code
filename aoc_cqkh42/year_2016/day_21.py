import itertools
from dataclasses import dataclass
from typing import List

from aoc_cqkh42 import BaseSolution


@dataclass
class Scrambler:
    password: List[str]

    def swap_position(self, x, y):
        x_char = self.password[x]
        y_char = self.password[y]
        self.password[x] = y_char
        self.password[y] = x_char
        return self.password

    def swap_letter(self, x, y):
        mapping = {x: y, y: x}
        self.password = [mapping.get(char, char) for char in self.password]
        return self.password

    def rotate_left(self, x):
        if not x:
            return self.password
        x %= len(self.password)
        self.password = self.password[x:] + self.password[:x]
        return self.password

    def rotate_right(self, x):
        if not x:
            return self.password
        x %= len(self.password)
        self.password = (
                self.password[-x:] +
                self.password[:len(self.password) - x]
        )
        return self.password

    def rotate_based_on(self, x):
        index = self.password.index(x)
        rotate = (1 + index + (index >= 4)) % len(self.password)
        return self.rotate_right(rotate)

    def reverse(self, x, y):
        self.password = (
                self.password[:x] +
                list(reversed(self.password[x:y+1])) + self.password[y+1:]
        )
        return self.password

    def move(self, x, y):
        char = self.password.pop(x)
        self.password.insert(y, char)
        return self.password


class Solution(BaseSolution):
    def scramble(self, scrambler, line):
        match line.split():
            case ['move', _, x, *_, y]:
                scrambler.move(int(x), int(y))
            case ['rotate', 'right', steps, _]:
                scrambler.rotate_right(int(steps))
            case ['rotate', 'left', steps, _]:
                scrambler.rotate_left(int(steps))
            case ['rotate', *_, letter]:
                scrambler.rotate_based_on(letter)
            case ['swap', 'position', x, *_, y]:
                scrambler.swap_position(int(x), int(y))
            case ['swap', 'letter', x, *_, y]:
                scrambler.swap_letter(x, y)
            case ['reverse', _, x, _, y]:
                scrambler.reverse(int(x), int(y))
            case _:
                raise NotImplementedError(line)
        return scrambler

    def part_a(self, password='abcdefgh'):
        scrambler = Scrambler(list(password))
        for line in self.lines:
            scrambler = self.scramble(scrambler, line)
        return ''.join(scrambler.password)

    def part_b(self):
        for password in itertools.permutations('abcdefgh'):
            if self.part_a(password) == 'fbgdceah':
                return ''.join(password)
