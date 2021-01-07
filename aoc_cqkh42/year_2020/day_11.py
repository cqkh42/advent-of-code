"""
Solutions for day 11 of 2020's Advent of Code

"""
import itertools


def _occupied_around(x, y, seats) -> int:
    x_s = (x-1, x, x + 1)
    y_s = (y-1, y, y+1)
    adjacent = (seats.get((x_, y_), False) for x_, y_ in itertools.product(x_s, y_s))
    return sum(adjacent) - seats[(x, y)]


def _new_value(seat, seats) -> bool:
    x, y = seat
    around = _occupied_around(x, y, seats)
    state = seats[(x, y)]
    if not state and not around:
        return True
    elif state and around >= 4:
        return False
    else:
        return state


def build_seat_dict(data):
    seats = {}
    for y, row in enumerate(data.split('\n')):
        for x, item in enumerate(row):
            if item != '.':
                seats[(x, y)] = False
    return seats


def part_a(data) -> int:
    """
    Solution for part a

    Parameters
    ----------
    data: str

    Returns
    -------
    answer: int

    """
    seats = build_seat_dict(data)

    for num in itertools.count():
        new_seats = {seat: _new_value(seat, seats) for seat in seats}
        unchanged = (new_seats[seat] == seats[seat] for seat in seats)
        if all(unchanged):
            return sum(seat for seat in seats.values())
        seats = new_seats


def _visible_from_seat(seat, seat_locations):
    x, y = seat
    found = []
    # N
    xs, ys = zip(*seat_locations)
    highest_x = max(xs)
    highest_y = max(ys)

    n = range(y-1, -1, -1)
    s = range(y+1, highest_y+1, 1)
    e=range(x+1, highest_x+1, 1)
    w = range(x-1, -1, -1)

    n_ = zip(itertools.repeat(x), n)
    s_ = zip(itertools.repeat(x), s)
    e_ = zip(e, itertools.repeat(y))
    w_ = zip(w, itertools.repeat(y))
    ne = zip(e, n)
    nw = zip(w, n)
    se = zip(e, s)
    sw = zip(w, s)
    for i in [ne, nw, se, sw, w_, e_, s_, n_]:
        i = (z for z in i if z in seat_locations)
        try:
            found.append(next(i))
        except StopIteration:
            pass
    return set(found)


def part_b(data, **_) -> int:
    """
    Solution for part b

    Parameters
    ----------
    data: str

    Returns
    -------
    answer: int

    """
    seats = build_seat_dict(data)
    seat_locations = frozenset(seats)
    visible = {seat: _visible_from_seat(seat, seat_locations) for seat in seats}
    # print(visible)

    for num in itertools.count():
        new_seats = {}
        for seat in seats:
            around = sum(seats[v] for v in visible[seat])
            current = seats[seat]
            if not current:
                new_seats[seat] = not bool(around)
            else:
                new_seats[seat] = around < 5
        unchanged = (new_seats[seat] == seats[seat] for seat in seats)
        if all(unchanged):
            return sum(seat for seat in seats.values())
        seats = new_seats


