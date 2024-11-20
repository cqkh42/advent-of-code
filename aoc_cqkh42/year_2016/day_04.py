import string
from collections import Counter
from dataclasses import dataclass

import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


def decrypt_letter(char, sector):
    if char == "-":
        return " "
    index = (string.ascii_lowercase.index(char) + (sector % 26)) % 26
    return string.ascii_lowercase[index]


@dataclass
class Room:
    encrypted: str
    sector: int
    checksum: str

    def calc_checksum(self):
        counted = Counter(self.encrypted.replace("-", "").strip())
        in_order = sorted(counted.items(), key=lambda x: (-x[1], x[0]))[:5]
        in_order = [letter for letter, count in in_order]
        return "".join(in_order)

    def valid_checksum(self):
        return self.calc_checksum() == self.checksum

    def decrypt(self):
        return "".join(
            decrypt_letter(char, self.sector) for char in self.encrypted.strip()
        )


class Solution(BaseSolution):
    def _parse(self):
        rooms = list(parse.findall(r"{:D}-{:d}[{:w}]", self.input_))
        rooms = [Room(*room) for room in rooms]
        checksummed = (room for room in rooms if room.valid_checksum())
        real = [(room.decrypt(), room.sector) for room in checksummed]

        r = dict(real)
        return r

    def part_a(self):
        return sum(self.parsed.values())

    def part_b(self):
        return self.parsed["northpole object storage"]
