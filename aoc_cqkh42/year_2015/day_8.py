import re


def _decode_str(string):
    string = re.sub(r'^"', '', string)
    string = re.sub(r'"$', '', string)
    string = re.sub(r'\\\\', r'\\', string)
    string = re.sub(r'\\"', '"', string)
    string = re.sub(r'\\x[a-f0-9]{2}', 'x', string)
    return string


def part_a(data):
    code_len = len(data) - data.count('\n')
    str_len = len(''.join(_decode_str(line) for line in data.split('\n')))
    return code_len - str_len


def part_b(data, **_):
    return sum(line.count('"') + line.count('\\') + 2 for line in data.split('\n'))
