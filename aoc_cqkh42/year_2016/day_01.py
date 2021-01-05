from collections import defaultdict

def part_a(data):
    directions = data.split(', ')
    compass = ('N', 'E', 'S', 'W')
    travelled = defaultdict(int)

    current_direction_index = 0

    for change, *distance in directions:
        if change == 'R':
            current_direction_index += 1
        else:
            current_direction_index -= 1
        current_direction_index %= 4
        current_direction = compass[current_direction_index]
        travelled[current_direction] += int(''.join(distance))

    return abs(travelled['E'] - travelled['W']) + abs(
        travelled['N'] - travelled['S'])


def part_b(data, **_):
    directions = data.split(', ')
    compass = ('N', 'E', 'S', 'W')
    visited = set((0, 0))
    travelled = defaultdict(int)

    current_direction_index = 0
    dir_changes = {'R': 1, 'L': -1}

    # directions = ['R8', 'R4', 'R4', 'R8']
    for change, *distance in directions:
        distance = int(''.join(distance))
        current_direction_index += dir_changes[change]
        current_direction = compass[current_direction_index % 4]
        try:
            for step in range(1, distance + 1):
                travelled[current_direction] += 1
                at = ((travelled['E'] - travelled['W']),
                      (travelled['N'] - travelled['S']))
                if at in visited:
                    return abs(at[0]) + abs(at[1])
                visited.add(at)
        except IndexError:
            break