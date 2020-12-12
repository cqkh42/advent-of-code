import itertools


def _parse_floor(data):
    seats = {}
    for y, row in enumerate(data.split('\n')):
        for x, item in enumerate(row):
            if item == 'L':
                seats[(x, y)] = 'L'
    return seats


def _count_adjacent_seats(x, y, seats):
    x_s = (x-1, x, x + 1)
    y_s = (y-1, y, y+1)
    occupied = (
        seats.get((x_, y_)) == '#' for x_, y_ in itertools.product(x_s, y_s)
        if (x_, y_) != (x, y)
    )
    occupied = sum(occupied)
    return occupied


def _new_state(x, y, seats):
    occupied = _count_adjacent_seats(x, y, seats)
    if seats[(x, y)] == 'L' and not occupied:
        return '#'
    if seats[(x, y)] == '#' and occupied >= 4:
        return 'L'
    return seats[x, y]


def _update_seats(seats):
    new_seats = {(x, y): _new_state(x, y, seats) for x, y in seats}
    return {**seats, **new_seats}


def _find_seats_in_sight(x, y, seats):
    occupied = 0
    #find N

    #find S
    # find E
    # find W
    #find NE
    # find SE
    #find SW



def part_a(data):
    seats = _parse_floor(data)
    while True:
        new_seats = _update_seats(seats)
        if seats == new_seats:
            return sum(val == '#' for val in seats.values())
        else:
            seats = new_seats


def part_b(data, **_):
    return False
