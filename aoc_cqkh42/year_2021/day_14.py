from collections import Counter
from functools import cache

from aoc_cqkh42 import BaseSolution

from frozendict import frozendict
import parse
import regex

@cache
def replace(polymer, mapping):
    new = ''
    # if it fails here it because we assume we always have a map
    for a,b in zip(polymer, polymer[1:]):
        new += a + mapping[a+b]
    new += polymer[-1]
    return new

@cache
def multiple_replace(polymer, mapping, num):
    for _ in range(num):
        polymer = replace(polymer, mapping)
    return polymer


class Solution(BaseSolution):
    parser = parse.compile(r'{:l} -> {:l}')
    ten_map = {}

    def parse_data(self):
        self.polymer = self.lines[0]
        p = frozendict(self.parser.findall(self.data))
        self.regex = regex.compile('|'.join(p))
        return p

    def rreplace(self, polymer, old):
        new = old[0] + self.parsed_data[old] + old[1]
        li = self.polymer.rsplit(old, 1)
        self.polymer = new.join(li)

    def replace(self, polymer):
        matches = self.regex.findall(polymer, overlapped=True)
        for old in reversed(matches):
            self.rreplace(self.polymer, old)

    def do(self):
        new_polymer = ''
        for pair in zip(self.polymer, self.polymer[1:]):
            new = multiple_replace(pair, self.parsed_data, 10)
            new_polymer += new[:-1]
        new_polymer += self.polymer[-1]
        self.polymer = new_polymer

    def part_a(self):
        self.do()
        c = Counter(self.polymer)
        most, *_, least = c.most_common()
        return most[1] - least[1]

    def part_b(self):
        self.do()
        self.do()
        self.do()
        c = Counter(self.polymer)
        most, *_, least = c.most_common()
        return most[1] - least[1]

