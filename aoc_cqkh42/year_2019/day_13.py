from collections import Counter

from aoc_cqkh42.year_2019.computer import Computer
def make_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def part_a(data):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]
    computer = Computer(inputs, [])
    computer.run()
    results = computer.outputs

    chunks = make_chunks(results, 3)
    tiles = [chunk[2] for chunk in chunks]
    result = Counter(tiles)[2]
    return  result

def part_b(data, **_):
    inputs = data.split(",")
    inputs = [int(input_) for input_ in inputs]
    inputs[0] = 2
    computer = Computer(inputs, [])

    results = {}
    while True:
        try:
            computer.run()
        except IndexError:
            pass
        chunks = make_chunks(computer.outputs, 3)
        computer.outputs = []
        new_results = {tuple(i[:2]): i[2] for i in chunks}
        results.update(new_results)
        ball_x = [k for k, v in results.items() if v == 4][0][0]
        paddle_x = [k for k, v in results.items() if v == 3][0][0]
        if ball_x > paddle_x:
            computer.inputs.append(1)
        elif ball_x < paddle_x:
            computer.inputs.append(-1)
        else:
            computer.inputs.append(0)

        if not sum(i == 2 for i in results.values()):
            break
    result = results[(-1, 0)]
    return result