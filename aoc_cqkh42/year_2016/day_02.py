from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _find_code(self, pad):
        k = {
            (y, x): a for (y, b) in enumerate(pad) for x, a in enumerate(b)
            if a
        }
        code = ''

        x = 1
        y = 1

        for step in self.lines:
            for move in step:
                if move == 'D' and (y+1, x) in k:
                    y += 1
                elif move == 'U' and (y-1, x) in k:
                    y -= 1
                elif move == 'R' and (y, x+1) in k:
                    x += 1
                elif move == 'L' and (y, x-1) in k:
                    x -= 1
            code += str(k[y, x])
        return code

    def part_a(self):
        keys = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        return self._find_code(keys)

    def part_b(self):
        keys = [
            [None, None, 1, None, None],
            [None, 2, 3, 4, None],
            [5, 6, 7, 8, 9],
            [None, 'A', 'B', 'C', None],
            [None, None, 'D', None, None]
        ]
        return self._find_code(keys)