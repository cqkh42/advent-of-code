import re

from aoc_cqkh42 import BaseSolution


def _decode_str(string):
    string = re.sub(r'^"', '', string)
    string = re.sub(r'"$', '', string)
    string = re.sub(r'\\\\', r'\\', string)
    string = re.sub(r'\\"', '"', string)
    string = re.sub(r'\\x[a-f0-9]{2}', 'x', string)
    return string


class Solution(BaseSolution):
    def part_a(self):
        code_len = len(self.data) - len(self.lines) + 1
        decoded = (len(_decode_str(line)) for line in self.lines)
        return code_len - sum(decoded)

    def part_b(self):
        return sum(
            line.count('"') + line.count("\\") + 2
            for line in self.lines
            )



