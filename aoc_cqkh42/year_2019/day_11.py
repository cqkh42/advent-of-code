from collections import defaultdict

from aoc_cqkh42.year_2019.computer import Computer


def calc_turn(direction, turn):
    t = 90 if turn else - 90
    return (direction + t) % 360


def move(position, direction):
    if direction == 0:
        position = (position[0], position[1] + 1)
    elif direction == 90:
        position = (position[0] + 1, position[1])
    elif direction == 180:
        position = (position[0], position[1] - 1)
    elif direction == 270:
        position = (position[0] - 1, position[1])

    return position


def process_square(computer, position, direction, results):
    computer.inputs = [results.get(position, 0)]
    computer.outputs = []
    while len(computer.outputs) < 2:
        computer.run_iteration()
    colour, turn = computer.outputs
    results[position] = colour
    direction = calc_turn(direction, turn)
    position = move(position, direction)
    return computer, position, direction, results


def run(inputs, start_colour):
    # start on a square
    position = (0, 0)
    direction = 0
    results = {position: start_colour}
    computer = Computer(inputs, [])
    while True:
        try:
            computer, position, direction, results = process_square(computer, position, direction, results)
        except StopIteration:
            return results


def part_a(data):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]
    return len(run(inputs, 0))


mappings = {
    ' 11  \n1  1 \n1    \n1    \n1  1 \n 11  ': 'C',
    '1111 \n1    \n111  \n1    \n1    \n1111 ': 'E',
    '1  1 \n1 1  \n11   \n1 1  \n1 1  \n1  1 ': 'K',
    '1  1 \n1  1 \n1  1 \n1  1 \n1  1 \n 11  ': 'U',
    ' 11  \n1  1 \n1  1 \n1111 \n1  1 \n1  1 ': 'A',
    '1111 \n   1 \n  1  \n 1   \n1    \n1111 ': 'Z',
    '1   1\n1   1\n 1 1 \n  1  \n  1  \n  1  ': 'Y',
    '111  \n1  1 \n111  \n1  1 \n1  1 \n111  ': 'B',
    '1    \n1    \n1    \n1    \n1    \n1111 ': 'L',
    '1  1 \n1  1 \n1111 \n1  1 \n1  1 \n1  1 ': 'H',
    '1111 \n1    \n111  \n1    \n1    \n1    ': 'F',
    '111  \n1  1 \n1  1 \n111  \n1 1  \n1  1 ': 'R',
    '111  \n1  1 \n1  1 \n111  \n1    \n1    ': 'P',
    ' 11  \n1  1 \n1    \n1 11 \n1  1 \n 111 ': 'G'
}


def get_letter(string, index):
    starts = [((num*40)+(index*5)) for num in range(6)]
    sliced = [string[start:start+5] for start in starts]
    sliced = '\n'.join(sliced).replace('0', ' ')
    return mappings[sliced]


def part_b(data, **_):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]
    results = run(inputs, 1)
    d = defaultdict(dict)
    for (x, y), colour in results.items():
        d[y][x] = colour
    rows = []
    for key in sorted(d, key=lambda x: -x):
        xs = d[key]
        max_x = max(xs)
        row = ["1" if xs.get(x, 0) else " " for x in range(0, max_x + 1)]
        rows.append(row)
    rows = [row[1:41] for row in rows]
    master = ''.join([a for b in rows for a in b])
    letters = ''.join(get_letter(master, i) for i in range(8))
    return letters
