# TODO HASH
import itertools
from _md5 import md5

from aocd import get_data

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    counter = itertools.count()

    def _crack_hash(self, sequence):
        for answer in self.counter:
            hash_ = self.parsed_data.copy()
            hash_.update(f"{answer}".encode())
            if hash_.hexdigest().startswith(sequence):
                return answer

    def _parse_data(self):
        return md5(self.data.encode())

    def part_a(self):
        answer = self._crack_hash("0" * 5)
        return answer

    def part_b(self):
        return self._crack_hash("0" * 6)


if __name__ == "__main__":
    data = get_data(
        session="53616c7465645f5f7578abb37529958ea6c4839cbbeeb414870a119609f21ea219dd7295504325ddb3aa309f17baa02e1a0c67d897449610aa0d811e4d721457",
        day=4,
        year=2015,
    )
    solution = Solution(data).part_a()
    # submit(solution.part_a(), part='a', day=4, year=2015,
    #        session='53616c7465645f5f7578abb37529958ea6c4839cbbeeb414870a119609f21ea219dd7295504325ddb3aa309f17baa02e1a0c67d897449610aa0d811e4d721457')
    # submit(solution.part_b(), part='b', day=4, year=2015,
    #        session='53616c7465645f5f7578abb37529958ea6c4839cbbeeb414870a119609f21ea219dd7295504325ddb3aa309f17baa02e1a0c67d897449610aa0d811e4d721457')
