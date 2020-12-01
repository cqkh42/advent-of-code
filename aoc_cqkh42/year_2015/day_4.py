from hashlib import md5


def _crack_hash(key, sequence, stop=1_000_000_000, start=0):
    for answer in range(start, stop):
        input_ = f'{key}{answer}'.encode()
        hashed = md5(input_).hexdigest()
        if hashed.startswith(sequence):
            return answer


def part_a(data):
    return _crack_hash(data, '00000')


def part_b(data, a):
    return _crack_hash(data, '000000', start=a)
