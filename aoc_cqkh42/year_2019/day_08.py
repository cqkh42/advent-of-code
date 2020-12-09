from collections import Counter

def make_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def flatten_message(message, width, height):
    final_message = []

    chunks = make_chunks(message, width * height)
    pixels = zip(*chunks)
    final_message = []
    for pixel in pixels:
        colours = [i for i in pixel if i != "2"]
        if colours:
            pixel = colours[0]
        else:
            pixel = "2"
        final_message.append(pixel)
    final_message = "".join(final_message)
    return final_message


def print_message(message, width):
    chunks = make_chunks(message, width)
    for chunk in chunks:
        x = [i if i=="1" else " "for i in chunk]
        print("".join(x))


def part_a(data):
    chunks = make_chunks(data, 25 * 6)
    counters = [Counter(chunk) for chunk in chunks]
    scores = [(counter["0"], counter["1"] * counter["2"]) for counter in
              counters]
    result = min(scores, key=lambda counter: counter[0])[1]
    return result


mappings = {
    ' 11  \n1  1 \n1    \n1    \n1  1 \n 11  ': 'C',
    '1111 \n1    \n111  \n1    \n1    \n1111 ': 'E',
    '1  1 \n1 1  \n11   \n1 1  \n1 1  \n1  1 ': 'K',
    '1  1 \n1  1 \n1  1 \n1  1 \n1  1 \n 11  ': 'U',
    ' 11  \n1  1 \n1  1 \n1111 \n1  1 \n1  1 ': 'A',
    '1111 \n   1 \n  1  \n 1   \n1    \n1111 ': 'Z',
    '1   1\n1   1\n 1 1 \n  1  \n  1  \n  1  ': 'Y',
    '111  \n1  1 \n111  \n1  1 \n1  1 \n111  ': 'B',
    '1    \n1    \n1    \n1    \n1    \n1111 ': 'L',
    '1  1 \n1  1 \n1111 \n1  1 \n1  1 \n1  1 ': 'H',
    '1111 \n1    \n111  \n1    \n1    \n1    ': 'F'
}


def get_letter(string, index):
    starts = [((num*25)+(index*5)) for num in range(6)]
    sliced = [string[start:start+5] for start in starts]
    sliced = '\n'.join(sliced).replace('0', ' ')
    return mappings[sliced]


def part_b(data, **_):
    width = 25
    height = 6
    result = flatten_message(data, width, height)
    return ''.join([get_letter(result, index) for index in range(5)])
