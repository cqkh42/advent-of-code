import itertools
import math
from collections import defaultdict

import parse

PARSER = parse.compile(r'{:d}-{:d}')


def part_a(data):
    fields, _, tickets = data.split('\n\n')
    ranges = PARSER.findall(fields)
    ranges = (range(start, end+1) for start, end in ranges)
    valid = set(itertools.chain.from_iterable(ranges))

    values = parse.findall('{num:d}', tickets)
    values = (match['num'] for match in values)
    values = (v for v in values if v not in valid)
    return sum(values)

def _parse_ticket(ticket):
    my_ticket = parse.findall('{num:d}', ticket)
    my_ticket = {index: find['num'] for index, find in enumerate(my_ticket)}
    return my_ticket

def _possibles_to_actuals(possibles, actuals):
    for k, v in possibles.items():
        if len(v) == 1:
            new = v[0]
            # print(f'{v=} must belong with {k=}')
            actuals[k] = new
            for k in possibles:
                # print(f'removing {v=} from {k=}, {possibles[k]=}')
                try:
                    possibles[k].remove(new)
                except (ValueError, IndexError):
                    pass
    return possibles, actuals

def _label_ticket(data):
    fields, my_ticket, tickets = data.split('\n\n')
    fields = parse.findall(r'{:w}:_{:d}-{:d}_or_{:d}-{:d}',
                           fields.replace(' ', '_'))
    fields = {field: {*range(start, end + 1), *range(start_2, end_2 + 1)} for
              field, start, end, start_2, end_2 in fields}

    all_field_values = set(itertools.chain.from_iterable(fields.values()))
    my_ticket = _parse_ticket(my_ticket)
    tickets = [_parse_ticket(ticket) for ticket in tickets.split('\n')[1:]]
    tickets = [my_ticket, *tickets]

    tickets = [ticket for ticket in tickets if
               set(ticket.values()).issubset(all_field_values)]
    tickets = dict(enumerate(list(zip(*[i.values() for i in tickets]))))
    possibles = defaultdict(list)
    for field in fields:
        for index, values in tickets.items():
            if set(values).issubset(fields[field]):
                possibles[field].append(index)
    actuals = {}
    while len(actuals) != len(possibles):
        possibles, actuals = _possibles_to_actuals(possibles, actuals)

    return actuals

def part_b(data, **_):
    _, my_ticket, _ = data.split('\n\n')
    my_ticket = my_ticket.split('\n')[1]

    my_ticket = [int(num) for num in my_ticket.split(',')]

    indices = _label_ticket(data)
    total = []
    for i in indices:
        if i.startswith('departure'):
            total.append(my_ticket[indices[i]])
    return math.prod(total)
