from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
import more_itertools
from collections import deque
import itertools


def solve(players: int, marbles: int) -> int:
    board = deque([0])
    scores = [0] * players
    for marble, turn in zip(range(1, marbles + 1), itertools.cycle(range(players))):
        # print(board)
        if marble % 23:
            board.rotate(-1)
            board.append(marble)
        else:
            scores[turn] += marble
            board.rotate(7)
            scores[turn] += board.pop()
            board.rotate(-1)
    return max(scores)

class Solution(BaseSolution):
    def part_a(self):
        return solve(*self.numbers)

    def part_b(self):
        players, marbles = self.numbers
        return solve(players, marbles*100)

if __name__ == "__main__":
    submit_answers(Solution,9, 2018)
