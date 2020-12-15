import re

REGEX = re.compile(r'mem\[(\d+)] = (\d+)')


def _replace_floater(address):
    if address.count('X') == 1:
        return {address.replace('X', '0'), address.replace('X', '1')}
    else:
        return {
            *_replace_floater(address.replace('X', '0', 1)),
            *_replace_floater(address.replace('X', '1', 1))
        }


def _mask_value(value, mask):
    value = f'{int(value):b}'.zfill(36)
    value = ''.join(v if m == 'X' else m for v, m in zip(value, mask))
    value = int(value, 2)
    return value


def _mask_address(address, mask):
    address = f'{int(address):b}'.zfill(36)
    address = ''.join(m if m != '0' else a for a, m in zip(address, mask))
    addresses = _replace_floater(address)
    return {int(address, 2) for address in addresses}


def part_a(data):
    memory = {}
    mask = None
    for row in data.split('\n'):
        if row.startswith('mask'):
            mask = row.split(' = ')[1]
        else:
            target, value = REGEX.match(row).groups()
            value = _mask_value(value, mask)
            memory[target] = value
    return sum(memory.values())


def part_b(data, **_):
    memory = {}
    mask = None
    for row in data.split('\n'):
        if row.startswith('mask'):
            mask = row.split(' = ')[1]
        else:
            target, value = REGEX.match(row).groups()
            addresses = _mask_address(target, mask)
            for address in addresses:
                memory[address] = int(value)
    return sum(memory.values())
