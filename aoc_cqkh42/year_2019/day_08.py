from collections import Counter

from aoc_cqkh42.helpers import aocr
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.helpers import make_chunks


def pixel_color(pixel):
    for level in pixel:
        if level != '2':
            return level
    else:
        return pixel[0]


def flatten_message(message, width, height):
    chunks = make_chunks(message, width * height)
    pixels = zip(*chunks)
    final_message = (pixel_color(pixel) for pixel in pixels)
    return final_message


class Solution(BaseSolution):
    def part_a(self):
        chunks = make_chunks(self.input_, 25 * 6)
        counters = [Counter(chunk) for chunk in chunks]
        scores = [(counter["0"], counter["1"] * counter["2"]) for counter in
                  counters]
        result = min(scores, key=lambda counter: counter[0])[1]
        return result

    def part_b(self):
        width = 25
        height = 6
        result = flatten_message(self.input_, width, height)
        return aocr.word(result, true='1')
