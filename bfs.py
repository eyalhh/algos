# imports
from collections import deque
from enum import Enum
from generic_algo import GenericAlgo
from typing import Optional

# color class
class BFSColor(Enum):
    WHITE = 0,
    GREY= 1,
    BLACK = 2

# bfs class
class BfsAlgo(GenericAlgo):

    # NOTE: this implementation uses an adjacency matrix , which is not as efficient as adjacency list
    def __init__(self, graph: list[list[int]], starting_node: int):
        self.graph = graph
        self.length = len(graph)
        assert starting_node >= 0 and starting_node < self.length, 'index of starting node must be within bounds'
        self.start = starting_node

    def run(self) -> tuple[list[float], list[int | None]]:

        bfs_queue = deque()
        d = [float('inf')] * self.length
        pi: list[int | None] = [None] * self.length # type checker was giving some problems 
        color = [BFSColor.WHITE] * self.length

        d[self.start] = 0
        color[self.start] = BFSColor.GREY
        bfs_queue.append(self.start)

        while bfs_queue:
            u = bfs_queue.popleft()
            for vertex, is_neighbor in enumerate(self.graph[u]):
                if is_neighbor:
                    if color[vertex] == BFSColor.WHITE:
                        color[vertex] = BFSColor.GREY
                        d[vertex] = d[u] + 1
                        pi[vertex] = u
                        bfs_queue.append(vertex)
            
        return (d, pi)
    
    def test(self):
        pass


bfs = BfsAlgo([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
print(bfs.run())
