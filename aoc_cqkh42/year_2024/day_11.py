from functools import cache

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

@cache
def blink_num(num: int, iterations:int):
    if iterations == 1:
        if len(str(num)) % 2 == 0:
            return 2
        else:
            return 1
    else:
        if num == 0:
            return blink_num(1, iterations-1)
        elif len(str(num)) % 2 == 0:
            st = str(num)
            a = int(st[:len(st)//2])
            b = int(st[len(st)//2:])
            return blink_num(a, iterations-1) + blink_num(b, iterations-1)
        else:
            return blink_num(num*2024, iterations-1)


class Solution(BaseSolution):
    def part_a(self):
        return sum(blink_num(num, 25) for num in self.numbers)

    def part_b(self):
        return sum(blink_num(num, 75) for num in self.numbers)2


if __name__ == "__main__":
    submit_answers(Solution,11, 2024)
