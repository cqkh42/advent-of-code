from collections import Counter, defaultdict
from functools import reduce, lru_cache
import math
import itertools

def s(num):
    p = prime_factorize(num)
    top = math.prod(s_relative(p, k) for p,k in p.items())
    return top

@lru_cache(maxsize=1_000_000)
def s_relative(p, k):
    return (p**(k+1) - 1) / (p-1)

@lru_cache(maxsize=1_000_000)
def prime_factorize(num):
    factors = defaultdict(int)
    while num >= 2:
        until = int(num**0.5) + 1
        for factor in range(2, until):
            if not num % factor:
                factors[factor] += 1
                break
        else:
            factors[num] += 1
            return factors
        num //= factor

def find_smallest(func, target, start):
    value = start
    while func(value) < target:
        value += 1
    return value


def _increasing_combinations(item):
    return itertools.chain.from_iterable(
        itertools.combinations(item, length) for length in
        range(1, len(item) + 1))


def sum_multiples(num):
    t = num / 50
    primes = prime_factorize(num)
    prime_factors = [[num] * count for num, count in primes.items()]
    prime_factors = [a for b in prime_factors for a in b]

    divisors = (math.prod(primes) for primes in
                _increasing_combinations(prime_factors))
    divisors = {div for div in divisors if div >= t}
    return sum(divisors)

def part_a(data):
    target = int(data)
    return find_smallest(lambda num: s(num) * 10, target, 2)



def part_b(data, **_):
    target = int(data)
    return find_smallest(lambda num: sum_multiples(num) * 11, target, 2)
