from typing import Self, Any

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

import re

import json
def count(string: re.Match):
    return '[' + str(string.group(0).count('1')) + ']'

def tidy(string):
    text = string.group(0)
    a = text.rfind('{')
    left = text[:a]
    right = text[a:]
    return left+'1'

def tidy_2(string):
    text = string.group(0)
    a = text.rfind('{')
    numbers = sum(int(i) for i in text[a+1:-1].split(',') if i)
    return text[:a] + '[' + str(numbers) + ']'


class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        first = re.sub(r'!.', '', self.input_)
        second = re.sub(r'<(.*?)>', '', first)
        return second

    def part_a(self):
        total = 0
        current_value = 1
        for char in self.processed:
            if char == '{':
                total += current_value
                current_value += 1
            if char == '}':
                current_value -= 1
        return total

    def part_b(self):
        first = re.sub(r'!.', '', self.input_)
        garbage = re.findall(r'<(.*?)>', first)
        return sum(len(string) for string in garbage)

if __name__ == "__main__":
    submit_answers(Solution, 9, 2017)
