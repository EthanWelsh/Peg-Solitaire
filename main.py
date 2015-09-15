import numpy as np


class Board:
    def __init__(self, board, directions):
        self.board = board
        self.size = board.shape[0]

        if directions == 'all':
            self.directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        elif directions == 'ortho:':
            self.directions = ['n', 'e', 's', 'w']
        elif directions == 'swne':
            self.directions = ['n', 'ne', 'e', 's', 'sw', 'w']
        else:
            assert False

    def check_peg(self, start_position, direction):
        return self._get_spot(start_position, direction) == '*'

    def check_free(self, start_position, direction):
        return self._get_spot(start_position, direction) == 'o'

    def get_possible_moves(self):
        """
        :returns: a list of lists of tuples of tuples of possible moves from source > destination
        """
        moves = []
        for free_position in self._free_positions():
            jumps = [(jump, free_position) for jump in self._possible_jumps_into_empty(free_position)]
            moves.extend(jumps)
        return moves

    def _move_direction(self, start_position, direction):
        """
        :param start_position: The coordinates that you'd like to start from
        :param direction: The direction that you'd like to look in
        :return: The adjusted index of (r, c) after moving in a certain direction
        """
        r, c = start_position

        if 'n' in direction:
            r -= 1 * direction.count('n')
        if 'e' in direction:
            c += 1 * direction.count('e')
        if 's' in direction:
            r += 1 * direction.count('s')
        if 'w' in direction:
            c -= 1 * direction.count('w')

        return r, c

    def _get_spot(self, start_position, direction):
        """
        :param start_position: The coordinates that you'd like to start from
        :param direction: The direction that you'd like to look in
        :return: the character at that position in the board
        """
        r, c = start_position

        if self._out_of_bounds(r, c):
            return '.'

        r, c = self._move_direction(start_position, direction)

        if self._out_of_bounds(r, c):
            return '.'

        return self.board[r, c]

    def _out_of_bounds(self, r, c):
        """
        Checks to see if a given r, c is out of bounds
        """
        return min(r, c) < 0 or max(r, c) > self.size

    def _free_positions(self):
        """
        Looks through the matrix and returns a list of empty spaces.
        :returns a list of (r, c) coordinates where blank spots can be found on the board.
        """
        positions = []
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r, c] == 'o':
                    positions.append((r, c))

        return positions

    def _possible_jumps_into_empty(self, empty_coord):
        """
        Given the coordinate of an empty space, will return the locations of all the pegs that could jump into that cell
        :param empty_coord: the coordinate of the empty spot that you'd like to check from
        """
        assert self.board[empty_coord] == 'o'
        possible_jumps = []

        for direction in self.directions:
            if self.check_peg(empty_coord, direction) and self.check_peg(empty_coord, direction * 2):
                possible_jumps.append(self._move_direction(empty_coord, direction * 2))

        return possible_jumps


def read_board_from_file(file_name):
    """
    :param file_name:
    :return: board_matrix: numpy character matrix
    :return: directions: string enumerating the directions travel is allowed
    """
    with open(file_name, 'r') as peg_file:
        directions, _, *matrix_lines = peg_file.readlines()

    board_matrix = np.array([[spot for spot in line.strip().split(' ')] for line in matrix_lines])
    return board_matrix, directions.strip()


def main():
    matrix, directions = read_board_from_file('input_files/test.txt')
    board = Board(matrix, directions)


if __name__ == '__main__':
    main()
