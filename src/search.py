import sys

from src.board import Board
from src.priority_queue import PriorityQueue
import src.heuristic as heuristics


class DepthFirstSearch:
    def __init__(self, start):
        self.start = start
        self.nodes_visited = 0

    def search(self, state=None, path=None):
        self.nodes_visited += 1

        if not state and not path:
            state = self.start
            path = []

        if state.is_goal():
            yield path

        for move, board in state.successors():
            yield from self.search(board, path + [move])


class BreadthFirstSearch:
    def __init__(self, start, check_duplicates):
        self.start = start
        self.check_duplicates = check_duplicates
        self.visited = []
        self.nodes_visited = 0

    def search(self):
        queue = [(self.start, [])]

        while queue:
            (state, path) = queue.pop(0)
            self.nodes_visited += 1

            for move, board in state.successors():
                if self.check_duplicates and board in self.visited:
                    continue
                elif self.check_duplicates:
                    self.visited = self.visited + [board]

                if board.is_goal():
                    yield path + [move]
                else:
                    queue.append((board, path + [move]))


class AStar:
    def __init__(self, start, heuristic, check_duplicates):
        self.start = start
        self.heuristic = heuristic
        self.check_duplicates = check_duplicates
        self.visited = []
        self.nodes_visited = 0

    def search(self):
        pq = PriorityQueue(self.heuristic)
        pq.put((self.start, []))
        while not pq.empty():
            state, path = pq.get()
            self.nodes_visited += 1

            if state.is_goal():
                yield path
            for move, board in state.successors():
                if self.check_duplicates and board in self.visited:
                    continue
                elif self.check_duplicates:
                    self.visited = self.visited + [board]

                pq.put((board, path + [move]))


class IterativeDeepeningAStar:
    def __init__(self, start, heuristic):
        self.start = start
        self.heuristic = heuristic
        self.nodes_visited = 0

    def search(self):

        def depth_limited_astar(depth, state, path, heuristic):
            self.nodes_visited += 1

            score = len(path) + heuristic(state)
            if score > depth:
                return None, score
            if state.is_goal():
                return path, score

            min = float('inf')
            for move, board in state.successors():
                search_path, score = depth_limited_astar(depth, board, path + [move], heuristic)
                if score < min:
                    min = score
                if search_path is not None:
                    return search_path, score
            return None, min

        x = None
        depth = 0
        while x is None:
            x, depth = depth_limited_astar(depth, self.start, [], self.heuristic)
            if x is not None:
                return x
            elif depth == float('inf'):
                return None


def main():
    start_board = Board.board_from_file(sys.argv[1])
    tree_or_graph = sys.argv[2]
    method = sys.argv[3]

    check_duplicates = 'graph' in tree_or_graph

    if 'star' in method:
        heuristic = sys.argv[4]

        if heuristic == 'max_moves':
            heuristic = heuristics.max_moves
        elif heuristic == 'min_moves':
            heuristic = heuristics.min_moves
        elif heuristic == 'max_movable_pegs':
            heuristic = heuristics.max_movable_pegs
        else:
            print("You did not pick a viable heuristic. Exiting...")
            return

    if method == 'dfs':
        seeker = DepthFirstSearch(start_board)
        try:
            print(next(seeker.search()))
        except StopIteration:
            print(None)

    elif method == 'bfs':
        seeker = BreadthFirstSearch(start_board, check_duplicates)
        try:
            print(next(seeker.search()))
        except StopIteration:
            print(None)

    elif method == 'astar':
        seeker = AStar(start_board, heuristic, check_duplicates)
        try:
            print(next(seeker.search()))
        except StopIteration:
            print(None)

    elif method == 'idastar':
        seeker = IterativeDeepeningAStar(start_board, heuristic)
        print(seeker.search())
    else:
        print("You must choose a valid search method. Exiting...")
        return

    print("Nodes Visited:", seeker)


if __name__ == '__main__':
    main()
