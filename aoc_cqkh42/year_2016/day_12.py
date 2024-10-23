from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers



class Solution(BaseSolution):
    def part_a(self):
        c = Computer(self.input_)
        c.run()
        return c.registers['a']

    def part_b(self):
        c = Computer(self.input_)
        c.registers['c'] = 1
        c.run()
        return c.registers['a']

def compile_instruction(instructions):
    commands = [i[0] for i in instructions]
    if commands[:3] == ['inc', 'dec', 'jnz']:
        from_ = instructions[1][1]
        to_ = instructions[0][1]
        new_instruction = ['add_a', to_, from_]
        return new_instruction
    elif commands[:3] == ['dec', 'inc', 'jnz']:
        from_ = instructions[0][1]
        to_ = instructions[1][1]
        new_instruction = ['add_b', from_, to_]
        return new_instruction
    if commands[:6] == ['cpy', 'add_a', 'dec', 'jnz', 'dec', 'jnz']:
        mul_1 = instructions[0][1]
        mul_2 = instructions[4][1]
        to_ = instructions[1][1]
        nulling = instructions[0][2]
        new_instruction = ['mul', mul_1, nulling, mul_2, to_]
        return new_instruction
    if commands[:6] == ['cpy', 'add_b', 'inc', 'jnz', 'dec', 'jnz']:
        mul_1 = instructions[0][1]
        mul_2 = instructions[4][1]
        to_ = instructions[2][1]
        nulling = instructions[0][2]
        new_instruction = ['mul', mul_1, nulling, mul_2, to_]
        return new_instruction


class Computer:
    def __init__(self, instructions):
        self.instructions = [
            instruction.split() for instruction in instructions.split('\n')
        ]
        self.instructions = self.compile_instructions()
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.index = 0
        self.outputs = [1]

    def __getitem__(self, item):
        value = self.registers.get(item, item)
        try:
            return int(value)
        except TypeError:
            return value

    def __setitem__(self, key, value):
        self.registers[key] = value

    def compile_instructions(self):
        for index in range(len(self.instructions)):
            instructions = tuple(self.instructions[index:index+6])
            new_instruction = compile_instruction(instructions)
            if new_instruction:
                self.instructions[index] = new_instruction
        return self.instructions


    def run_step(self):
        cmd, input_1, *values = self.instructions[self.index]
        incr = 1
        if cmd == 'cpy':
            self[values[0]] = self[input_1]
        elif cmd == 'inc':
            self[input_1] += 1
        elif cmd == 'dec':
            self[input_1] -= 1
        elif cmd == 'jnz':
            if self[input_1]:
                incr = self[values[0]]
        elif cmd == 'add_a':
            self[input_1] += self[values[0]]
            self[values[0]] = 0
            incr=3
        elif cmd == 'add_b':
            self[values[0]] += self[input_1]
            self[input_1] = 0
            incr=3
        elif cmd == 'mul':
            self[values[2]] += (self[input_1] * self[values[1]])
            self[values[0]] = 0
            incr = 6
        elif cmd == 'tgl':
            focus = self.index + self[input_1]
            try:
                toggled = process_toggle(
                    self.instructions[focus])
                self.instructions[focus] = toggled
            except IndexError:
                pass
            else:
                self.instructions = self.compile_instructions()
        elif cmd == 'out':
            if self[input_1] not in {0, 1} or self[input_1] == self.outputs[-1] or len(self.outputs) > 12:
                incr = float('inf')
            self.outputs.append(self[input_1])
        self.index += incr

    def run(self):
        while self.index < len(self.instructions):
            try:
                self.run_step()
            except (TypeError, ValueError):
                self.index += 1


def process_toggle(instruction):
    cmd, input_1, *values = instruction
    mapping = {
        'inc': 'dec',
        'dec': 'inc',
        'jnz': 'cpy',
        'cpy': 'jnz',
        'tgl': 'inc',
        'add_a': 'dec',
        'add_b': 'inc',
        'mul': 'jnz'
    }
    return mapping[cmd], input_1, *values


if __name__ == "__main__":
    submit_answers(Solution, 12, 2016)