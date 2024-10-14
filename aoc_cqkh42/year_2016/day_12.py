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


class Computer:
    def __init__(self, instructions):
        self.instructions = [
            instruction.split() for instruction in instructions.split('\n')
        ]
        # for i in self.instructions:
        #     print(i)
        # print()
        self.compile_instructions()
        # for i in self.instructions:
        #     print(i)
        # raise
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.index = 0

    def compile_instructions(self):
        for index in range(len(self.instructions)):
            instructions = self.instructions[index:index+3]
            commands = [i[0] for i in instructions]
            if commands == ['inc', 'dec', 'jnz']:
                from_ = instructions[1][1]
                to_ = instructions[0][1]
                new_instruction = ['mul', from_, to_]
                self.instructions[index] = new_instruction
            elif commands == ['dec', 'inc', 'jnz']:
                from_ = instructions[0][1]
                to_ = instructions[1][1]
                new_instruction = ['mul', from_, to_]
                self.instructions[index] = new_instruction


    def run_step(self):
        cmd, input_1, *values = self.instructions[self.index]
        incr = 1
        if cmd == 'cpy':
            val = self.registers.get(input_1, input_1)
            self.registers[values[0]] = int(val)
        elif cmd == 'inc':
            self.registers[input_1] += 1
        elif cmd == 'dec':
            self.registers[input_1] -= 1
        elif cmd == 'jnz':
            val_1 = self.registers.get(input_1, input_1)
            val_2 = self.registers.get(values[0], values[0])
            if int(val_1):
                incr = int(val_2)
        elif cmd == 'mul':
            from_ = self.registers.get(input_1, input_1)
            self.registers[values[0]] += int(from_)
            self.registers[input_1] = 0
            incr=3
        elif cmd == 'inv_mul':
            from_ = self.registers.get(values[0], values[0])
            self.registers[input_1] += int(from_)
            self.registers[values[0]] = 0
            incr = 3
        elif cmd == 'tgl':
            val = self.registers.get(input_1, input_1)
            focus = self.index + val
            try:
                self.instructions[focus] = process_toggle(
                    self.instructions[focus])
            except IndexError:
                pass

        else:
            raise
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
        'mul': 'inv_mul',
        'inv_mul': 'mul'
    }
    return mapping[cmd], input_1, *values


if __name__ == "__main__":
    submit_answers(Solution, 12, 2016)