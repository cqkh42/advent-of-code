def exists(x, y, keys):
    try:
        val = keys[y][x]
    except IndexError:
        return False
    else:
        return bool(val)


def part_a(data):
    steps = data.split('\n')
    keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    code = []

    x = 1
    y = 1

    for step in steps:
        for move in step:
            if move == 'D' and exists(x, y + 1, keys):
                y += 1
            elif move == 'U' and exists(x, y - 1, keys):
                y = max(0, y - 1)
            elif move == 'R' and exists(x + 1, y, keys):
                x += 1
            elif move == 'L' and exists(x - 1, y, keys):
                x = max(0, x - 1)
        code.append(keys[y][x])

    return ''.join([str(num) for num in code])


def part_b(data, **_):
    steps = data.split('\n')

    keys = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ]

    code = []

    x = 0
    y = 2

    for step in steps:
        for move in step:
            if move == 'D' and exists(x, y + 1, keys):
                y += 1
            elif move == 'U' and exists(x, y - 1, keys):
                y = max(0, y - 1)
            elif move == 'R' and exists(x + 1, y, keys):
                x += 1
            elif move == 'L' and exists(x - 1, y, keys):
                x = max(0, x - 1)
        code.append(keys[y][x])

    return ''.join([str(num) for num in code])