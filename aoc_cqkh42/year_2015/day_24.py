import functools
import itertools
import math


@functools.lru_cache(maxsize=None)
def contains_subset_equal_to(set_, target):
    s = sorted(set_)
    for c in itertools.count(1):
        if sum(s[:c]) >= target:
            max_needed = c
            break

    for c in itertools.count(1):
        if sum(s[-c:]) >= target:
            min_needed = c
            break
    for size in range(min_needed, max_needed + 1):
        possibles = itertools.combinations(set_, size)
        yield (comb for comb in possibles if sum(comb) == target)
    return False


def find_smallest_groups(parcels, num):
    group_weight = sum(parcels) / num
    fewest_size = math.ceil(len(parcels) / num)

    smallest_groups = (
        itertools.combinations(parcels, length)
        for length in range(1, fewest_size)
    )
    smallest_groups = [
        group for group in itertools.chain.from_iterable(smallest_groups)
        if sum(group) == group_weight
    ]
    return smallest_groups


def valid_group(group, parcels, num, min_length):
    each_weight = sum(parcels) / num

    still_to_sort = parcels.difference(group)
    # can we split this to be two equal sizes
    group_b = (itertools.combinations(still_to_sort, length) for length in
               range(min_length, len(still_to_sort)))
    group_b = (group for group in itertools.chain.from_iterable(group_b) if
               sum(group) == each_weight)
    return any(group_b)


def zz(parcels, num):
    parcels = {int(parcel) for parcel in parcels}
    group_a = find_smallest_groups(parcels, num)

    min_length = min(len(group) for group in group_a)
    group_a = (group for group in group_a if
               len(group) == min_length and valid_group(group, parcels, num, min_length))
    return min(math.prod(group) for group in group_a)


def part_a(data):
    parcels = data.split('\n')
    parcels = [int(i) for i in parcels]

    packages = frozenset(parcels)
    total_weight = sum(packages)
    group_weight = total_weight / 3

    possible_first_groups = contains_subset_equal_to(packages, group_weight)

    for size in possible_first_groups:
        results = []
        for group in size:
            others = packages.difference()
            if contains_subset_equal_to(others, group_weight):
                results.append(group)
        if results:
            break

    answer = min(math.prod(group) for group in results)
    return answer


def part_b(data, **_):
    parcels = data.split('\n')
    parcels = [int(i) for i in parcels]

    packages = frozenset(parcels)
    total_weight = sum(packages)
    group_weight = total_weight / 4
    possible_first_groups = contains_subset_equal_to(packages, group_weight)
    #
    for size in possible_first_groups:
        results = []
        for group in size:
            others = packages.difference()
            if (bits := contains_subset_equal_to(others, group_weight)):
                for three_four in bits:
                    k = others.difference(bits)
                    if contains_subset_equal_to(k, group_weight):
                        results.append(group)
        if results:
            break
    answer = min(math.prod(group) for group in results)
    return answer
