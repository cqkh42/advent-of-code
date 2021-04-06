# TODO USing A*
# TODO extract graph logic

from dataclasses import dataclass, field, replace

from aoc_cqkh42 import BaseSolution


@dataclass(frozen=True)
class State:
    x: int
    y: int
    fav_number: int
    steps: int = field(compare=False)

    def valid(self):
        if self.x < 0 or self.y < 0:
            return False
        calc = self.x**2 + 3*self.x + 2*self.x*self.y + self.y + self.y**2 + self.fav_number
        ones = bin(calc).count('1')
        return not(ones % 2)

    def is_complete(self):
        return self.x == 31 and self.y == 39

    def next_moves(self):
        for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_state = replace(self, x=self.x+x, y=self.y+y, steps=self.steps+1)
            if new_state.valid():
                yield new_state


class ShortestPath:
    def __init__(self, state, cutoff=float('inf')):
        self.states = [state]
        self.cutoff = cutoff
        self.seen = set()

    def run(self):
        while self.states:
            state = self.states.pop(0)
            if state in self.seen or state.steps > self.cutoff:
                continue
            else:
                self.seen.add(state)
            neighbours = state.next_moves()
            if state.is_complete():
                return state.steps
            for neighbour in neighbours:
                self.states.append(neighbour)


class Solution(BaseSolution):
    def part_a(self):
        state = State(1, 1, int(self.data), 0)
        a_star = ShortestPath(state)
        return a_star.run()

    def part_b(self):
        state = State(1, 1, int(self.data), 0)
        a_star = ShortestPath(state, 50)
        a_star.run()
        return len(a_star.seen)
