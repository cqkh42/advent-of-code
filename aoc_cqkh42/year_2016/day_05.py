import hashlib
import functools
import itertools


@functools.lru_cache
def find_hashes(door):
    hashes = []
    placed_hashes = [None]*8
    for index in itertools.count():
        hashed = hashlib.md5(f'{door}{index}'.encode()).hexdigest()
        if hashed.startswith('0'*5):
            hashes.append(hashed[5])
            if hashed[5] in '01234567' and placed_hashes[int(hashed[5])] is None:
                placed_hashes[int(hashed[5])] = hashed[6]
            if None not in placed_hashes:
                return hashes[:8], placed_hashes


def part_a(data):
    hashes = find_hashes(data)[0]
    return ''.join(hashes)


def part_b(data, **_):
    hashes = find_hashes(data)[1]
    return ''.join(hashes)