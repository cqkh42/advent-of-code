from collections import defaultdict
import itertools
from hashlib import md5
import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    triple_re = re.compile(r'(.)\1\1')
    fiver = re.compile(r'(.)\1\1\1\1')

    def stretched_hash(self, salt, times):
        a = md5(f'{self.data}{salt}'.encode())
        a = a.hexdigest()
        for _ in range(times-1):
            a = md5(a.encode())
            a = a.hexdigest()
        return a

    def hash(self, num, triples, keys, times):
        a = self.stretched_hash(num, times)
        if match := self.triple_re.search(a):
            char = match.groups(0)[0]
            triples[char].add(num)
        if match := self.fiver.search(a):
            char = match.groups(0)[0]
            #     # did we see a triple in the last 1000:
            r = range(num-1000, num)
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


