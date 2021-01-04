import itertools
import math


def algorithm_u(ns, m):
    def visit(n, a):
        ps = [[] for i in range(m)]
        for j in range(n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def f(mu, nu, sigma, n, a):
        if mu == 2:
            yield visit(n, a)
        else:
            for v in f(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v
        if nu == mu + 1:
            a[mu] = mu - 1
            yield visit(n, a)
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                yield visit(n, a)
        elif nu > mu + 1:
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = mu - 1
            else:
                a[mu] = mu - 1
            if (a[nu] + sigma) % 2 == 1:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v

    def b(mu, nu, sigma, n, a):
        if nu == mu + 1:
            while a[nu] < mu - 1:
                yield visit(n, a)
                a[nu] = a[nu] + 1
            yield visit(n, a)
            a[mu] = 0
        elif nu > mu + 1:
            if (a[nu] + sigma) % 2 == 1:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] < mu - 1:
                a[nu] = a[nu] + 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = 0
            else:
                a[mu] = 0
        if mu == 2:
            yield visit(n, a)
        else:
            for v in b(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v

    n = len(ns)
    a = [0] * (n + 1)
    for j in range(1, m + 1):
        a[n - m + j] = j - 1
    return f(m, n, 0, n, a)


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
    possible_bundles = (algorithm_u(list(parcels), num))
    group_a = find_smallest_groups(parcels, num)

    min_length = min(len(group) for group in group_a)
    group_a = (group for group in group_a if
               len(group) == min_length and valid_group(group, parcels, num, min_length))
    return min(math.prod(group) for group in group_a)


def part_a(data):
    parcels = data.split('\n')
    return zz(parcels, 3)


def part_b(data, **_):
    parcels = data.split('\n')
    return zz(parcels, 4)

