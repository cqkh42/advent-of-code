import numpy as np
import pytest

from aoc_cqkh42.year_2021 import day_11

step_0 = np.array([
    list('5483143223'),
    list('2745854711'),
    list('5264556173'),
    list('6141336146'),
    list('6357385478'),
    list('4167524645'),
    list('2176841721'),
    list('6882881134'),
    list('4846848554'),
    list('5283751526'),
], dtype=int)

step_1 = np.array([
    list('6594254334'),
    list('3856965822'),
    list('6375667284'),
    list('7252447257'),
    list('7468496589'),
    list('5278635756'),
    list('3287952832'),
    list('7993992245'),
    list('5957959665'),
    list('6394862637'),
], dtype=int)

step_2 = np.array([
    list('8807476555'),
    list('5089087054'),
    list('8597889608'),
    list('8485769600'),
    list('8700908800'),
    list('6600088989'),
    list('6800005943'),
    list('0000007456'),
    list('9000000876'),
    list('8700006848'),
], dtype=int)

step_3 = np.array([
    list('0050900866'),
    list('8500800575'),
    list('9900000039'),
    list('9700000041'),
    list('9935080063'),
    list('7712300000'),
    list('7911250009'),
    list('2211130000'),
    list('0421125000'),
    list('0021119000'),
], dtype=int)

step_4 = np.array([
    list('2263031977'),
    list('0923031697'),
    list('0032221150'),
    list('0041111163'),
    list('0076191174'),
    list('0053411122'),
    list('0042361120'),
    list('5532241122'),
    list('1532247211'),
    list('1132230211'),
], dtype=int)

step_5 = np.array([
    list('4484144000'),
    list('2044144000'),
    list('2253333493'),
    list('1152333274'),
    list('1187303285'),
    list('1164633233'),
    list('1153472231'),
    list('6643352233'),
    list('2643358322'),
    list('2243341322'),
], dtype=int)

step_6 = np.array([
    list('5595255111'),
    list('3155255222'),
    list('3364444605'),
    list('2263444496'),
    list('2298414396'),
    list('2275744344'),
    list('2264583342'),
    list('7754463344'),
    list('3754469433'),
    list('3354452433'),
], dtype=int)

step_7 = np.array([
    list('6707366222'),
    list('4377366333'),
    list('4475555827'),
    list('3496655709'),
    list('3500625609'),
    list('3509955566'),
    list('3486694453'),
    list('8865585555'),
    list('4865580644'),
    list('4465574644'),
], dtype=int)

step_8 = np.array([
    list('7818477333'),
    list('5488477444'),
    list('5697666949'),
    list('4608766830'),
    list('4734946730'),
    list('4740097688'),
    list('6900007564'),
    list('0000009666'),
    list('8000004755'),
    list('6800007755'),
], dtype=int)

step_9 = np.array([
    list('9060000644'),
    list('7800000976'),
    list('6900000080'),
    list('5840000082'),
    list('5858000093'),
    list('6962400000'),
    list('8021250009'),
    list('2221130009'),
    list('9111128097'),
    list('7911119976'),
], dtype=int)

step_10 = np.array([
    list('0481112976'),
    list('0031112009'),
    list('0041112504'),
    list('0081111406'),
    list('0099111306'),
    list('0093511233'),
    list('0442361130'),
    list('5532252350'),
    list('0532250600'),
    list('0032240000'),
], dtype=int)


@pytest.fixture
def solution():
    data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    return day_11.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 1656


def test_part_b(solution):
    assert solution.part_b() == 195


@pytest.mark.parametrize('start,end', [
    (step_0, step_1),
    (step_1, step_2),
    (step_2, step_3),
    (step_3, step_4),
    (step_4, step_5),
    (step_5, step_6),
    (step_6, step_7),
    (step_7, step_8),
    (step_8, step_9),
    (step_9, step_10),
])
def test_step(start, end):
    np.testing.assert_equal(day_11.step(start), end)