from dataclasses import dataclass, field

from aoc_cqkh42.helpers.base_solution import BaseSolution

WINNING_OPTIONS = [
    {(0, row) for row in range(5)},
    {(1, row) for row in range(5)},
    {(2, row) for row in range(5)},
    {(3, row) for row in range(5)},
    {(col, 0) for col in range(5)},
    {(col, 1) for col in range(5)},
    {(col, 2) for col in range(5)},
    {(col, 3) for col in range(5)},
    {(col, 4) for col in range(5)},
]


@dataclass
class Board:
    numbers: dict  # mapping is int: position
    marked: set = field(default_factory=set)

    def is_complete(self):
        return any(option.issubset(self.marked) for option in WINNING_OPTIONS)

    def score(self, last_called):
        unmarked = [num for num, index in self.numbers.items() if index not in self.marked]
        return sum(unmarked) * last_called


class Solution(BaseSolution):
    numbers: list
    boards: list

    def _make_board(self, board_list):
        mappings = {}
        for row_index, row in enumerate(board_list):
            for col_index, item in enumerate(row):
                mappings[int(item)] = (row_index, col_index)
        return Board(mappings)

    def _process_data(self):
        numbers, _, *boards = self.lines
        self.numbers = [int(num) for num in numbers.split(',')]
        boards = [row.split() for row in boards if row]
        boards = [boards[row:row + 5] for row in range(0, len(boards), 5)]
        return [self._make_board(board) for board in boards]

    def part_a(self):
        for number in self.numbers:
            for board in self.parsed_data:
                board.marked.add(board.numbers.get(number))
                if board.is_complete():
                    return board.score(number)

    def part_b(self):
        for number in self.numbers:
            for board in self.parsed_data:
                board.marked.add(board.numbers.get(number))
            self.parsed_data = [board for board in self.parsed_data if not board.is_complete()]
            if not self.parsed_data:
                return board.score(number)
