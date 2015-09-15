import numpy as np


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
    board, directions = read_board_from_file('input_files/sample00.txt')
    print(board[0, 0])


if __name__ == '__main__':
    main()