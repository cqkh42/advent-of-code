from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return self.data.split('\n')

    def _find_code(self, pad):
        k = {}
        for row_index, row in enumerate(pad):
            for col_index, col in enumerate(row):
                if col:
                    k[(row_index, col_index)] = col

        code = ''

        x = 1
        y = 1

        for step in self.parsed_data:
            for move in step:
                if move == 'D' and k.get((y + 1, x)):
                    y += 1
                elif move == 'U' and k.get((y - 1, x)):
                    y = max(0, y - 1)
                elif move == 'R' and k.get((y, x + 1)):
                    x += 1
                elif move == 'L' and k.get((y, x - 1)):
                    x = max(0, x - 1)
            code += str(pad[y][x])
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