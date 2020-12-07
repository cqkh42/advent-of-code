def _fuel_needed(module):
    return max(int(module) // 3 - 2, 0)


def _total_fuel_needed(module):
    fuel = _fuel_needed(module)
    if not fuel:
        return fuel
    return fuel + _total_fuel_needed(fuel)


def part_a(data):
    return sum(_fuel_needed(module) for module in data.split('\n'))


def part_b(data, **_):
    return sum(_total_fuel_needed(module) for module in data.split('\n'))
