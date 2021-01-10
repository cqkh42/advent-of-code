from collections import defaultdict
import itertools

import parse

def part_a(data):
    instructions = data.split('\n')

    bots = defaultdict(set)
    bot_instructions = {}

    for instruction in instructions:
        if instruction.startswith('value'):
            new_value, new_bot = parse.search('value {:d} goes to bot {:d}', instruction)
            bots[new_bot].add(new_value)
        elif instruction.startswith('bot'):
            p = parse.parse('bot {:d} gives low to {:w} {:d} and high to {:w} {:d}', instruction)
            bot, low_out, low, high_out, high = p
            bot_instructions[bot] = {
                'high': [high_out, high],
                'low': [low_out, low]
            }

    outputs = {}
    for bot, instruction in itertools.cycle(bot_instructions.items()):
        holding = bots[bot]
        if holding == {17, 61}:
            break
        if len(holding) == 2:
            for level, num in zip(['low', 'high'], sorted(holding)):
                where, who = instruction[level]
                if where == 'bot':
                    bots[who].add(num)
                else:
                    outputs[who] = num
            bots[bot] = set()

    return bot


def part_b(data, **_):
    instructions = data.split('\n')

    bots = defaultdict(list)
    outputs = {}

    setting = [instruction for instruction in instructions if
               instruction.startswith('value')]
    for instruction in setting:
        _, value, *__, bot = instruction.split(' ')
        bots[int(bot)].append(int(value))

    bot_instructions = [instruction.split() for instruction in instructions if
                        instruction.startswith('bot')]
    bot_instructions = {
        int(instruction[1]): {
            'high': [instruction[-2], int(instruction[-1])],
            'low': [instruction[5], int(instruction[6])]
        } for instruction in bot_instructions
    }

    for bot, instruction in itertools.cycle(bot_instructions.items()):
        holding = bots[bot]
        if 0 in outputs and 1 in outputs and 2 in outputs:
            break
        if len(holding) == 2:
            for level, num in zip(['low', 'high'], sorted(holding)):
                where, who = instruction[level]
                if where == 'bot':
                    bots[who].append(num)
                else:
                    outputs[who] = num
            bots[bot] = []

    return outputs[0] * outputs[1] * outputs[2]
