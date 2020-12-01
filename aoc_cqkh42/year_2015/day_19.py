def part_a(data):
    *maps, _, element = data.split('\n')
    maps = [item.split(' => ') for item in maps]

    new_strings = []
    for old, new in maps:
        count = element.count(old)
        for occurence in range(1, count + 1):
            new_string = element.replace(old, '$$$', occurence - 1).replace(old, new, 1).replace('$$$', old)
            new_strings.append(new_string)

    return len(set(new_strings))


def part_b(data, **_):

    *maps, _, element = data.split('\n')
    maps = [item.split(' => ') for item in maps]
    return maps, element

    replaced = 0
    while element != 'e':
        for new, old in maps:
            if old not in element:
                continue
            element = element.replace(old, new, 1)
            replaced += 1
    return replaced
