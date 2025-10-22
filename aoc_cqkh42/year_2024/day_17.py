import itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Computer:
    def __init__(self, intcode, register):
        self.pointer = 0
        self.intcode = list(intcode)
        self.register = register
        self.outputs = []

    def get_combo(self):
        operand = self.intcode[self.pointer+1]
        if operand <= 3:
            return operand
        elif operand == 4:
            return self.register['A']
        elif operand == 5:
            return self.register['B']
        elif operand == 6:
            return self.register['C']
        else:
            raise ValueError(f'getcombo not valid for {operand}')

    def dv(self):
        return self.register['A'] // (2 ** self.get_combo())


    def step(self):
        opcode = self.intcode[self.pointer]
        operand = self.intcode[self.pointer+1]

        jmp = 2
        if opcode == 0:  # adv
            self.register['A'] = self.dv()
        elif opcode == 1:  # bxl
            self.register['B'] ^= operand
        elif opcode == 2:  #bst
            self.register['B'] = self.get_combo() % 8
        elif opcode == 3 and self.register['A']: #jnz
            self.pointer = operand
            jmp = 0
        elif opcode == 4:  # bxc
            self.register['B'] ^= self.register['C']
        elif opcode == 5:  #out
            self.outputs.append(self.get_combo() % 8)
            self.pointer += jmp
            return True
        elif opcode == 6:  # bdv
            self.register['B'] = self.dv()
        elif opcode == 7:  # cdv
            self.register['C'] = self.dv()

        self.pointer += jmp

    def run(self, iters=1_000_000, early_stopping=False):
        for _ in range(iters):
            try:
                self.step()
            except IndexError:
                return self.outputs == self.intcode[:len(self.outputs)]
            if early_stopping:
                if self.outputs != self.intcode[:len(self.outputs)]:
                    return False



class Solution(BaseSolution):
    def  _parse(self):
        a, b, c, *intcode = self.numbers
        register = {"A": a, "B": b, "C": c}
        return intcode, register

    def part_a(self):
        computer = Computer(*self.parsed)
        computer.run()
        return ','.join([str(i) for i in computer.outputs])

    def part_b(self):
        target = list(self.parsed[0])
        for seed in itertools.count():

            register = {"A": seed, "B": 0, "C": 0}
            computer = Computer(target, register)
            computer.run(early_stopping=True)
            if computer.outputs == target:
                return seed


if __name__ == "__main__":
    submit_answers(Solution,17, 2024)
