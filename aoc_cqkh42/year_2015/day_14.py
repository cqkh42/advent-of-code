# TODO use parse here
import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    time = 2503

    def parse_data(self):
        reindeer = [Reindeer(*data) for data in REGEX.findall(self.data)]
        return reindeer

    def part_a(self):
        return max(deer.distance(self.time) for deer in self.parsed_data)

    def part_b(self):
        for second in range(1, self.time + 1):
            highest_score = max(deer.distance(second) for deer in self.parsed_data)
            in_the_lead = (
                deer for deer in self.parsed_data
                if deer.distance(second) == highest_score
            )
            for deer in in_the_lead:
                deer.score += 1
        return max(self.parsed_data, key=lambda deer: deer.score).score

REGEX = re.compile(r'(\w+?) .*?(\d+).*?(\d+).*?(\d+)')


class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = int(speed)
        self.duration = int(duration)
        self.rest = int(rest)
        self.score = 0

    def distance(self, time):
        sprints, final_stretch = divmod(time, self.duration + self.rest)
        sprint_distance = self.speed * self.duration * sprints

        # we either end still sprinting or resting
        final_sprint_time = min(final_stretch, self.duration)
        final_distance = final_sprint_time * self.speed
        return sprint_distance + final_distance
