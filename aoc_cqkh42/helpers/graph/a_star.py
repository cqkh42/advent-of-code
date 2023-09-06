import queue
from abc import ABC, abstractmethod


class AStarBaseNode(ABC):
    distance = NotImplemented

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError

    @abstractmethod
    def neighbours(self):
        raise NotImplementedError

    @abstractmethod
    def is_valid(self):
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        # PriorityQueue returns the lowest value item first
        return self.distance + self.h >= (other.distance + other.h)


class AStar:
    def __init__(self, start, target):
        # f(n) = g(n) + h(n)
        # where g(n) is current distance and h(n) is the heuristic
        self.frontier = queue.PriorityQueue()
        self.visited = set()
        self.frontier.put(start)
        self.target = target

    def run(self):
        while not self.frontier.empty():
            state = self.frontier.get()
            # print(state.distance + state.h)
            if state == self.target:
                return state.distance
            if state in self.visited:
                continue
            self.visited.add(state)
            new_states = [i for i in state.neighbours() if i not in self.visited]
            for new_state in new_states:
                self.frontier.put(new_state)
