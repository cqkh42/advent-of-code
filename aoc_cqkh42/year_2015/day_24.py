import itertools
import math


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

def part_a(data):
    parcels = data.split('\n')
    parcels = {int(parcel) for parcel in parcels}
    group_a = find_smallest_groups(parcels, 3)

    min_length = min(len(group) for group in group_a)
    group_a = (group for group in group_a if
               len(group) == min_length and valid_group(group, parcels, 3, min_length))
    return min(math.prod(group) for group in group_a)


def part_b(data, **_):
    parcel = data
    parcels = data.split('\n')
    parcels = [int(parcel) for parcel in parcels]
    group_a = find_smallest_groups(parcels, 4)

    min_length = min(len(group) for group in group_a)
    group_a = (group for group in group_a if
               len(group) == min_length and valid_group(group, parcels, 4, min_length))
    return min(math.prod(group) for group in group_a)
