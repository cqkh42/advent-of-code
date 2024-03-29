import itertools
from _md5 import md5 as md5_builtin

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _process_data(self):
        hashes = ''
        placed_hashes = [''] * 8
        base_hash = md5_builtin(self.input_.encode())

        for index in itertools.count():
            hashed = base_hash.copy()
            hashed.update(b'%a' % index)

            digest = hashed.hexdigest()
            if digest.startswith('0' * 5):
                kk = int(digest[5], 16)
                hashes += digest[5]
                if kk < 8 and not placed_hashes[kk]:
                    placed_hashes[kk] = digest[6]
                if all(placed_hashes):
                    return hashes, placed_hashes

    def part_a(self):
        hashes = self.processed[0]
        return hashes[:8]

    def part_b(self):
        hashes = self.processed[1]
        return ''.join(hashes)
