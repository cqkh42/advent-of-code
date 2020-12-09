import itertools


def _is_valid(preamble, target):
    sums = (sum(nums) for nums in itertools.combinations(preamble, 2))
    equal_target = (sum_ == target for sum_ in sums)
    return any(equal_target)


def _find_sequence(numbers, target):
    slice_indices = itertools.combinations(range(len(numbers)+1), 2)
    slices = (numbers[start:end] for start, end in slice_indices)
    for sliced in slices:
        if sum(sliced) == target:
            return sliced
    return False


def part_a(data, preamble=25):
    numbers = [int(num) for num in data.split('\n')]
    preambles = (
        numbers[start:start+preamble] for start in range(len(data)-preamble)
    )
    targets = numbers[preamble:]
    invalids = (
        target for preamble, target in zip(preambles, targets)
        if not _is_valid(preamble, target)
    )
    return next(invalids)


def part_b(data, a):
    numbers = [int(num) for num in data.split('\n')]
    sequence = _find_sequence(numbers, a)
    return min(sequence) + max(sequence)
