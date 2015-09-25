from src.board import Board


def max_moves(board):
    pegs_on_board = board.peg_count()
    pegs_with_move, _ = zip(board.get_possible_moves())
    pegs_with_move = len(list(set(pegs_with_move)))
    return pegs_on_board - 1 - (pegs_with_move / pegs_on_board)


def min_moves(board):
    pegs_on_board = board.peg_count()
    moves, _ = zip(board.get_possible_moves())
    moves = len(moves)
    return pegs_on_board - 1 - moves / (moves + 1)


def max_movable_pegs(board):
    pegs_on_board = board.peg_count()
    moves, _ = zip(board.get_possible_moves())
    moves = len(moves)
    return pegs_on_board - 1 - 1/(moves + 1)
