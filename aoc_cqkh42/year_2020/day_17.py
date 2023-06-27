import itertools
from collections import defaultdict


def around(coords):
    ranges = [
        (coord-1, coord, coord+1)
        for coord in coords
    ]
    a = (coords_ for coords_ in itertools.product(*ranges) if coords != coords_)
    return a


def _new_state(alive, coords):
    a = around(coords)
    alive_around = sum(alive[cell] for cell in a)
    if alive[coords]:
        return alive_around in [2, 3]
    else:
        return alive_around == 3


def part_a(data):
    alive = defaultdict(bool)
    for y, row in enumerate(data.split('\n')):
        for x, item in enumerate(row):
            alive[(x, y, 0)] = item == '#'

    opening_x = len(data.split('\n')[0])
    opening_y = len(data.split('\n'))
    for outwards in range(1, 7):
        x_range = range(-outwards, opening_x+outwards+1)
        y_range = range(-outwards, opening_y+outwards+1)
        z_range = range(-outwards, outwards+1)
        new_alive = {}
        for coords in itertools.product(x_range, y_range, z_range):
            new_state = _new_state(alive, coords)
            new_alive[coords] = new_state
        alive.update(new_alive)
    return sum(alive.values())


def part_b(data, **_):
    alive = defaultdict(bool)
    for y, row in enumerate(data.split('\n')):
        for x, item in enumerate(row):
            alive[(x, y, 0, 0)] = item == '#'
    opening_x = len(data.split('\n')[0])
    opening_y = len(data.split('\n'))
    for outwards in range(1, 7):
        x_range = range(-outwards, opening_x+outwards+1)
        y_range = range(-outwards, opening_y+outwards+1)
        z_range = range(-outwards, outwards+1)
        w_range = range(-outwards, outwards+1)
        new_alive = {}
        for coords in itertools.product(x_range, y_range, z_range, w_range):
            new_state = _new_state(alive, coords)
            new_alive[coords] = new_state
        alive.update(new_alive)
    return sum(alive.values())
