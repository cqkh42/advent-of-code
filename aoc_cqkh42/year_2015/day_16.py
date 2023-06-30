import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution

PARSER = parse.compile("{:w}: {:d}, {:w}: {:d}, {:w}: {:d}")


# noinspection SpellCheckingInspection
AUNTIE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


# noinspection SpellCheckingInspection
def _good_sue(sue):
    equals = ["children", "samoyeds", "akitas", "vizslas", "cars", "perfumes"]
    equals = all(sue.get(key, AUNTIE[key]) == AUNTIE[key] for key in equals)

    gt = ["cats", "trees"]
    gt = all(sue.get(key, float("inf")) > AUNTIE[key] for key in gt)

    lt = ["pomeranians", "goldfish"]
    lt = all(sue.get(key, -1) < AUNTIE[key] for key in lt)
    return equals and gt and lt


class Solution(BaseSolution):
    def _process_data(self):
        sue_list = PARSER.findall(self.input_)
        sues = [zip(sue[::2], sue[1::2]) for sue in sue_list]
        return [dict(sue) for sue in sues]

    def part_a(self):
        sue_is_good = [sue.items() <= AUNTIE.items() for sue in self.processed]
        return sue_is_good.index(True) + 1

    def part_b(self):
        is_good_sue = [_good_sue(sue) for sue in self.processed]
        return is_good_sue.index(True) + 1
