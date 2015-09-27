import heapq


class PriorityQueue:

    class BoardPathPair:
        def __init__(self, board, path, astar_value):
            self.board = board
            self.path = path
            self.value = astar_value

        def __lt__(self, other):
            return self.value < other.value

    def __init__(self, heuristic):
        self.heap = []
        self.heuristic = heuristic

    def put(self, board_path_tup):
        board, path = board_path_tup
        heapq.heappush(self.heap, PriorityQueue.BoardPathPair(board, path, self.heuristic(board) + len(path)))

    def get(self):
        board_path = heapq.heappop(self.heap)
        return board_path.board, board_path.path

    def empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)
