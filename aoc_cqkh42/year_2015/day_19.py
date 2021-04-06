# TODO tidy up
import itertools

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        *maps, _, element = self.data.split('\n')
        maps = [item.split(' => ') for item in maps]

        new_strings = set()
        for old, new in maps:
            count = element.count(old)
            for occurence in range(1, count + 1):
                new_string = element.replace(old, '$$$',
                                             occurence - 1).replace(old, new,
                                                                    1).replace(
                    '$$$', old)
                new_strings.add(new_string)
        return len(new_strings)

    def part_b(self):
        maps = self.data
        *maps, _, element = maps.split('\n')
        maps = [item.split(' => ') for item in maps]
        possible_orders = itertools.permutations(maps)
        for order in possible_orders:
            # result = None
            result = try_permutation(order, element)
            # raise ValueError
            if result:
                return result


def replace_occurence(string, old, new, occurence):
    return string.replace(old, '$$$', occurence - 1).replace(old, new, 1).replace('$$$', old)


def try_permutation(maps, element):
    visited = set()
    replaced = 0
    while element != 'e':
        for new, old in maps:
            if old not in element or element.count('e'):
                continue
            c = element.count(old)
            element = element.replace(old, new, 1)
            if element == 'e':
                return replaced + 1
            elif 'e' in element:
                return None
            if element in visited:
                return None
            visited.add(element)
            replaced += 1
    return replaced

