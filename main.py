import numpy as np


class Board:
    def __init__(self, board):
        self.board = board
        self.size = board.shape[0]

    def check_peg(self, start_position, direction):
        return self._get_spot(start_position, direction) == '*'

    def check_free(self, start_position, direction):
        return self._get_spot(start_position, direction) == 'o'

    def _get_spot(self, start_position, direction):
        r, c = start_position

        if self._out_of_bounds(r, c):
            return '.'

        if 'n' in direction:
            r -= 1
        if 'e' in direction:
            c += 1
        if 's' in direction:
            r += 1
        if 'w' in direction:
            c -= 1

        if self._out_of_bounds(r, c):
            return '.'

        return self.board[r, c]

    def _out_of_bounds(self, r, c):
        return min(r, c) < 0 or max(r, c) > self.size

    def get_blank_spots(self):
        positions = []
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r, c] == 'o':
                    positions.append((r, c))

        return positions


def read_board_from_file(file_name):
    """
    :param file_name:
    :return: board_matrix: numpy character matrix
    :return: directions: string enumerating the directions travel is allowed
    """
    with open(file_name, 'r') as peg_file:
        directions, _, *matrix_lines = peg_file.readlines()

    board_matrix = np.array([[spot for spot in line.strip().split(' ')] for line in matrix_lines])
    return board_matrix, directions


def main():
    matrix, directions = read_board_from_file('input_files/test.txt')
    board = Board(matrix)
    print(board.get_blank_spots())


if __name__ == '__main__':
    main()
