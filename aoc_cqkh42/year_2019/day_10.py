import math


def _find_asteroids(data):
    asteroids = set()
    for y_index, row in enumerate(data.split('\n')):
        for x_index, item in enumerate(row):
            if item == '#':
                asteroids.add((x_index, y_index))
    return asteroids


def _angle(origin, other):
    if other == origin:
        return - 180
    x = other[0] - origin[0]
    y = other[1] - origin[1]
    angle = math.atan2(x, y) * 180 / math.pi
    return - angle + 180


def _asteroids_in_sight(origin, asteroids):
    in_sight = {}
    for asteroid in asteroids:
        angle = _angle(origin, asteroid)
        if angle not in in_sight:
            in_sight[angle] = asteroid
        else:
            in_sight[angle] = min(in_sight[angle], asteroid, key= lambda asteroid: (asteroid[0] - origin[0]) ** 2 + (asteroid[1] - origin[1]) ** 2)
    in_sight = set(in_sight.values())
    in_sight.remove(origin)
    return in_sight


def part_a(data):
    asteroids = _find_asteroids(data)
    in_sight = (_asteroids_in_sight(origin, asteroids) for origin in asteroids)
    counts = (len(asteroids) for asteroids in in_sight)
    return max(counts)


def part_b(data, **_):
    asteroids = _find_asteroids(data)
    in_sight = {
        origin: _asteroids_in_sight(origin, asteroids) for origin in asteroids
    }
    centre = max(in_sight, key=lambda key: len(in_sight[key]))
    in_sight = in_sight[centre]
    to_destroy = 200
    if len(in_sight) <= to_destroy:
        to_destroy -= len(in_sight)
        asteroids = asteroids.difference(in_sight)
        in_sight = _asteroids_in_sight(centre, asteroids)
    else:
        in_sight = sorted(in_sight, key=lambda x: _angle(centre, x))
        return (in_sight[to_destroy-1][0] * 100) + in_sight[to_destroy-1][1]
    return False
