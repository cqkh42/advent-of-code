# TODO chompsky language decomposition
import itertools

from aoc_cqkh42 import BaseSolution


def replace_occurence(string, old, new, occurence):
    return (
        string.replace(old, "$$$", occurence - 1)
        .replace(old, new, 1)
        .replace("$$$", old)
    )


def try_permutation(maps, element):
    visited = set()
    replaced = 0
    while element != "e":
        for new, old in maps:
            if old not in element or element.count("e"):
                continue
            element = element.replace(old, new, 1)
            if element == "e":
                return replaced + 1
            elif "e" in element:
                return None
            if element in visited:
                return None
            visited.add(element)
            replaced += 1
    return replaced


class Solution(BaseSolution):
    element = None
    maps = None

    def parse_data(self):
        *maps, _, element = self.lines
        maps = [item.split(" => ") for item in maps]
        self.element = element
        self.maps = maps
        return maps, element

    def part_a(self):
        new_strings = set()
        for old, new in self.maps:
            count = self.element.count(old)
            for occurence in range(1, count + 1):
                new_string = replace_occurence(self.element, old, new, occurence)
                new_strings.add(new_string)
        return len(new_strings)

    def part_b(self):
        possible_orders = itertools.permutations(self.maps)
        for order in possible_orders:
            result = try_permutation(order, self.element)
            if result:
                return result
