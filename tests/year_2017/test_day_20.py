import pytest

from aoc_cqkh42.year_2017.day_20 import Solution, Particle

import numpy as np

@pytest.fixture
def data_a():
    return """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""

@pytest.fixture
def data_b():
    return """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>    
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""

@pytest.fixture()
def p_0():
    return Particle(np.array([3,0,0]), np.array([2,0,0]), np.array([-1,0,0]))

@pytest.fixture()
def p_1():
    return Particle(np.array([4, 0, 0]), np.array([0, 0, 0]), np.array([-2, 0, 0]))

@pytest.mark.parametrize('step,velocity', [
    (1, 1),
    (2, 0),
    (3, -1),
])
def test_velocity_at_p_0(p_0, step,velocity):
    np.testing.assert_array_equal(p_0.velocity_at(step), [velocity, 0,0])

@pytest.mark.parametrize('step,velocity', [
    (1, -2),
    (2, -4),
    (3, -6)
])
def test_velocity_at_p_1(p_1, step,velocity):
    np.testing.assert_array_equal(p_1.velocity_at(step), [velocity, 0,0])


@pytest.mark.parametrize('step,position', [
    (1, 4),
    (2, 4),
    (3, 3),
])
def test_position_at_p_0(p_0, step,position):
    np.testing.assert_array_equal(p_0.position_at(step), [position, 0,0])

@pytest.mark.parametrize('step,position', [
    (1, 2),
    (2, -2),
    (3, -8)
])
def test_position_at_p_1(p_1, step,position):
    np.testing.assert_array_equal(p_1.position_at(step), [position, 0,0])


@pytest.mark.parametrize('step,distance', [
    (1, 4),
    (2, 4),
    (3, 3),
])
def test_distance_at_p_0(p_0, step,distance):
    assert p_0.distance_at(step) == distance

@pytest.mark.parametrize('step,distance', [
    (1, 2),
    (2, 2),
    (3, 8)
])
def test_distance_at_p_1(p_1, step,distance):
    assert p_1.distance_at(step) == distance

def test_part_a(data_a):
    assert Solution(data_a).part_a() == 0


def test_part_b(data_b):
    assert Solution(data_b).part_b() == 1