import hashlib

import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution

#todo compass coords
class Solution(BaseSolution):
    def _parse(self):
        to_visit = [(0, 0, "")]
        while True:
            try:
                x, y, steps = to_visit.pop(0)
            except IndexError:
                return
            if x == y == 3:
                yield steps
                continue
            c = self.input_ + steps
            digest = hashlib.md5(c.encode()).hexdigest()[:4]
            u, d, l, r = (char in "bcdef" for char in digest)
            if u and y - 1 >= 0:
                to_visit.append((x, y - 1, steps + "U"))
            if d and y + 1 <= 3:
                to_visit.append((x, y + 1, steps + "D"))
            if l and x - 1 >= 0:
                to_visit.append((x - 1, y, steps + "L"))
            if r and x + 1 <= 3:
                to_visit.append((x + 1, y, steps + "R"))

    def part_a(self):
        return next(self.parsed)

    def part_b(self):
        return len(more_itertools.last(self.parsed))
