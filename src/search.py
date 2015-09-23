from queue import PriorityQueue
import sys
import heapq
import itertools

from src.board import Board


class DepthFirstSearch:

    def __init__(self, start):
        self.start = start

    def search(self, state=None, path=None):
        if not state and not path:
            state = self.start
            path = []

        if state.is_goal():
            yield path

        for move, board in state.successors():
            yield from self.search(board, path + [move])


class BreadthFirstSearch:
    def __init__(self, start):
        self.start = start

    def search(self):
        queue = [(self.start, [])]

        while queue:
            (state, path) = queue.pop(0)
            for move, board in state.successors():
                if board.is_goal():
                    yield path + [move]
                else:
                    queue.append((board, path + [move]))


class AStar:

    def __init__(self, start):
        self.start = start

    def search(self):
        pq = PriorityQueue()
        pq.put((self.start, []))
        while not pq.empty():
            state, path = pq.get()

            if state.is_goal():
                yield path
            for move, board in state.successors():
                pq.put((board, path + [move]))


class IterativeDeepeningAStar:

    def __init__(self, start):
        self.start = start

    def search(self):

        def depth_limited_astar(depth, state, path):
            if len(path) + state.heuristic(state) > depth:
                return

            if state.is_goal():
                return path

            for move, board in state.successors():
                z = depth_limited_astar(depth, board, path + [move])
                if z is not None:
                    return z

        for depth in itertools.count():
            x = depth_limited_astar(depth, self.start, [])
            if x is not None:
                return x


def main():

    start_board = Board.board_from_file(sys.argv[1])
    method = sys.argv[2]

    if method == 'dfs':
        dfs = DepthFirstSearch(start_board)
        print(next(dfs.search()))
    elif method == 'bfs':
        bfs = BreadthFirstSearch(start_board)
        print(next(bfs.search()))
    elif method == 'astar':
        x = lambda x: 1
        start_board.heuristic = x
        astar = AStar(start_board)
        print(next(astar.search()))
    elif method == 'itdastar':
        x = lambda x: 1
        start_board.heuristic = x
        itd_astar = IterativeDeepeningAStar(start_board)
        print(itd_astar.search())
    else:
        print("You must choose a valid method")

if __name__ == '__main__':
    main()
