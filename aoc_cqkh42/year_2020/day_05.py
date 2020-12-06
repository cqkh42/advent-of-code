def _row(boarding):
    row = boarding.replace('F', '0').replace('B', '1')
    row = ''.join(char for char in row if char in '01')
    return int(row, 2)


def _col(boarding):
    col = boarding.replace('L', '0').replace('R', '1')
    col = ''.join(char for char in col if char in '01')
    return int(col, 2)


def _seat_id(boarding):
    row = _row(boarding)
    col = _col(boarding)
    return (row * 8) + col


def part_a(data):
    ids = (_seat_id(boarding) for boarding in data.split('\n'))
    return max(ids)


def part_b(data, **_):
    ids = [_seat_id(boarding) for boarding in data.split('\n')]
    all_seats = range(min(ids), max(ids))
    missing_ids = (seat for seat in all_seats if seat not in ids)
    return next(missing_ids)