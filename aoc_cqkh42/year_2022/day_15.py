from aoc_cqkh42 import BaseSolution

# 6228183 is too high

import parse


def manhattan(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])


def resolve_manhattan(u, distance, known_y):
    partial_diff = abs(u[1] - known_y)
    needed = distance - partial_diff
    if needed < 0:
        raise ValueError
    return sorted((u[0] - needed, u[0] + needed))


class Solution(BaseSolution):
    parser = parse.compile(
        'Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}'
    )
    beacons = set()

    def parse_data(self):
        sensors = {}
        for sensor_x, sensor_y, beacon_x, beacon_y in self.parser.findall(self.data):
            sensors[(sensor_x, sensor_y)] = manhattan((sensor_x, sensor_y), (beacon_x, beacon_y))
            self.beacons.add((beacon_x, beacon_y))
        # print(sensors)
        return sensors

    def part_a(self, y=2_000_000):
        unavailable = set()
        for sensor, distance in self.parsed_data.items():
            try:
                start, end = resolve_manhattan(sensor, distance, y)
                # print(sensor, start, end, distance)
            except ValueError:
                # print('raised')
                continue
            else:
                for num in range(start, end+1):
                    unavailable.add(num)
        for beacon in self.beacons:
            if beacon[1] == y:
                unavailable.remove(beacon[0])
        for sensor in self.parsed_data:
            if sensor[1] == y:
                unavailable.remove(sensor[0])
                # print()
        # print(sorted(unavailable))
        return len(unavailable)

    def part_b(self, limit=4_000_000):
        ...
