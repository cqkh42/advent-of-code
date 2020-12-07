def run_intcode(intcode):
    pointer = 0
    while True:
        code = intcode[pointer]
        if code == 99:
            return intcode
        a, b, location = intcode[pointer+1:pointer+4]
        if code == 1:
            intcode[location] = intcode[a] + intcode[b]
        elif code == 2:
            intcode[location] = intcode[a] * intcode[b]
        pointer += 4


def parse_string(string):
    return [int(num) for num in string.split(',')]


def get_output(intcode):
    return run_intcode(intcode)[0]