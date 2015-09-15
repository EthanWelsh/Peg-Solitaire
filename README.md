# Peg-Solitaire

Version: This particular solution is written using Python3.4.

Implementation Details
-----------------------
I used a fairly simple object that encapsulated 2d numpy character matrix in order to represent my board's state.
I considered using a boolean matrix instead (which would save space), but I decided that for the time being I valued the
simplicity of the program more than efficiency. I also toyed around with the idea of representing my states as a just a
list of moves (I'd also store the start state). Once again, this could vastly cut down on the space (although I'd have
to perform more calculations to find the matrix that is indicated by the list of moves), but I decided against it
because (for the time being) simplicity mattered most to me.

Sample Output
-------------
```
  0 1 2 3 4
0 o * * * *
1 * * * * .
2 * * * . .
3 * * . . .
4 * . . . .

0:	(0, 2) --> (0, 0)
1:	(2, 0) --> (0, 0)
Please select a move (or 'q' to quit): 1

  0 1 2 3 4
0 * * * * *
1 o * * * .
2 o * * . .
3 * * . . .
4 * . . . .

0:	(1, 2) --> (1, 0)
1:	(0, 2) --> (2, 0)
2:	(2, 2) --> (2, 0)
3:	(4, 0) --> (2, 0)
Please select a move (or 'q' to quit): 2

  0 1 2 3 4
0 * * * * *
1 o * * * .
2 * o o . .
3 * * . . .
4 * . . . .

0:	(1, 2) --> (1, 0)
1:	(3, 0) --> (1, 0)
2:	(0, 1) --> (2, 1)
3:	(0, 3) --> (2, 1)
4:	(0, 2) --> (2, 2)
5:	(0, 4) --> (2, 2)
6:	(4, 0) --> (2, 2)
Please select a move (or 'q' to quit): 6

  0 1 2 3 4
0 * * * * *
1 o * * * .
2 * o * . .
3 * o . . .
4 o . . . .

0:	(1, 2) --> (1, 0)
1:	(3, 0) --> (1, 0)
2:	(0, 1) --> (2, 1)
3:	(0, 3) --> (2, 1)
4:	(1, 3) --> (3, 1)
5:	(2, 0) --> (4, 0)
Please select a move (or 'q' to quit): 4

  0 1 2 3 4
0 * * * * *
1 o * * o .
2 * o o . .
3 * * . . .
4 o . . . .

0:	(1, 2) --> (1, 0)
1:	(3, 0) --> (1, 0)
2:	(1, 1) --> (1, 3)
3:	(0, 1) --> (2, 1)
4:	(0, 3) --> (2, 1)
5:	(0, 2) --> (2, 2)
6:	(2, 0) --> (4, 0)
Please select a move (or 'q' to quit): 5

  0 1 2 3 4
0 * * o * *
1 o * o o .
2 * o * . .
3 * * . . .
4 o . . . .

0:	(0, 4) --> (0, 2)
1:	(2, 0) --> (0, 2)
2:	(0, 0) --> (0, 2)
3:	(3, 0) --> (1, 0)
4:	(3, 1) --> (1, 3)
5:	(0, 1) --> (2, 1)
6:	(2, 0) --> (4, 0)
7:	(2, 2) --> (4, 0)
Please select a move (or 'q' to quit): 4

  0 1 2 3 4
0 * * o * *
1 o * o * .
2 * o o . .
3 * o . . .
4 o . . . .

0:	(0, 4) --> (0, 2)
1:	(2, 0) --> (0, 2)
2:	(0, 0) --> (0, 2)
3:	(3, 0) --> (1, 0)
4:	(0, 1) --> (2, 1)
5:	(0, 4) --> (2, 2)
6:	(2, 0) --> (4, 0)
Please select a move (or 'q' to quit): 5

  0 1 2 3 4
0 * * o * o
1 o * o o .
2 * o * . .
3 * o . . .
4 o . . . .

0:	(2, 0) --> (0, 2)
1:	(0, 0) --> (0, 2)
2:	(3, 0) --> (1, 0)
3:	(0, 1) --> (2, 1)
4:	(2, 0) --> (4, 0)
Please select a move (or 'q' to quit): 1

  0 1 2 3 4
0 o o * * o
1 o * o o .
2 * o * . .
3 * o . . .
4 o . . . .

0:	(0, 3) --> (0, 1)
1:	(0, 2) --> (0, 4)
2:	(3, 0) --> (1, 0)
3:	(2, 0) --> (4, 0)
Please select a move (or 'q' to quit): 0

  0 1 2 3 4
0 o * o o o
1 o * o o .
2 * o * . .
3 * o . . .
4 o . . . .

0:	(2, 0) --> (0, 2)
1:	(3, 0) --> (1, 0)
2:	(0, 1) --> (2, 1)
3:	(2, 0) --> (4, 0)
Please select a move (or 'q' to quit): 1

  0 1 2 3 4
0 o * o o o
1 * * o o .
2 o o * . .
3 o o . . .
4 o . . . .

0:	(1, 0) --> (1, 2)
1:	(0, 1) --> (2, 1)
Please select a move (or 'q' to quit): 1

  0 1 2 3 4
0 o o o o o
1 * o o o .
2 o * * . .
3 o o . . .
4 o . . . .

0:	(2, 2) --> (2, 0)
Please select a move (or 'q' to quit): 0

  0 1 2 3 4
0 o o o o o
1 * o o o .
2 * o o . .
3 o o . . .
4 o . . . .

0:	(2, 0) --> (0, 0)
1:	(1, 0) --> (3, 0)
Please select a move (or 'q' to quit): 0

Congratulations! You won!
  0 1 2 3 4
0 * o o o o
1 o o o o .
2 o o o . .
3 o o . . .
4 o . . . .
```