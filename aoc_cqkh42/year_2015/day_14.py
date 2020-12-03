import re

REGEX = re.compile(r'(\w+?) .*?(\d+).*?(\d+).*?(\d+)')


class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = int(speed)
        self.duration = int(duration)
        self.rest = int(rest)
        self.score = 0

    def distance(self, time):
        distance_per_sprint = self.speed * self.duration
        num_sprints = time // (self.duration + self.rest)
        sprint_distance = distance_per_sprint * num_sprints

        the_end = time % (self.duration + self.rest)
        # we either end still sprinting or resting
        final_sprint_time = min(the_end, self.duration)
        final_distance = final_sprint_time * self.speed
        return sprint_distance + final_distance


def part_a(data, time=2503):
    reindeer = data
    reindeer = reindeer.split('\n')
    reindeer = (REGEX.search(deer).groups() for deer in reindeer)
    reindeer = (Reindeer(*data) for data in reindeer)
    return max(deer.distance(time) for deer in reindeer)


def part_b(data, time=2503, **_):
    reindeer = data
    reindeer = reindeer.split('\n')
    reindeer = (REGEX.search(deer).groups() for deer in reindeer)
    reindeer = [Reindeer(*data) for data in reindeer]

    for second in range(1, time+1):
        highest_score = max(deer.distance(second) for deer in reindeer)
        in_the_lead = (
            deer for deer in reindeer
            if deer.distance(second) == highest_score
        )
        for deer in in_the_lead:
            deer.score += 1
    return max(reindeer, key=lambda deer: deer.score).score
