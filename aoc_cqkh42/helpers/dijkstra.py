import queue


def dijkstra(start):
    frontier = queue.PriorityQueue()

    frontier.put(start)
    visited = set()

    while frontier.not_empty:
        node = frontier.get()
        if node in visited:
            continue
        if node.is_target():
            return node.used_mana
        visited.add(node)
        for neighbour in node.neighbours():
            frontier.put(neighbour)