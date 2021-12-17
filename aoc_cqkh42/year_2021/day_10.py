from collections import Counter

import numpy as np

from aoc_cqkh42 import BaseSolution

def is_corrupt(line):
    while True:
        new_line = line.replace('{}', '').replace('[]', '').replace('<>', '').replace('()', '')
        if new_line == line:
            break
        line = new_line

    for char in line:
        if char in '}])>':
            return char


def completion_score(line):
    TRANSLATOR = str.maketrans('({[<', ')}]>')
    while True:
        new_line = line.replace('{}', '').replace('[]', '').replace('<>',
                                                                    '').replace(
            '()', '')
        if new_line == line:
            break
        line = new_line
    closing = line[::-1].translate(TRANSLATOR)
    score_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for char in closing:
        score *= 5
        score += score_dict[char]
    return score


class Solution(BaseSolution):
    def part_a(self):
        illegal = [is_corrupt(line) for line in self.lines]
        illegal = Counter(illegal)

        return illegal[')'] * 3 + illegal[']'] * 57 + illegal['}'] * 1197 + illegal['>'] * 25137

    def part_b(self):
        legal = [completion_score(line) for line in self.lines if not is_corrupt(line)]
        return np.median(legal).astype(int)
