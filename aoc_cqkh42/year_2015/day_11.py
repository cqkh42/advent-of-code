import itertools

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        ords = [ord(char) - 97 for char in self.input_]
        for index, char in enumerate(ords):
            if char in [8, 14, 11]:
                ords[index] += 1
                ords[index + 1 :] = [0] * (len(ords) - index - 1)
                break
        return ords

    def part_a(self):
        return self.next_valid_password()

    def part_b(self):
        return self.next_valid_password()

    def cycle_password(self):
        for index in range(len(self.parsed) - 1, -1, -1):
            if num := self.parsed[index] != 25:
                self.parsed[index] += 1 + (num in [7, 13, 10])
                break
            self.parsed[index] = 0

    def next_valid_password(self):
        self.cycle_password()
        while not _is_valid(self.parsed):
            self.cycle_password()
        return "".join(chr(index + 97) for index in self.parsed)


def _is_valid(password):
    # TODO this is messy
    match_triples = any(
        first == second - 1 == third - 2
        for first, second, third in more_itertools.triplewise(password)
    )

    counts = [len(list(b)) for a, b in itertools.groupby(password)]
    counts = [i >= 2 for i in counts]
    match_counts = sum(counts) >= 2
    return match_counts and match_triples and 8 not in password


if __name__ == "__main__":
    submit_answers(Solution, 11, 2015)
