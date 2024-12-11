from functools import cache

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

@cache
def blink(stone: tuple):
    new_stone = []
    for num in stone:
        if num == 0:
            new_stone.append(1)
        elif len(str(num)) % 2 == 0:
            st = str(num)
            new_stone.append(int(st[:len(st)//2]))
            new_stone.append(int(st[len(st)//2:]))
        else:
            new_stone.append(num*2024)
    return tuple(new_stone)

@cache
def blink_repeatedly(stone, num):
    if num == 1:
        return blink(stone)
    else:
        stones = blink(stone)
        return blink_repeatedly(stones, num-1)

class Solution(BaseSolution):
    def part_a(self):
        total = 0
        for num in self.numbers:
            stone = tuple([num])
            # stone = blink_repeatedly
            for _ in range(25):
                stone = blink(stone)
            total += len(stone)
        return total

    def part_b(self):
        return
        total = 0
        for num in self.numbers:
            stone = tuple([num])
            for _ in range(75):
                stone = blink(stone)
            total += len(stone)
        return total


if __name__ == "__main__":
    submit_answers(Solution,11, 2024)
