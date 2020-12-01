import re


def part_a(data):
    row, col = re.findall(r'\d+', data)
    row = int(row)
    col = int(col)

    triangle_number = col + row - 1
    that_number = triangle_number * (triangle_number + 1) / 2
    my_number = int(that_number - row)

    start = 20151125
    for _ in range(my_number):
        start *= 252533
        start %= 33554393

    return start


def part_b(**_):
    return None
