import itertools

from aoc_cqkh42.year_2019.computer import Computer


def horizontal_intersections(scaffolding):
    for row_index, row in enumerate(scaffolding):
        z = zip(row, row[1:], row[2:])
        for index, zz in enumerate(z):
            if set(zz) == {"#"}:
                yield row_index, index+1


def vertical_intersections(scaffolding):
    for row_index, row in enumerate(zip(*scaffolding)):
        z = zip(row, row[1:], row[2:])
        for index, zz in enumerate(z):
            if set(zz) == {"#"}:
                yield index+1, row_index


def build_scaffolding(intcode):
    computer = Computer(intcode, [])
    computer.run()
    scaffolding = computer.outputs
    scaffolding = "".join([chr(i) for i in scaffolding])
    scaffolding = scaffolding.split("\n")[:-2]
    sc = [list(i) for i in scaffolding]

    return sc

def move(current, movement):
    move_dict = {
        ("U", "L"): "L",
        ("U", "R"): "R",
        ("R", "L"): "U",
        ("R", "R"): "D",
        ("D", "L"): "R",
        ("D", "R"): "L",
        ("L", "L"): "D",
        ("L", "R"): "U"
    }
    return move_dict[(current, movement)]


def part_a(data):
    inputs = data.split(",")
    intcode = [int(input_) for input_ in inputs]
    scaffolding = build_scaffolding(intcode)

    hors = set(horizontal_intersections(scaffolding))
    vert = set(vertical_intersections(scaffolding))

    result = sum(
        [(coords[0] * coords[1]) for coords in hors.intersection(vert)])
    return result


def current_location(sc):
    for a, row in enumerate(sc):
        for c, item in enumerate(row):
            if item in ["^", ">", "v", "<"]:
                return a, c


def part_b(data, **_):
    intcode = [int(input_) for input_ in data.split(',')]
    scaffolding = build_scaffolding(intcode)
    print('\n')
    for row in scaffolding:
        print(''.join(row))

    start_location = current_location(scaffolding)


    current_direction = "U"

    step_map = {
        "A": [("R", 4), ("R", 12), ("R", 10), ("L", 12)],
        "B": [("L", 12), ("R", 4), ("R", 12)],
        "C": [("L", 12), ("L", 8), ("R", 10), ]
    }

    step_letters = ["A", "B", "B", "C", "C", "A", "B", "B", "C", "A"]

    steps = [step_map[step] for step in step_letters]
    y, x = current_location(scaffolding)

    for direction, distance in itertools.chain.from_iterable(steps):
        current_direction = move(current_direction, direction)

        track = ['X' for _ in range(distance)]
        if current_direction == "R":
            new_x = x + distance
            new_y = y
            scaffolding[y][x:new_x] = track
        elif current_direction == "L":
            new_x = x - distance
            new_y = y
            scaffolding[y][new_x+1:x+1] = track
        elif current_direction == "D":
            new_y = y + distance
            new_x = x
            multiplier = 1
            for step in range(distance):
                scaffolding[y+(step*multiplier)][x] = track
        elif current_direction == "U":
            new_y = y - distance
            new_x = x
            multiplier = -1
            for step in range(distance):
                scaffolding[y+(step*multiplier)][x] = track
        y = new_y
        x = new_x
    intcode[0] = 2
    movements = [ord(char) for char in ",".join(step_letters)]
    y = [ord(char) for char in
         ",".join([str(a) for b in step_map["A"] for a in b])]
    b = [ord(char) for char in
         ",".join([str(a) for b in step_map["B"] for a in b])]
    x = [ord(char) for char in
         ",".join([str(a) for b in step_map["C"] for a in b])]
    view = ord("n")
    newline = ord("\n")
    instructions = [*movements, newline, *y, newline, *b, newline, *x, newline,
                    view, newline]
    computer = Computer(intcode, instructions)
    computer.run()
    result = computer.outputs[-1]
    return result