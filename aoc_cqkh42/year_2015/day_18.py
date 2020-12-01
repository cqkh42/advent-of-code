import itertools

def _new_state(x, y, lights):
    around_it = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x + 1, y), (x - 1, y - 1), (x, y - 1),
                 (x + 1, y - 1)]

    lit = sum([lights.get(light) == '#' for light in around_it])
    if lights[(x, y)] == '#':
        if lit == 2 or lit == 3:
            return '#'
        return '.'
    else:
        if lit == 3:
            return '#'
        return '.'


def part_a(data, steps=100):
    light_string = data.split('\n')
    lights = {}
    for y_index, row in enumerate(light_string):
        for x_index, item in enumerate(row):
            lights[(x_index, y_index)] = item

    for _ in range(steps):
        lights = {light: _new_state(*light, lights) for light in lights}
    return sum([light == '#' for light in lights.values()])


def part_b(data, steps=100, **_):
    light_string = data
    light_string = light_string.split('\n')
    end_of_x = len(light_string[0]) - 1
    end_of_y = len(light_string) - 1

    lights = {}
    for y_index, row in enumerate(light_string):
        for x_index, item in enumerate(row):
            lights[(x_index, y_index)] = item
    lights[(0, 0)] = '#'
    lights[(0, end_of_y)] = '#'
    lights[(end_of_x, 0)] = '#'
    lights[(end_of_x, end_of_y)] = '#'

    for _ in range(steps):
        lights = {light: _new_state(*light, lights) for light in lights}
        lights[(0, 0)] = '#'
        lights[(end_of_x, 0)] = '#'
        lights[(0, end_of_y)] = '#'
        lights[(end_of_x, end_of_y)] = '#'
    return sum([light == '#' for light in lights.values()])
