from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        instructions = self.data.split('\n')
        instructions = [
            tuple(instr.replace(',', '').replace('+', '').split(' '))
            for instr in instructions]
        instructions = [[i if not i.isnumeric() else int(i) for i in instr] for
                        instr in instructions]
        return instructions

    def part_a(self, target='b'):
        registers = {'a': 0, 'b': 0}
        return self.run(registers)

    def part_b(self):
        registers = {'a': 1, 'b': 0}
        return self.run(registers)

    def run(self, registers):
        index = 0
        while True:
            try:
                instr = self.parsed_data[index]
                registers, index = iteration(instr, registers, index)
            except IndexError:
                return registers['b']

def is_even(num):
    return not num % 2


def iteration(instr, x, index):
    incr = 1
    i = instr[1]
    o = instr[0]
    if o == 'jio' and x[i] == 1:
        incr = instr[2]
    elif o == 'jie' and is_even(x[i]):
        incr = instr[2]
    elif o == 'jmp':
        incr = int(i)
    elif o == "inc":
        x[i] += 1
    elif o == 'tpl':
        x[i] *= 3
    elif o == 'hlf':
        x[i] *= 0.5

    return x, index+incr
