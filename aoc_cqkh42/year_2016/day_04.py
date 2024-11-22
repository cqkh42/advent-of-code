import string
from collections import Counter
from dataclasses import dataclass

import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


def decrypt_letter(char, sector):
    if char == "-":
        return " "
    index = (string.ascii_lowercase.index(char) + sector) % 26
    return string.ascii_lowercase[index]


@dataclass
class Room:
    encrypted: str
    sector: int
    checksum: str

    def calc_checksum(self):
        counted = Counter(sorted(self.encrypted.replace("-", "")))
        in_order = counted.most_common(5)
        in_order = [letter for letter, count in in_order]
        return "".join(in_order)

    def valid_checksum(self):
        return self.calc_checksum() == self.checksum

    def decrypt(self):
        return "".join(
            decrypt_letter(char, self.sector) for char in self.encrypted.strip()
        )


class Solution(BaseSolution):
    PARSER = parse.compile(r"{:D}-{:d}[{:w}]")
    def _parse(self):
        return dict(room for room in self.parsed_lines if room)

    def _parse_line(self, line: str):
        line = self.PARSER.search(line)
        room = Room(*line)
        if not room.valid_checksum():
            return
        else:
            return room.decrypt(), room.sector


    def part_a(self):
        return sum(self.parsed.values())

    def part_b(self):
        return self.parsed["northpole object storage"]
