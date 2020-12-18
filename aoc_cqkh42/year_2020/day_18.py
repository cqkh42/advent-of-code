import operator

def solve_in_sequence(equation):
    equation = equation.split(' ')
    total = int(equation[0])
    funcs = {
        '+': operator.add,
        '*': operator.mul
    }
    func = funcs[equation[1]]
    for step in equation[1:]:
        if step in funcs:
            func = funcs[step]
        else:
            total = func(total, int(step))
    return total


def fix_bracket(string, order=solve_in_sequence):
    start = len(string) - string[-1::-1].index('(') - 1
    counted = 0
    for index, char in enumerate(string[start:], start):
        if char == '(':
            counted -= 1
        elif char == ')':
            counted += 1
        if not counted:
            break
    equation = string[start+1:index]
    answer = order(equation)
    new_string = string[:start] + str(answer) + string[index+1:]
    return new_string.replace('  ', ' ')



def solve_in_precedence(equation):
    equation = equation.split(' ')
    while '+' in equation:
        plus = equation.index('+')
        answer = int(equation[plus-1]) + int(equation[plus+1])
        equation = [*equation[:plus-1], answer, *equation[plus+2:]]
    if len(equation) == 1:
        return equation[0]
    return solve_in_sequence(' '.join(str(i) for i in equation))


def do(data, order=solve_in_sequence):
    data = '(' + data + ')'
    while '(' in data:
        data = fix_bracket(data, order)
    return int(data)


def part_a(data):
    equations = data.split('\n')
    answers = (do(equation, solve_in_sequence) for equation in equations)
    return sum(answers)


def part_b(data, **_):
    equations = data.split('\n')
    answers = (do(equation, solve_in_precedence) for equation in equations)
    return sum(answers)
