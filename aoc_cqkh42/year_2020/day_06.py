def part_a(data):
    groups = data.split('\n\n')
    as_one = (group.replace('\n', '') for group in groups)
    unique = (set(group) for group in as_one)
    return sum(len(group) for group in unique)


def part_b(data, **_):
    groups = data.split('\n\n')
    sub_groups = ((set(g) for g in group.split('\n')) for group in groups)
    intersections = (set.intersection(*groups) for groups in sub_groups)
    return sum(len(intersection) for intersection in intersections)
