import itertools
import re
from collections import defaultdict
from hashlib import md5

from more_itertools import ilen, first

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    triple_re = re.compile(r"(.)\1\1")
    fiver = re.compile(r"(.)\1\1\1\1")

    def stretched_hash(self, salt, times):
        a = md5(f"{self.input_}{salt}".encode())
        a = a.hexdigest()
        for _ in range(times - 1):
            a = md5(a.encode())
            a = a.hexdigest()
        return a

    def hash(self, num, triples, keys, times):
        a = self.stretched_hash(num, times)

        z = itertools.groupby(a)
        y = ((x, ilen(y)) for x, y in z)
        xx = (a for a, b in y if b >= 3)
        if match := first(xx, default=None):
            triples[match].add(num)

        z = itertools.groupby(a)
        y = ((x, ilen(y)) for x, y in z)
        if match := self.fiver.search(a):
            char = match.groups(0)[0]
            #     # did we see a triple in the last 1000:
            r = range(num - 1000, num)
            if z := triples[char].intersection(r):
                keys.update(z)
        return triples, keys

    def part_a(self):
        triples = defaultdict(set)
        keys = set()
        for num in itertools.count():
            triples, keys = self.hash(num, triples, keys, 1)
            if len(keys) >= 64:
                return sorted(keys)[63]

    def part_b(self):
        triples = defaultdict(set)
        keys = set()
        for num in itertools.count():
            triples, keys = self.hash(num, triples, keys, 2017)
            if len(keys) >= 64:
                return sorted(keys)[63]


if __name__ == "__main__":
    submit_answers(Solution, 14, 2016)
