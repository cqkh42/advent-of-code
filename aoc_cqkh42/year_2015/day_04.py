import itertools
from functools import lru_cache
from hashlib import md5


@lru_cache(maxsize=None)
def _crack_hash(key, sequence, start=0):
    for answer in itertools.count(start):
        input_ = f'{key}{answer}'.encode()
        hashed = md5(input_).hexdigest()
        if hashed.startswith(sequence):
            return answer


def part_a(data):
    return _crack_hash(data, '00000')


def part_b(data, a):
    return _crack_hash(data, '000000', start=a)
