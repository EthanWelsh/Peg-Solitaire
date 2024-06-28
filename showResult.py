from board import Board, Spot
from matplotlib import animation, pyplot as plt
import numpy as np

# filename = 'input_files/ortho.txt'
filename = input('Please enter your input file name: ')
board = Board.board_from_file(filename)

result = []
result_filename = 'output_files/' + filename.split('/')[-1]
with open(result_filename, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].startswith('Steps:'):
            steps = int(lines[i].split()[1])
            result = lines[i+1:i+1+steps]
            break


moves = []
for line in result:
    # print(line)
    start, end = line.strip().split(' --> ')
    start = tuple(map(int, start[1:-1].split(', ')))
    end = tuple(map(int, end[1:-1].split(', ')))
    moves.append((start, end))

def MySquare(x, y, color):
    return plt.Rectangle((x + 0.05, y + 0.05), 0.9, 0.9, color=color)

def addSquare(x, y, color, ax):
    ax.add_patch(MySquare(x, y, color))

def InitBoard(board, ax):
    for x in range(board.size):
        for y in range(board.size):
            if board.board[x, y] == Spot.PEG:
                addSquare(board.size - y, board.size - x, 'blue', ax)
            elif board.board[x, y] == Spot.FREE:
                addSquare(board.size - y, board.size - x, 'white', ax)
            else:
                addSquare(board.size - y, board.size - x, 'black', ax)

def moveUpdateSqaure(board, move, ax):
    start, end = move
    hop = tuple(np.array(np.divide(np.add(start, end), (2, 2)), dtype=np.int32))
    addSquare(board.size - start[1], board.size - start[0], 'white', ax)
    addSquare(board.size - hop[1], board.size - hop[0], 'white', ax)
    addSquare(board.size - end[1], board.size - end[0], 'blue', ax)

fig1 = plt.figure(figsize=(8, 8))
plt.ion()
ax1 = fig1.add_subplot(111)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

# plt.show()

def update(i, board, moves, ax):
    if i == 0:
        InitBoard(board, ax1) 
    moveUpdateSqaure(board, moves[i], ax)

anime =animation.FuncAnimation(fig1, update, frames=len(moves), fargs=(board, moves, ax1), interval=1000)
anime_filename = 'animations/' + filename.split('/')[-1].split('.')[0] + '.html'
with open(anime_filename, "w") as f:
    print(anime.to_jshtml(), file=f)

print('Animation file has saved to ' + anime_filename + '.')