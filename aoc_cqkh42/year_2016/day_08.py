import itertools
import functools

import adventocr
import parse
import numpy as np


RECT_PARSER = parse.compile(r'rect {:d}x{:d}')
ROW_PARSER = parse.compile(r'rotate row y={:d} by {:d}')
COL_PARSER = parse.compile(r'rotate column x={:d} by {:d}')


@functools.lru_cache()
def create_screen(data):
    instructions = data.split('\n')
    screen = np.zeros((6, 50))
    for instruction in instructions:
        if instruction.startswith('rect'):
            x, y = RECT_PARSER.parse(instruction)
            screen[:y, :x] = 1
        elif 'row' in instruction:
            y, steps = ROW_PARSER.parse(instruction)
            screen[y] = np.roll(screen[y], steps)
        else:
            x, steps = COL_PARSER.parse(instruction)
            screen[:, x] = np.roll(screen[:, x], steps)
    return screen.astype(int)


def part_a(data):
    screen = create_screen(data)
    return screen.sum()


def part_b(data, **_):
    screen = create_screen(data)
    return adventocr.word(itertools.chain.from_iterable(screen))
