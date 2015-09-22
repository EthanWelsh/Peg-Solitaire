import numpy as np
import sys


class Board:
    def __init__(self, board, directions, heuristic=None):
        self.board = board
        self.size = board.shape[0]

        self.heuristic = heuristic

        if type(directions) is str:
            if directions == 'all':
                self.directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
            elif directions == 'ortho':
                self.directions = ['n', 'e', 's', 'w']
            elif directions == 'swne':
                self.directions = ['n', 'ne', 'e', 's', 'sw', 'w']
            else:
                assert False
        else:
            self.directions = directions

    @classmethod
    def board_from_file(cls, file_name):
        """
        :param file_name:
        :return: board_matrix: numpy character matrix
        :return: directions: string enumerating the directions travel is allowed
        """
        with open(file_name, 'r') as peg_file:
            directions, _, *matrix_lines = peg_file.readlines()

        board_matrix = np.array([[spot for spot in line.strip().split(' ')] for line in matrix_lines])
        return Board(board=board_matrix, directions=directions.strip())

    @classmethod
    def board_from_board(cls, other):
        new_board = Board(np.copy(other.board), other.directions, other.heuristic)
        return new_board

    def successors(self):
        moves = self.get_possible_moves()
        for move in moves:
            yield (move, self.make_move(*move))

    def check_peg(self, start_position, direction):
        return self._get_spot(start_position, direction) == '*'

    def check_free(self, start_position, direction):
        return self._get_spot(start_position, direction) == 'o'

    def is_goal(self):
        """
        Checks if the current board is in a goal state (IE there is only one pin left)
        :return: board_is_goal_state
        """
        pins = 0

        for r in range(self.size):
            for c in range(self.size):
                if self.board[r, c] == '*':
                    pins += 1

                if pins > 1:
                    return False
        return pins == 1

    def get_possible_moves(self):
        """
        :returns: a list of lists of tuples of tuples of possible moves from source > destination
        """
        for free_position in self._free_positions():
            yield from [(jump, free_position) for jump in self._possible_jumps_into_empty(free_position)]

    def make_move(self, source, destination):
        """
        :param source: The coordinate of the pin that you'd like to move
        :param destination: The coordinate of the empty position that you'd like to move the pin into
        :param apply: If you'd like to apply the move to the current board and change its matrix accordingly
        :return: new_board: a new board with the move applied
        """
        assert (not self._out_of_bounds(*source) and not self._out_of_bounds(*destination))
        assert (self.board[source] == '*')
        assert (self.board[destination] == 'o')
        assert ((source, destination) in self.get_possible_moves())

        new_board = Board.board_from_board(self)

        # Calculate the coordinates of the pixel that is between the source and destination
        hop = tuple(np.divide(np.add(source, destination), (2, 2)))
        assert self.board[hop] == '*'

        new_board.board[source] = 'o'
        new_board.board[destination] = '*'
        new_board.board[hop] = 'o'

        return new_board

    @staticmethod
    def _adjusts_coords_to_direction(start_position, direction):
        """
        :param start_position: The coordinates that you'd like to start from
        :param direction: The direction that you'd like to look in
        :return: The adjusted index of (r, c) after moving in a certain direction
        """
        r, c = start_position

        r -= direction.count('n')
        r += direction.count('s')
        c += direction.count('e')
        c -= direction.count('w')

        return r, c

    def _possible_jumps_into_empty(self, empty_coord):
        """
        Given the coordinate of an empty space, will return the locations of all the pegs that could jump into that cell
        :param empty_coord: the coordinate of the empty spot that you'd like to check from
        """
        assert self.board[empty_coord] == 'o'

        for direction in self.directions:
            if self.check_peg(empty_coord, direction) and self.check_peg(empty_coord, direction * 2):
                yield self._adjusts_coords_to_direction(empty_coord, direction * 2)

    def _free_positions(self):
        """
        Looks through the matrix and returns a list of empty spaces.
        :returns a list of (r, c) coordinates where blank spots can be found on the board.
        """
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r, c] == 'o':
                    yield (r, c)

    def _get_spot(self, start_position, direction):
        """
        :param start_position: The coordinates that you'd like to start from
        :param direction: The direction that you'd like to look in
        :return: the character at that position in the board
        """
        r, c = start_position
        if self._out_of_bounds(r, c):
            return '.'

        r, c = self._adjusts_coords_to_direction(start_position, direction)
        if self._out_of_bounds(r, c):
            return '.'

        return self.board[r, c]

    def _out_of_bounds(self, r, c):
        """
        Checks to see if a given r, c is out of bounds
        """
        return min(r, c) < 0 or max(r, c) >= self.size

    def __lt__(self, other):
        return self.heuristic(self.board) < self.heuristic(other.board)

    def __str__(self):
        ret = '  '
        for i in range(self.size):
            ret += str(i) + ' '
        ret += '\n'

        for r in range(self.size):
            ret += str(r) + ' '
            for c in range(self.size):
                ret += '{} '.format(self.board[r, c])
            ret += '\n'
        return ret


def main():
    board = Board.board_from_file(sys.argv[1])

    # Game loop
    while not board.is_goal():
        moves = board.get_possible_moves()

        print('\n{}'.format(board))

        # Print out a list of all possible moves
        if len(moves) == 0:
            print("You lost! Sorry")
            return 0

        for move_num, move in enumerate(moves):
            source, destination = move
            print('{}:\t{} --> {}'.format(move_num, source, destination))

        # Get input from the user as to which move to take next
        user_input = None
        while user_input is None:
            prompt = input("Please select a move (or 'q' to quit): ")

            if prompt == 'q':
                return 0
            if int(prompt) in range(len(moves)):
                user_input = int(prompt)
                break

        board = board.make_move(*moves[user_input])

    print('\nCongratulations! You won!')
    print(board)


if __name__ == '__main__':
    main()
