from _md5 import md5 as md5_builtin
from collections import defaultdict

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        hashes = ""
        # placed_hashes = [''] * 8
        placed_hashes = defaultdict(list)
        strings = ((self.input_ + str(index)).encode() for index in range(100_000_000))
        h = (md5_builtin(s).hexdigest() for s in strings)
        valid_hashes = (digest[5:7] for digest in h if digest.startswith("00000"))

        for l, r in valid_hashes:
            hashes += l
            kk = int(l, 16)
            if kk < 8:
                placed_hashes[kk].append(r)
            if len(placed_hashes) == 8:
                return hashes, placed_hashes

    def part_a(self):
        hashes = self.parsed[0]
        return hashes[:8]

    def part_b(self):
        hashes = self.parsed[1]
        return "".join(hashes[index][0] for index in range(8))
