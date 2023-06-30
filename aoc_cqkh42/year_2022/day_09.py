import itertools

import more_itertools
import numpy as np
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


# TODO move is messy here

def touching(head, tail):
    x = abs(head[0] - tail[0])
    y = abs(head[1] - tail[1])

    return x <= 1 and y <= 1


def move(head, tail):
    x_move = 0
    y_move = 0
    if head[1] == tail[1] and head[0] > tail[0]:
        x_move = 1
    elif head[1] == tail[1] and head[0] < tail[0]:
        x_move = -1
    # do we need a vertical move (y not x)
    elif head[1] != tail[1] and head[0] == tail[0]:
        y_move = (-1) ** (1 + (head[1] - tail[1] > 0))
    else:
        # we are going to do a diagonal
        if head[1] > tail[1]:
            y_move = 1
        else:
            y_move = -1
        if head[0] > tail[0]:
            x_move = 1
        else:
            x_move = -1
    return tail[0] + x_move, tail[1] + y_move


def chase(steps, tail=(0, 0)):
    tail_locations = [tail]
    for head in steps:
        if not touching(head, tail):
            tail = move(head, tail)
        tail_locations.append(tail)
    return tail_locations


class Solution(BaseSolution):
    parser = parse.compile('{:l} {:d}')
    tail = (0, 0)

    def _parse_data(self):
        movements = more_itertools.run_length.decode(
            self.parser.findall(self.data))
        dicts = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        return list(itertools.accumulate((dicts[i] for i in movements),
                                         initial=np.array([0, 0])))

    def part_a(self):
        places = chase(self.parsed_data)
        return len(set(places))

    def part_b(self):
        k = self.parsed_data
        for i in range(9):
            k = chase(k)
        return len(set(k))
