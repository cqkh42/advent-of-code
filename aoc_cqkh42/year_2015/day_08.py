import re

from aoc_cqkh42.helpers.base_solution import BaseSolution


def _decode_str(string):
    replacements = [
        (r'^"', ""),
        (r'"$', ""),
        (r"\\\\", r"\\"),
        (r'\\"', '"'),
        (r"\\x[a-f0-9]{2}", "x"),
    ]
    for regex, repl in replacements:
        string = re.sub(regex, repl, string)
    return string


class Solution(BaseSolution):
    def part_a(self):
        code_len = len(self.data) - len(self.lines) + 1
        decoded = (len(_decode_str(line)) for line in self.lines)
        return code_len - sum(decoded)

    def part_b(self):
        return (
                2 * len(self.lines) + self.data.count('"') + self.data.count(
            "\\")
        )
