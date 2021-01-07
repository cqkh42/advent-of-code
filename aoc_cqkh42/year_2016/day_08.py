import itertools
import functools

import adventocr


@functools.lru_cache()
def create_screen(data):
    instructions = data.split('\n')
    screen = [[0 for _ in range(50)] for _ in range(6)]
    for instruction in instructions:
        parts = instruction.split()
        if parts[0] == 'rect':
            x, y = parts[1].split('x')
            x, y = int(x), int(y)
            for line in range(y):
                screen[line][:x] = [1 for _ in range(x)]
        elif parts[0] == 'rotate' and parts[1] == 'row':
            y = int(parts[2].split('=')[1])
            steps = int(parts[-1])
            screen[y] = screen[y][-steps:] + screen[y][:-steps]
        elif parts[0] == 'rotate' and parts[1] == 'column':
            x = int(parts[2].split('=')[1])
            steps = int(parts[-1])
            existing = [line[x] for line in screen]
            new_col = existing[-steps:] + existing[:-steps]
            for line, val in enumerate(new_col):
                screen[line][x] = val
    return screen


def part_a(data):
    screen = create_screen(data)
    return sum(itertools.chain.from_iterable(screen))


def part_b(data, **_):
    screen = create_screen(data)
    return adventocr.word(itertools.chain.from_iterable(screen))
