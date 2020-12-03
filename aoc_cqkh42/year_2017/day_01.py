def _compare_indices(string, jump):
    index_ahead = (
        int((index + jump) % len(string))
        for index in range(len(string))
    )
    matches = (
        int(string[i]) for i, v in enumerate(index_ahead)
        if string[i] == string[v]
    )
    return sum(matches)


def part_a(data):
    return _compare_indices(data, 1)


def part_b(data, **_):
    jump = len(data) / 2
    return _compare_indices(data, jump)
