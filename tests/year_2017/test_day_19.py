import pytest

from aoc_cqkh42.year_2017.day_19 import Solution

@pytest.fixture
def data():
    return ("""     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """)

def test_part_a(data):
    assert Solution(data).part_a() == 'ABCDEF'


def test_part_b():
    assert Solution('123').part_b() == 3