from aoc_cqkh42.helpers.base_solution import BaseSolution

DISC_LENGTH = 272
TRANS = str.maketrans('01', '10')


def dragon_curve(a, length):
    b = a[::-1].translate(TRANS)
    # a = a+'0'+b
    if len(a)*2+1 < length:
        return dragon_curve(a+'0'+b, length)
    return (a+'0'+b)[:length]


def checksum(num):
    pairs = zip(num[::2], num[1::2])
    p = ''.join('1' if a == b else '0' for a, b in pairs)
    if not len(p) % 2:
        return checksum(p)
    return p


class Solution(BaseSolution):
    def _dragon_curve(self, length):
        b = self.input_[::-1].translate(TRANS)
        self.input_ += '0' + b
        if len(self.input_) < length:
            return self._dragon_curve(length)
        return self.input_[:length]

    def part_a(self):
        b = self._dragon_curve(272)
        return checksum(b)

    def part_b(self):
        b = dragon_curve(self.input_, 35651584)
        return checksum(b)
