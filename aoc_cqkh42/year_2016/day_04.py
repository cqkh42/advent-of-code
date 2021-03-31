from collections import Counter
import itertools
import re
import string

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        rooms = self.data.split('\n')
        rooms = [re.search(r'([a-z\-]+)-(\d+)\[([a-z]+)\]', room).groups() for room
                 in rooms]

        real = [(encrypted, sector, checksum) for encrypted, sector, checksum in
                rooms if make_checksum(encrypted) == checksum]
        return sum(int(room[1]) for room in real)

    def part_b(self):
        rooms = self.data.split('\n')
        rooms = [re.search(r'([a-z\-]+)-(\d+)\[([a-z]+)\]', room).groups() for room
                 in rooms]

        real = [(encrypted, sector, checksum) for encrypted, sector, checksum in
                rooms if make_checksum(encrypted) == checksum]
        decrypted = {decrypt_room(room): room for room in real}
        return decrypted['northpole object storage'][1]

def make_checksum(encrypted):
    counted = Counter(encrypted.replace('-', ''))
    in_order = sorted(counted.items(), key=lambda x: (-x[1], x[0]))[:5]
    in_order = [letter for letter, count in in_order]
    return ''.join(in_order)




def decrypt_letter(char, sector):
    if char == '-':
        return ' '
    return string.ascii_lowercase[(string.ascii_lowercase.index(char)+(sector%26))%26]

def decrypt_room(room):
    return ''.join([decrypt_letter(char, int(room[1])) for char in room[0]])

