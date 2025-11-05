from _md5 import md5 as md5_builtin
from collections import defaultdict
import itertools
from aoc_cqkh42.helpers.base_solution import BaseSolution


#todo hashes


class Solution(BaseSolution):

    def hasher(self):
        for index in itertools.count():
            string = (self.input_ + str(index)).encode()
            digest = md5_builtin(string).hexdigest()
            if digest.startswith("00000"):
                yield digest[5:7]

    def _parse(self):
        hashes = ""
        placed_hashes = [None] * 8
        hasher= self.hasher()

        while not all(placed_hashes):
            l, r = next(hasher)
            if len(hashes) < 8:
                hashes += l
            kk = int(l, 16)
            if kk < 8 and placed_hashes[kk] is None:
                placed_hashes[kk] = r
        return hashes, placed_hashes

    def part_a(self):
        return self.parsed[0]

    def part_b(self):
        hashes = self.parsed[1]
        return "".join(hashes)
