import itertools


def get_pattern(index):
    first_pattern = (
        itertools.repeat(0, index),
        itertools.repeat(1, index),
        itertools.repeat(0, index),
        itertools.repeat(-1, index),
    )
    pattern = itertools.chain.from_iterable(first_pattern)

    g = itertools.cycle(pattern)
    next(g)
    return g


def _get_patterns(signal):
    signal_length = len(signal)
    patterns = [
        get_pattern(index+1) for index in range(len(signal))
    ]
    patterns = [
        [next(iterator) for _ in range(signal_length)]
        for iterator in patterns
    ]
    return patterns


def process_loop(index, signal):
    pattern = get_pattern(index)
    z = (a * b for a, b in zip(signal, pattern))
    t = sum(z)
    return abs(t) % 10


def _process_loop(pattern, signal):
    z = (a * b for a, b in zip(signal, pattern))
    t = sum(z)
    return abs(t) % 10


def run_phases(signal, phases):
    patterns = _get_patterns(signal)

    for _ in range(phases):
        signal = [_process_loop(pattern, signal) for pattern in patterns]
    return signal


def do_iteration(numbers):
    sum_ = 0
    result = []
    for num in numbers[-1::-1]:
        sum_ += num
        result.append(sum_)
    result = [abs(num) % 10 for num in result]
    result.reverse()
    return result


def run_it_all(numbers, iters):
    for _ in range(iters):
        numbers = do_iteration(numbers)
    return "".join([str(i) for i in numbers[:8]])


def part_a(data):
    inputs = list(data)
    inputs = [int(num) for num in inputs]
    phased = run_phases(inputs, 100)[:8]
    r = [str(i) for i in phased]
    result = int("".join(r))
    return result


def part_b(data, **_):
    # return False
    listed = [int(num) for num in data] * 10000

    skip = int(data[:7])
    post_skip = listed[skip:]
    result = int(run_it_all(post_skip, 100))
    return result