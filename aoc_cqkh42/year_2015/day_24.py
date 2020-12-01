import itertools
import functools
import math

def part_a(data):
    parcels = data
    parcels = parcels.split('\n')
    parcels = [int(parcel) for parcel in parcels]

    def valid_group(group):
        still_to_sort = [parcel for parcel in parcels if parcel not in group]
        # can we split this to be two equal sizes
        group_b = (itertools.combinations(still_to_sort, length) for length in
                   range(min_length, len(still_to_sort)))
        group_b = (group for group in itertools.chain.from_iterable(group_b) if
                   sum(group) == each_weight)
        return any(group_b)

    each_weight = sum(parcels) / 3

    for fewest in range(1, len(parcels)):
        if sum(parcels[-fewest:]) >= each_weight:
            break

    group_a = (itertools.combinations(parcels, length) for length in
               range(fewest, (len(parcels) // 3) + 1))
    group_a = [group for group in itertools.chain.from_iterable(group_a) if
               sum(group) == each_weight]

    min_length = min({len(group) for group in group_a})
    group_a = (group for group in group_a if
               len(group) == min_length and valid_group(group))
    return min(math.prod(group) for group in group_a)


def part_b(data, **_):
    parcels = data
    parcels = parcels.split('\n')
    parcels = [int(parcel) for parcel in parcels]

    def valid_group(group):
        still_to_sort = [parcel for parcel in parcels if parcel not in group]
        # can we split this to be two equal sizes
        group_b = (itertools.combinations(still_to_sort, length) for length in
                   range(min_length, len(still_to_sort)))
        group_b = (group for group in itertools.chain.from_iterable(group_b) if
                   sum(group) == each_weight)
        return any(group_b)

    each_weight = sum(parcels) / 4

    for fewest in range(1, len(parcels)):
        if sum(parcels[-fewest:]) >= each_weight:
            break

    group_a = (itertools.combinations(parcels, length) for length in
               range(fewest, (len(parcels) // 4) + 1))
    group_a = [group for group in itertools.chain.from_iterable(group_a) if
               sum(group) == each_weight]

    min_length = min({len(group) for group in group_a})
    group_a = (group for group in group_a if
               len(group) == min_length and valid_group(group))
    return min(math.prod(group) for group in group_a)
