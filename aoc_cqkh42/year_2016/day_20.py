import itertools

import parse

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        parser = parse.compile('{:d}-{:d}')
        rs = parser.findall(self.data)
        rs = sorted([(a, b) for a, b in rs])

        guess = rs[0][1]
        for ranged in rs:
            if guess not in range(ranged[0], ranged[1] + 1):
                continue
                # print(guess)
            else:
                guess = ranged[1] + 1
        return guess

    def part_b(self):
        parser = parse.compile('{:d}-{:d}')
        rs = parser.findall(self.parsed_data)
        rs = sorted([(a, b) for a, b in rs], key=lambda x: x[0])
        ranges = []

        current = list(rs[0])

        for start, end in rs:
            if start <= current[1] + 1:
                current[1] = max(end, current[1])
                # print(guess)
            else:
                ranges.append(current)
                current = [start, end]
        ranges.append(current)
        ranges = [range(a, b + 1) for a, b in ranges]
        bad_count = sum(len(i) for i in ranges)
        return 4294967295 + 1 - bad_count



        for first, second in zip(rs, rs[1:]):
            if second[0] <= first[1]+1:
                continue
            else:
                return second[1]+1