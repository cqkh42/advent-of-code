import itertools


def replace_occurence(string, old, new, occurence):
    return string.replace(old, '$$$', occurence - 1).replace(old, new, 1).replace('$$$', old)


def part_a(data):
    *maps, _, element = data.split('\n')
    maps = [item.split(' => ') for item in maps]

    new_strings = set()
    for old, new in maps:
        count = element.count(old)
        for occurence in range(1, count + 1):
            new_string = element.replace(old, '$$$', occurence - 1).replace(old, new, 1).replace('$$$', old)
            new_strings.add(new_string)
    return len(new_strings)


def try_permutation(maps, element):
    visited = set()
    replaced = 0
    while element != 'e':
        for new, old in maps:
            if old not in element:
                continue
            element = element.replace(old, new, 1)
            if element in visited:
                return None
            visited.add(element)
            replaced += 1
    return replaced


def part_b(data, **_):
    maps = data
    *maps, _, element = maps.split('\n')
    maps = [item.split(' => ') for item in maps]
    possible_orders = itertools.permutations(maps)
    for order in possible_orders:
        result = try_permutation(order, element)
        if result:
            return result
