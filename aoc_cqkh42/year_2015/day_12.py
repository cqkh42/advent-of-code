import json
import re


def part_a(data):
    numbers = re.findall(r'-?\d+', data)
    numbers = [int(num) for num in numbers]
    return sum(numbers)


def part_b(data, **_):
    data = json.loads(data)
    if isinstance(data, dict):
        data = [data]
    answer = 0

    for item in data:
        if isinstance(item, int):
            answer += item
        elif isinstance(item, list):
            data.extend(item)
        elif isinstance(item, dict) and 'red' not in item.values():
            data.extend(item.values())
    return answer
