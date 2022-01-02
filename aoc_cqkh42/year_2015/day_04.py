import itertools
from _md5 import md5

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    counter = 0

    def _crack_hash(self, sequence):
        for answer in itertools.count(self.counter):
            hashed = self.parsed_data.copy()
            hashed.update(f'{answer}'.encode())
            hashed = hashed.hexdigest()
            if hashed.startswith(sequence):
                return answer

    def parse_data(self):
        return md5(self.data.encode())

    def part_a(self):
        return self._crack_hash('0'*5)

    def part_b(self):
        return self._crack_hash('0'*6)

