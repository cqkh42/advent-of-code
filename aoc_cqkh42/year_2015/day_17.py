from collections import Counter
import itertools


def _increasing_combinations(item):
    return itertools.chain.from_iterable(itertools.combinations(item, length) for length in range(1, len(item) + 1))


def part_a(data, target=150):
    containers = [int(container) for container in data.split('\n')]
    container_combinations = _increasing_combinations(containers)
    valid_containers = (sum(group) == target for group in container_combinations)
    return sum(valid_containers)


def part_b(data, target=150, **_):
    containers = [int(container) for container in data.split('\n')]
    container_combinations = _increasing_combinations(containers)
    valid_containers = [len(group) for group in container_combinations if sum(group) == target]
    lowest = min(valid_containers)
    return valid_containers.count(lowest)

