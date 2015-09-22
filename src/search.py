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
            return path

        for move, board in state.successors():
            child_path = self.search(board, path + [move])
            if child_path is not None:
                return child_path

        return None


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
    print(dfs.search())


if __name__ == '__main__':
    main()
