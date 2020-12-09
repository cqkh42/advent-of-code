from collections import Counter, deque

from aoc_cqkh42.year_2019.computer import Computer

def path_to_coordinate(path):
    counts = Counter(path)
    x = counts.get(4, 0) - counts.get(3, 0)
    y = counts.get(1, 0) - counts.get(2, 0)
    return x, y

def winning_computer(data):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]
    visited = set()
    queue = [[inputs, 0, 0, []]]

    while True:
        intcode, pointer, relative_base, path = queue.pop(0)
        this_location = path_to_coordinate(path)
        if this_location in visited:
            continue
        else:
            visited.add(this_location)

        for next_ in range(1, 5):
            c = Computer(intcode, [next_])
            c.pointer = pointer
            c.relative_base = relative_base
            try:
                c.run()
            except IndexError:
                pass
            if c.output == 2:
                result = len(path) + 1
                break

            elif c.output == 1:
                queue.append(
                    [c.intcode, c.pointer, c.relative_base, [*path, next_]])
        else:
            continue
        break
    return c, result


def part_a(data):
    c, result = winning_computer(data)
    return result


def part_b(data, **_):
    c, result = winning_computer(data)
    intcode_at_zero = c.intcode
    pointer_at_zero = c.pointer
    relative_base_at_zero = c.relative_base

    visited = {}
    queue = [[intcode_at_zero, pointer_at_zero, relative_base_at_zero, []]]

    while len(queue):
        intcode, pointer, relative_base, path = queue.pop(-1)
        this_location = path_to_coordinate(path)
        if this_location in visited:
            continue
        else:
            visited[this_location] = len(path)

        for next_ in range(1, 5):
            c = Computer(intcode, [next_])
            c.pointer = pointer
            c.relative_base = relative_base
            try:
                c.run()
            except IndexError:
                pass

            if c.output == 1:
                queue.append(
                    [c.intcode, c.pointer, c.relative_base, [*path, next_]])
        else:
            continue
        break
    result = max(visited.values())
    return result

    return False