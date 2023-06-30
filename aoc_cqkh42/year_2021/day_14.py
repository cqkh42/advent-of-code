from collections import Counter, defaultdict

import parse
from frozendict import frozendict

# old SKNHVVBSCOPFHKFBKSPNVFFPFVBBKPVBCBVHSHHOHVVFVFFPFHHVNBBCBCBBKSPVKSSBPNVOONHFC
# old = {'V': 12, 'B': 12, 'F': 10, 'H': 9, 'S': 7, 'P': 7, 'K': 6, 'N': 5, 'C': 5, 'O': 4}
# new = {'B': 12, 'V': 11.5, 'H': 9, 'F': 7, 'S': 7, 'K': 6, 'P': 6, 'C': 5, 'N': 5, 'O': 4}
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile(r'{:l} -> {:l}')

    def parse_data(self):
        self.original_polymer = self.lines[0]
        p = frozendict(self.parser.findall(self.data))
        self.polymer = Counter((a+b for a, b in zip(self.lines[0], self.lines[0][1:])))
        return p

    def run(self):
        new = defaultdict(int)
        for (a, b), v in self.polymer.items():
            l = a + self.parsed_data[a+b]
            r = self.parsed_data[a+b] + b
            new[l] += v
            new[r] += v
        self.polymer = new

    def flat(self):
        final = Counter({self.original_polymer[0]: 1, self.original_polymer[-1]: 1})
        for (a, b), v in self.polymer.items():
            final[a] += v
            final[b] += v
        final = Counter({k: v // 2 for k, v in final.items()})
        return final

    def count(self):
        mc = self.flat().most_common()
        return mc[0][1] - mc[-1][1]

    def part_a(self):
        for _ in range(10):
            self.run()
        return self.count()

    def part_b(self):
        for _ in range(30):
            self.run()
        return self.count()

