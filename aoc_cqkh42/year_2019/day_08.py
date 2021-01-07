from collections import Counter

import aocr

def make_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


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


def part_a(data):
    chunks = make_chunks(data, 25 * 6)
    counters = [Counter(chunk) for chunk in chunks]
    scores = [(counter["0"], counter["1"] * counter["2"]) for counter in
              counters]
    result = min(scores, key=lambda counter: counter[0])[1]
    return result


def part_b(data, **_):
    width = 25
    height = 6
    result = flatten_message(data, width, height)
    return aocr.word(result)
