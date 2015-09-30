from board import Spot


def max_moves(board):
    pegs_on_board = board.peg_count()
    moves = [move for move in board.get_possible_moves()]

    if len(moves) == 0:
        return float('inf')

    moves, _ = zip(*moves)
    pegs_with_move = len(list(set(moves)))
    return pegs_on_board - 1 - (pegs_with_move / pegs_on_board)


def min_moves(board):
    pegs_on_board = board.peg_count()
    moves = [move for move in board.get_possible_moves()]

    if len(moves) == 0:
        return float('inf')

    moves, _ = zip(*moves)
    moves = len(moves)
    return pegs_on_board - 1 - (moves / (moves + 1))


def max_movable_pegs(board):
    pegs_on_board = board.peg_count()
    moves = [move for move in board.get_possible_moves()]

    if len(moves) == 0:
        return float('inf')

    moves, _ = zip(*moves)
    moves = len(moves)
    return pegs_on_board - 1 - (1 / (moves + 1))


def manhattan_cost(board):
    man = 0
    number_of_pegs = 0

    for r in range(board.size):
        for c in range(board.size):
            if board.board[r, c] == Spot.PEG:
                number_of_pegs += 1
                for rr in range(board.size):
                    for cc in range(board.size):
                        if board.board[rr, cc] == Spot.PEG:
                            man += abs(r - rr) + abs(c - cc)
    return man / number_of_pegs


def pagoda_value(board):
    pass


def isolated_pegs(board):
    pass
