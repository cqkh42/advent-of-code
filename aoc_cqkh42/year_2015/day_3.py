def _trace_path(steps):
    mapping_dict = {'>': ('x', 1), '<': ('x', -1), '^': ('y', 1), 'v': ('y', -1)}
    mapped = [mapping_dict[step] for step in steps]

    visited = {(0, 0)}
    current = {'x': 0, 'y': 0}
    for direction, increment in mapped:
        current[direction] += increment
        visited.add((current['x'], current['y']))

    return visited


def part_a(data):
    return len(_trace_path(data))


def part_b(data, **_):
    santa = data[::2]
    robo_santa = data[1::2]

    santa_visited = _trace_path(santa)
    robo_visited = _trace_path(robo_santa)
    all_visited = {*santa_visited, *robo_visited}
    return len(all_visited)
