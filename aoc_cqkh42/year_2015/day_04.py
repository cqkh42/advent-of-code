import itertools
from hashlib import md5

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    counter = 0

    def parse_data(self):
        return md5(self.data.encode())

    def part_a(self):
        return self._crack_hash('00000')

    def part_b(self):
        return self._crack_hash('000000')

    def _crack_hash(self, sequence):
        for answer in itertools.count(self.counter):
            hashed = self.parsed_data.copy()
            hashed.update(f'{answer}'.encode())
            hashed = hashed.hexdigest()
            if hashed.startswith(sequence):
                return answer
