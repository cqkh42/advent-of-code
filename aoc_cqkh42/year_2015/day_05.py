import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    repeating_char = re.compile(r'(\w)\1')
    repeating_chars = re.compile(r'(\w{2}).*\1')
    repeats_with_space = re.compile(r'(\w).\1')

    def parse_data(self):
        return self.data.split('\n')

    def _is_nice_a(self, string):
        # noinspection SpellCheckingInspection
        vowels = sum(string.count(vowel) for vowel in 'aeiou') >= 3
        repeating_char = self.repeating_char.search(string)
        bad_phrases = ['ab', 'cd', 'pq', 'xy']
        phrases = all(phrase not in string for phrase in bad_phrases)
        return all((vowels, repeating_char, phrases))

    def part_a(self):
        return sum(self._is_nice_a(string) for string in self.parsed_data)

    def part_b(self):
        return sum(self._is_nice_b(string) for string in self.parsed_data)

    def _is_nice_b(self, string):
        repeats = self.repeating_chars.search(string)
        one_between = self.repeats_with_space.search(string)
        return bool(repeats and one_between)
