import re

def part_a(data):
    triangles = data.split('\n')
    triangles = [re.split(r'\s+', triangle.strip()) for triangle in triangles]
    triangles = [[int(num) for num in triangle] for triangle in triangles]

    valid = [triangle for triangle in triangles if
             triangle[0] + triangle[1] > triangle[2]]
    valid = [triangle for triangle in valid if
             triangle[0] + triangle[2] > triangle[1]]
    valid = [triangle for triangle in valid if
             triangle[1] + triangle[2] > triangle[0]]

    return len(valid)


def part_b(data, **_):
    triangles = data.split('\n')
    triangles = [re.split(r'\s+', triangle.strip()) for triangle in triangles]
    triangles = [[int(num) for num in triangle] for triangle in triangles]

    triangles = [
        *[triangle[0] for triangle in triangles],
        *[triangle[1] for triangle in triangles],
        *[triangle[2] for triangle in triangles]
    ]

    triangles = [(triangles[index:index + 3]) for index in
                 range(0, len(triangles), 3)]

    valid = [triangle for triangle in triangles if
             triangle[0] + triangle[1] > triangle[2]]
    valid = [triangle for triangle in valid if
             triangle[0] + triangle[2] > triangle[1]]
    valid = [triangle for triangle in valid if
             triangle[1] + triangle[2] > triangle[0]]

    return len(valid)