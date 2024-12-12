import string

import regex

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Solution(BaseSolution):
    # I tried recursion here but I get a recursion error
    REGEX = regex.compile(r'(\p{L})(?!\1)(?i:\1)')
    reacted = None
    def react(self, string):
        while True:
            new_string = self.REGEX.sub('', string)
            if new_string == string:
                return new_string
            else:
                string = new_string
    def part_a(self):
        self.reacted = self.react(self.input_)
        return len(self.reacted)

    def part_b(self):
        polys = [self.reacted.replace(char, '').replace(char.upper(), '') for char in string.ascii_lowercase]
        return min(len(self.react(string)) for string in polys)

if __name__ == "__main__":
    submit_answers(Solution,5 , 2018)
