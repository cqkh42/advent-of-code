from collections import defaultdict

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def calc_perimeter(region):
    total = 0
    for x, y in region:
        if (x+1, y) not in region:
            total += 1
        if (x-1, y) not in region:
            total += 1
        if (x, y+1) not in region:
            total += 1
        if (x, y-1) not in region:
            total += 1
    return total
#todo grid
class Solution(BaseSolution):
    def grid(self):
        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                yield (x_index, y_index), value

    def part_a(self):
        regions = defaultdict(list)
        for (x, y), letter in self.grid():
            surround = {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}
            surround = {(x, y) for x, y in surround if 0 <=x < len(self.lines[0]) and 0<= y < self.num_lines}
            for region in regions[letter]:
                if surround.intersection(region):
                    region.add((x, y))
                    break
            else:
                regions[letter].append({(x, y),})

        t = 0
        # I 12 20 wrong
        # I 2 6 wrong

        print()
        for letter in regions:
            for seg in regions[letter]:
                print(letter, len(seg), calc_perimeter(seg))
                t += calc_perimeter(seg) * len(seg)
        return t
    # 808456 is too low

    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,12, 2024)
