def is_even(num):
    return not num % 2


def iteration(instr, x, index):
    if instr[0] == 'jio' and x[instr[1]] == 1:
        index += instr[2]
        return x, index
    elif instr[0] == 'jie' and is_even(x[instr[1]]):
        index += instr[2]
        return x, index
    elif instr[0] == 'jmp':
        index += int(instr[1])
        return x, index
    elif instr[0] == "inc":
        x[instr[1]] += 1
    elif instr[0] == 'tpl':
        x[instr[1]] *= 3
    elif instr[0] == 'hlf':
        x[instr[1]] *= 0.5

    index += 1
    return x, index

def part_a(data, target='b'):
    instructions = data.split('\n')
    instructions = [tuple(instr.replace(',', '').replace('+', '').split(' '))
                    for instr in instructions]
    instructions = [[i if not i.isnumeric() else int(i) for i in instr] for
                    instr in instructions]

    registers = {'a': 0, 'b': 0}
    index = 0



    while index in range(len(instructions)):
        instr = instructions[index]
        registers, index = iteration(instr, registers, index)

    return registers[target]


def part_b(data, **_):
    instructions = data.split('\n')
    instructions = [tuple(instr.replace(',', '').replace('+', '').split(' '))
                    for instr in instructions]
    instructions = [[i if not i.isnumeric() else int(i) for i in instr] for
                    instr in instructions]

    registers = {'a': 1, 'b': 0}
    index = 0

    while index in range(len(instructions)):
        instr = instructions[index]
        registers, index = iteration(instr, registers, index)

    return registers['b']
