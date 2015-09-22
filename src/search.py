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
    def search(self):
        pass

    def get_next_from_frontier(self):
        pass


class AStar:
    def search(self):
        pass

    def get_next_from_frontier(self):
        pass


class IterativeDeepeningAStar:
    def search(self):
        pass

    def get_next_from_frontier(self):
        pass


def main():

    start_board = Board.board_from_file(sys.argv[1])
    dfs = DepthFirstSearch(start_board)
    for path in dfs.search():
        print(path)


if __name__ == '__main__':
    main()
