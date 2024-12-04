import pytest

import aoc_cqkh42.year_2024.day_04


@pytest.fixture
def solution():
    return aoc_cqkh42.year_2024.day_04.Solution(
        """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""")

def test_part_a(solution):
    assert solution.part_a() == 18