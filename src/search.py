from abc import ABCMeta, abstractmethod
import sys
from src.board import Board


class Search:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.frontier = []

    def add_to_frontier(self, board):
        self.add_to_frontier(board)

    def in_frontier(self, board):
        return board in self.frontier


class DepthFirstSearch(Search):

    def search(self, state, path):

        if state.is_goal():
            print(path)
            return path

        for move, board in state.successors():
            self.search(board, path + [move])

class BreadthFirstSearch(Search):
    def search(self):
        pass

    def get_next_from_frontier(self):
        pass


class AStar(Search):
    def search(self):
        pass

    def get_next_from_frontier(self):
        pass


class IterativeDeepeningAStar(Search):
    def search(self):
        pass

    def get_next_from_frontier(self):
        pass


def main():

    start_board = Board.board_from_file(sys.argv[1])
    dfs = DepthFirstSearch()
    dfs.search(start_board, [])


if __name__ == '__main__':
    main()
