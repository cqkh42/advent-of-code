import itertools

from aoc_cqkh42 import BaseSolution

import more_itertools
import parse
import numpy as np

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
        if head[1] - tail[1] == 2:
            y_move = 1
        elif head[1] - tail[1] == -2:
            y_move = -1
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


def chase(steps, tail=(0,0)):
    tail_locations = [tail]
    for head in steps:
        if not touching(head, tail):
            tail = move(head, tail)
        tail_locations.append(tail)
    return tail_locations



class Solution(BaseSolution):
    parser = parse.compile('{:l} {:d}')
    tail = (0, 0)

    def parse_data(self):
        movements = more_itertools.run_length.decode(self.parser.findall(self.data))
        dicts = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        return list(itertools.accumulate((dicts[i] for i in movements), initial=np.array([0,0])))

    def part_a(self):
        places = chase(self.parsed_data)
        return len(set(places))

    def part_b(self):
        k_1 = chase(self.parsed_data)
        k_2 = chase(k_1)
        k_3 = chase(k_2)
        k_4 = chase(k_3)
        k_5 = chase(k_4)
        k_6 = chase(k_5)
        k_7 = chase(k_6)
        k_8 = chase(k_7)
        k_9 = chase(k_8)
        return len(set(k_9))