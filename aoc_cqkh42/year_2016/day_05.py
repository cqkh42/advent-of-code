import hashlib
import itertools

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        hashes = ''
        placed_hashes = [''] * 8
        base_hash = hashlib.md5(self.data.encode())
        for index in itertools.count():
            hashed = base_hash.copy()
            hashed.update(str(index).encode())
            hashed = hashed.hexdigest()
            start, k, v = hashed[:5], hashed[5], hashed[6]
            if start == '0'*5:
                if len(hashes) < 8:
                    hashes += k
                try:
                    z = int(k)
                    if z < 8 and not placed_hashes[z]:
                        placed_hashes[z] = v
                except ValueError:
                    continue
            if all(placed_hashes):
                return hashes, placed_hashes

    def part_a(self):
        hashes = self.parsed_data[0]
        return hashes

    def part_b(self):
        hashes = self.parsed_data[1]
        return ''.join(hashes)
