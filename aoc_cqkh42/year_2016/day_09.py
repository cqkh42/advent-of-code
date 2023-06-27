import re
from collections import defaultdict

import parse

from aoc_cqkh42 import BaseSolution


def split(string):
    parts = []
    while string:
        bracket = re.match(BRACKET_REGEX, string)
        num_chars = int(bracket.group(1))
        end = bracket.end() + num_chars
        parts.append(string[:end])
        string = string[end:]
    return parts


def do_sub(string):
    new_string = ''
    while string:
        next_bracket = p.search(string)
        num_chars, num_reps = next_bracket
        end = next_bracket.spans[1][1] + 1
        new_string += string[end:num_chars + end] * num_reps
        string = string[num_chars + end:]
    return new_string


class Solution(BaseSolution):
    def part_a(self):
        return len(do_sub(self.data))

    def part_b(self):
        c = {part: 1 for part in split(self.data)}
        total = 0

        while c:
            new_parts = defaultdict(int)
            for k, v in c.items():
                if k.count('(') == 1:
                    total += len(do_sub(k)) * v
                else:
                    k = do_sub(k)
                    for i in split(k):
                        new_parts[i] += v
            c = new_parts
        return total


BRACKET_REGEX = re.compile(r'\((\d+)+x(\d+)\)')
p = parse.compile(r'({:d}x{:d})')






