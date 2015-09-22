import sys
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
    def search(self):
        pass

class IterativeDeepeningAStar:
    def search(self):
        pass

def main():

    start_board = Board.board_from_file(sys.argv[1])

    bfs = BreadthFirstSearch(start_board)
    for board in bfs.search():
        print(board)


if __name__ == '__main__':
    main()
