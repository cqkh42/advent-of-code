def _count_lights(instructions, mapping):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in instructions:
        line = line.replace('turn ', '')
        action, start, __, end = line.split()

        x_start, y_start = [int(num) for num in start.split(',')]
        x_end, y_end = [int(num) for num in end.split(',')]

        f = mapping[action]

        for x in range(x_start, x_end + 1):
            new_lights = [f(light) for light in lights[x][y_start:y_end + 1]]
            lights[x][y_start:y_end + 1] = new_lights
    return sum([light for row in lights for light in row])


def part_a(data):
    instructions = data.split('\n')
    mapping = {
        'on': lambda light: 1,
        'off': lambda light: 0,
        'toggle': lambda light: not light
    }
    return _count_lights(instructions, mapping)


def part_b(data, **_):
    instructions = data.split('\n')
    mapping = {
        'on': lambda light: light + 1,
        'off': lambda light: max(light - 1, 0),
        'toggle': lambda light: light + 2
    }
    return _count_lights(instructions, mapping)
