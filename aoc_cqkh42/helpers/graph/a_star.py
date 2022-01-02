from abc import ABC, abstractmethod
import itertools
import queue


class AStarBaseState(ABC):
    @abstractmethod
    def h(self):
        return NotImplementedError

    @abstractmethod
    def is_target(self):
        return NotImplementedError

    @abstractmethod
    def __hash__(self):
        return NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        return NotImplementedError

    @abstractmethod
    def neighbours(self):
        return NotImplementedError

    @abstractmethod
    def is_valid(self):
        return NotImplementedError

    def __gt__(self, other):
        # PriorityQueue returns the lowest value item first
        return self.distance + self.h() >= (other.distance + other.h())


class AStar:
    def __init__(self, start):
        # f(n) = g(n) + h(n)
        # where g(n) is current distance and h(n) is the heuristic
        self.frontier = queue.PriorityQueue()
        self.visited = set()
        self.frontier.put(start)

    def run(self):
        while not self.frontier.empty():
            state = self.frontier.get()
            if state.is_target():
                return state.distance
            if state in self.visited:
                continue
            self.visited.add(state)
            new_states = state.neighbours()
            for new_state in new_states:
                self.frontier.put(new_state)
