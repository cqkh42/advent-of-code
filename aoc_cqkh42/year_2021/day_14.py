from collections import Counter

from aoc_cqkh42 import BaseSolution

from frozendict import frozendict
import parse
import regex


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

    def part_a(self):
        # for pair in zip(self.polymer, self.polymer[1:]):
        #     for _ in range(10):

        for _ in range(10):
            self.replace(self.polymer)
        c = Counter(self.polymer)
        most, *_, least = c.most_common()
        return most[1] - least[1]

    def part_b(self):
        self.polymer = self.polymer[:2]
        for _ in range(1):
            # print(self.polymer)
            self.replace()
        print(self.polymer)
        c = Counter(self.polymer)
        most, *_, least = c.most_common()
        return most[1] - least[1]

