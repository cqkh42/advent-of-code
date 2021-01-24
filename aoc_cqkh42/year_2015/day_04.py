import itertools
from hashlib import md5

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    answer_a = None

    def parse_data(self):
        return md5(self.data.encode())

    def part_a(self):
        answer = self._crack_hash('00000')
        self.answer_a = answer
        return answer

    def part_b(self):
        return self._crack_hash('000000', start=self.answer_a)

    def _crack_hash(self, sequence, start=0):
        for answer in itertools.count(start):
            hashed = self.parsed_data.copy()
            hashed.update(f'{answer}'.encode())
            hashed = hashed.hexdigest()
            if hashed.startswith(sequence):
                return answer
