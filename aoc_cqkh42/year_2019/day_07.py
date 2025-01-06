import itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2019.computer import Computer


def find_best_config(possible_configs, intcode):
    results = []
    for configs in possible_configs:
        input_ = 0
        for config in configs:
            amp = Computer(intcode, [config, input_])
            amp.run()
            input_ = amp.output

        results.append((configs, input_))
    return max(results, key=lambda result: result[1])

def run_until_output(computer):
    computer.output = None
    while computer.output is None:
        computer.run_iteration()
    return computer


def find_best_config_b(possible_configs, intcode):
    results = []
    for configs in possible_configs:
        computers = [Computer(intcode, [config]) for config in configs]
        input_ = 0
        for index, computer in enumerate(itertools.cycle(computers)):
            list_index = index % len(computers)
            computer.inputs.append(input_)
            try:
                computer = run_until_output(computer)
            except StopIteration:
                results.append((configs, input_))
                break
            else:
                computers[list_index] = computer
                input_ = computer.output

    return max(results, key=lambda result: result[1])


class Solution(BaseSolution):

    def part_a(self):
        inputs = self.numbers
        configs = itertools.permutations(range(5))
        result = find_best_config(configs, inputs)[1]
        return result

    def part_b(self):
        range_ = range(5, 10)
        inputs = self.numbers
        configs = itertools.permutations(range_)
        result = find_best_config_b(configs, inputs)[1]
        return result
