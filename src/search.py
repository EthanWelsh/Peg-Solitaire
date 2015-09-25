import sys

import itertools
import math

from src.board import Board
from src.priority_queue import PriorityQueue
import src.heuristic as heuristics


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
    def __init__(self, start, heuristic):
        self.start = start
        self.heuristic = heuristic

    def search(self):
        pq = PriorityQueue(self.heuristic)
        pq.put((self.start, []))
        while not pq.empty():
            state, path = pq.get()

            if state.is_goal():
                yield path
            for move, board in state.successors():
                pq.put((board, path + [move]))


class IterativeDeepeningAStar:
    def __init__(self, start, heuristic):
        self.start = start
        self.heuristic = heuristic

    def search(self):

        def depth_limited_astar(depth, state, path, heuristic):
            score = len(path) + heuristic(state)
            if score > depth:
                return None, score
            if state.is_goal():
                return path, score

            min = float('inf')
            for move, board in state.successors():
                z, s = depth_limited_astar(depth, board, path + [move], heuristic)
                if s < min:
                    min = s
                if z is not None:
                    return z, s
            return None, min

        x = None
        depth = 0
        while x is None:
            x, depth = depth_limited_astar(depth, self.start, [], self.heuristic)
            if x is not None:
                return x


def main():
    start_board = Board.board_from_file(sys.argv[1])
    method = sys.argv[2]
    heuristic = sys.argv[3]

    if heuristic == 'max_moves':
        heuristic = heuristics.max_moves
    elif heuristic == 'min_moves':
        heuristic = heuristics.min_moves
    elif heuristic == 'max_movable_pegs':
        heuristic = heuristics.max_movable_pegs

    if method == 'dfs':
        dfs = DepthFirstSearch(start_board)
        print(next(dfs.search()))
    elif method == 'bfs':
        bfs = BreadthFirstSearch(start_board)
        print(next(bfs.search()))
    elif method == 'astar':
        astar = AStar(start_board, heuristic)
        print(next(astar.search()))
    elif method == 'itdastar':
        itd_astar = IterativeDeepeningAStar(start_board, heuristic)
        print(itd_astar.search())
    else:
        print("You must choose a valid method")


if __name__ == '__main__':
    main()
