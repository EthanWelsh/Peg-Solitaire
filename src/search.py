from abc import ABCMeta, abstractmethod


class Search:
    __metaclass__ = ABCMeta

    def __init__(self, init_state):
        self.state = init_state
        self.frontier = []

    def add_to_frontier(self, board):
        self.add_to_frontier(board)

    def in_frontier(self, board):
        return board in self.frontier

    @abstractmethod
    def get_next_from_frontier(self):
        pass


class BreadthFirstSearch:
    pass


class DepthFirstSearch:
    pass


class AStar:
    pass


class IterativeDeepeningAStar:
    pass
