import itertools

from aoc_cqkh42 import BaseSolution

import more_itertools
import parse

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

def move_big_rope(rope):
    new_rope = [rope[0]]
    first = rope[0]
    for second in rope[1:]:
        if not touching(first, second):
            new_place = move(first, second)
        else:
            new_place = second
        new_rope.append(new_place)
        first = new_place
    return new_rope



class Solution(BaseSolution):
    parser = parse.compile('{:l} {:d}')
    tail = (0, 0)

    def parse_data(self):
        locations = [(0, 0)]
        movements = more_itertools.run_length.decode(self.parser.findall(self.data))
        for direction in movements:
            x, y = locations[-1]
            if direction == 'R':
                locations.append((x+1, y))
            elif direction == 'L':
                locations.append((x-1, y))
            elif direction == 'U':
                locations.append((x, y+1))
            elif direction == 'D':
                locations.append((x, y-1))
        return locations

    def part_a(self):
        tail = (0, 0)
        tail_locations = {tail}
        for head in self.parsed_data:
            if not touching(head, tail):
                tail = move(head, tail)
            tail_locations.add(tail)
        return len(tail_locations)

    def part_b(self):
        return
        rope = [self.parsed_data[0], *((0,0) for _ in range(9))]
        final_locations = {(0, 0)}
        for head in self.parsed_data[1:]:
            rope[-1] = head
            rope = move_big_rope(rope)
            final_locations.add(rope[-1])
        print(final_locations)
        return len(final_locations)
