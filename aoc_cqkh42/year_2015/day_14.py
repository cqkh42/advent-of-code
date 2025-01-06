from dataclasses import dataclass

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

PARSER = parse.compile(
    r"{name:w} can fly {speed:d} km/s for {duration:d} seconds, but then must "
    r"rest for {rest:d} seconds."
)


class Reindeer:
    def __init__(self, line):
        as_dict = PARSER.search(line).named
        self.name = as_dict['name']
        self.speed = as_dict['speed']
        self.duration = as_dict['duration']
        self.rest = as_dict['rest']
        self.score = 0

    def distance(self, time):
        sprints, final_stretch = divmod(time, self.duration + self.rest)
        sprint_distance = self.speed * self.duration * sprints

        # we either end still sprinting or resting
        final_sprint_time = min(final_stretch, self.duration)
        final_distance = final_sprint_time * self.speed
        return sprint_distance + final_distance


class Solution(BaseSolution):
    def part_a(self, time=2503):
        return max(deer.distance(time) for deer in self.lines_as(Reindeer))

    def part_b(self, time=2503):
        reindeers = self.lines_as(Reindeer)
        for second in range(1, time + 1):
            highest_score = max(deer.distance(second) for deer in reindeers)
            for deer in reindeers:
                deer.score += deer.distance(second) == highest_score
        return max(reindeers, key=lambda deer: deer.score).score


if __name__ == "__main__":
    submit_answers(Solution, 14, 2015)
