def run_program(instructions, registers):
    instructions = [instruction.split() for instruction in instructions]
    index = 0
    while True:
        try:
            cmd, input_1, *values = instructions[index]
        except IndexError:
            return registers['a']
        else:
            incr = 1
            if cmd == 'cpy':
                val = registers.get(input_1, input_1)
                registers[values[0]] = int(val)
            elif cmd == 'inc':
                registers[input_1] += 1
            elif cmd == 'dec':
                registers[input_1] -= 1
            elif cmd == 'jnz':
                val = registers.get(input_1, input_1)
                if int(val):
                    incr = int(values[0])
            index += incr


def part_a(data):
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    instructions = data.split('\n')
    return run_program(instructions, registers)


def part_b(data, **_):
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    instructions = data.split('\n')
    return run_program(instructions, registers)
