import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return self.data.split('\n')

    def part_a(self):
        code_len = len(self.data) - len(self.parsed_data) + 1
        decoded = (len(_decode_str(line)) for line in self.parsed_data)
        return code_len - sum(decoded)

    def part_b(self):
        return sum(
            line.count('"') + line.count('\\') + 2
            for line in self.parsed_data
            )


def _decode_str(string):
    string = re.sub(r'^"', '', string)
    string = re.sub(r'"$', '', string)
    string = re.sub(r'\\\\', r'\\', string)
    string = re.sub(r'\\"', '"', string)
    string = re.sub(r'\\x[a-f0-9]{2}', 'x', string)
    return string
