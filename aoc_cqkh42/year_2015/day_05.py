import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    repeating_char = re.compile(r'(\w)\1')
    repeating_chars = re.compile(r'(\w{2}).*\1')
    repeats_with_space = re.compile(r'(\w).\1')
    bad_phrases = ('ab', 'cd', 'pq', 'xy')

    def parse_data(self):
        return self.data.split('\n')

    def _is_nice_a(self, string):
        vowels = sum(char in 'aeiou' for char in string) >= 3
        repeating_char = bool(self.repeating_char.search(string))
        phrases = all(phrase not in string for phrase in self.bad_phrases)
        return vowels and repeating_char and phrases

    def _is_nice_b(self, string):
        repeats = bool(self.repeating_chars.search(string))
        one_between = bool(self.repeats_with_space.search(string))
        return repeats and one_between

    def part_a(self):
        return sum(self._is_nice_a(string) for string in self.parsed_data)

    def part_b(self):
        return sum(self._is_nice_b(string) for string in self.parsed_data)


