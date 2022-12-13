from bidict import bidict

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    beats = bidict({'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'})
    score = {'rock': 1, 'paper': 2, 'scissors': 3}
    you_mapping = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

    def parse_data(self):
        elf_mapping = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
        plays = (line.split() for line in self.lines)
        return [(elf_mapping[elf], you) for elf, you in plays]

    def round_score(self, elf, you):
        score = self.score[you]
        if self.beats[you] == elf:
            score += 6
        elif you == elf:
            score += 3
        return score

    def part_a(self):
        return sum(
            self.round_score(elf, self.you_mapping[you])
            for elf, you in self.parsed_data
        )

    def _find_your_b_play(self, elf, you):
        if you == 'X':
            your_play = self.beats[elf]
        elif you == 'Y':
            your_play = elf
        else:
            your_play = self.beats.inverse[elf]
        return your_play

    def part_b(self):
        return sum(
            self.round_score(elf, self._find_your_b_play(elf, you))
            for elf, you in self.parsed_data
        )
