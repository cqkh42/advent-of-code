from dataclasses import dataclass

import parse

from aoc_cqkh42 import BaseSolution


TIME = 2503
PARSER = parse.compile(
    r'{name:w} can fly {speed:d} km/s for {duration:d} seconds, but then must '
    r'rest for {rest:d} seconds.'
)


@dataclass
class Reindeer:
    name: str
    speed: int
    duration: int
    rest: int
    score = 0

    def distance(self, time):
        sprints, final_stretch = divmod(time, self.duration + self.rest)
        sprint_distance = self.speed * self.duration * sprints

        # we either end still sprinting or resting
        final_sprint_time = min(final_stretch, self.duration)
        final_distance = final_sprint_time * self.speed
        return sprint_distance + final_distance


class Solution(BaseSolution):
    def parse_data(self):
        reindeer = [
            Reindeer(**data.named) for data in PARSER.findall(self.data)
        ]
        return reindeer

    def part_a(self, time=TIME):
        return max(deer.distance(time) for deer in self.parsed_data)

    def part_b(self, time=TIME):
        for second in range(1, time + 1):
            highest_score = max(
                deer.distance(second) for deer in self.parsed_data
            )
            for deer in self.parsed_data:
                deer.score += deer.distance(second) == highest_score
        return max(self.parsed_data, key=lambda deer: deer.score).score




