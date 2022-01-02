import collections
from abc import ABC, abstractmethod


class BFS:
    def __init__(self, start):
        self.frontier = collections.deque()
        self.visited = set()
        self.frontier.append(start)

    def run(self):
        while self.frontier:
            node = self.frontier.popleft()
            if node in self.visited:
                continue
            if node.is_target():
                return node.distance
            self.visited.add(node)
            for neighbour in node.neighbours():
                self.frontier.append(neighbour)



class BFSBaseState(ABC):
    distance: int = NotImplemented

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
