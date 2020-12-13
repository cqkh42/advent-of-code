import itertools


def _occupied_around(x, y, seats):
    contents = []

    x_s = (x-1, x, x + 1)
    y_s = (y-1, y, y+1)
    for x_, y_ in itertools.product(x_s, y_s):
        if (x_, y_) != (x, y) and x_ >= 0 and y_ >= 0:
            try:
                there = seats[y_][x_]
                contents.append(there)
            except IndexError:
                continue
    return contents.count('#')


def _new_value(around, state):
    if state == 'L' and not around:
        return '#'
    elif state == '#' and around >= 4:
        return 'L'
    else:
        return state


def _find_first_seat(xs, ys, seats):
    for y_, x_ in zip(ys, xs):
        if (seat := seats[y_][x_]) != '.':
            return seat



def _occupied_in_sight(x, y, seats):
    contents = []
    north = range(y-1, -1, -1)
    south = range(y+1, len(seats))
    east = range(x+1, len(seats[0]))
    west = range(x-1, -1, -1)
    vertical = itertools.repeat(y)
    horizontal = itertools.repeat(x)
    # find N
    n = _find_first_seat(itertools.repeat(x), north, seats)
    s = _find_first_seat(itertools.repeat(x), south, seats)
    contents.extend((n, s))
    #find S
    # for y_ in south:
    #     if (seat := seats[y_][x]) != '.':
    #         contents.append(seat)
    #         break
    # find E
    for x_ in east:
        if (seat := seats[y][x_]) != '.':
            contents.append(seat)
            break
    # find W
    for x_ in west:
        if seats[y][x_] != '.':
            contents.append(seats[y][x_])
            break
    #find NE
    angles = (
        _find_first_seat(x_dir, y_dir, seats)
        for y_dir, x_dir in itertools.product((north, south), (east, west))
    )
    contents.extend(angles)
    return contents.count('#')


def part_a(data):
    seats = data.split('\n')
    while True:
        new_seats = []
        for y_index, row in enumerate(seats):
            new_row = ''
            for x_index, seat in enumerate(row):
                around = _occupied_around(x_index, y_index, seats)
                new_seat = _new_value(around, seat)
                new_row += new_seat
            new_seats.append(new_row)
        if new_seats == seats:
            return ''.join(seats).count('#')

        else:
            seats = new_seats


def _new_value_2(around, state):
    if state == 'L' and not around:
        return '#'
    elif state == '#' and around >= 5:
        return 'L'
    else:
        return state


def part_b(data, **_):
    seats = data.split('\n')
    while True:
        new_seats = []
        for y_index, row in enumerate(seats):
            new_row = ''
            for x_index, seat in enumerate(row):
                around = _occupied_in_sight(x_index, y_index, seats)
                new_seat = _new_value_2(around, seat)
                new_row += new_seat
            new_seats.append(new_row)
        if new_seats == seats:
            return ''.join(seats).count('#')

        else:
            seats = new_seats
