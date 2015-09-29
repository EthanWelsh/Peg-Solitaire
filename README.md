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
=============
```
------------------------------
Search: tree-search on dfs 
Input File: input_files/sample04.txt
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(3, 2) --> (1, 2)
(3, 3) --> (1, 3)
(0, 2) --> (2, 2)
(2, 0) --> (0, 2)
(4, 2) --> (2, 0)
(1, 3) --> (3, 1)
(2, 0) --> (2, 2)
(3, 1) --> (1, 3)
(0, 2) --> (2, 4)
Duration: 0.0269 seconds
Nodes Visited: 33
Space: 12 nodes
------------------------------
------------------------------
Search: tree-search on bfs 
Input File: input_files/sample04.txt
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(3, 2) --> (1, 2)
(3, 3) --> (1, 3)
(0, 2) --> (2, 2)
(2, 0) --> (0, 2)
(4, 2) --> (2, 0)
(1, 3) --> (3, 1)
(2, 0) --> (2, 2)
(3, 1) --> (1, 3)
(0, 2) --> (2, 4)
Duration: 198.0089 seconds
Nodes Visited: 167668
Space: 88392 nodes
------------------------------
------------------------------
Search: graph-search on bfs 
Input File: input_files/sample04.txt
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(3, 2) --> (1, 2)
(3, 3) --> (1, 3)
(0, 2) --> (2, 2)
(2, 0) --> (0, 2)
(4, 2) --> (2, 0)
(1, 3) --> (3, 1)
(2, 0) --> (2, 2)
(3, 1) --> (1, 3)
(0, 2) --> (2, 4)
Duration: 185.0698 seconds
Nodes Visited: 2303
Space: 721 nodes
Visited Size: 2339
------------------------------
------------------------------
Search: graph-search on astar max_movable_pegs
Input File: input_files/sample04.txt
(0, 2) --> (2, 2)
(3, 2) --> (1, 2)
(2, 4) --> (0, 2)
(3, 3) --> (1, 3)
(0, 2) --> (2, 2)
(1, 1) --> (3, 3)
(2, 0) --> (2, 2)
(3, 3) --> (1, 1)
(4, 2) --> (2, 0)
(2, 0) --> (0, 2)
(0, 2) --> (2, 4)
Duration: 147.1836 seconds
Nodes Visited: 2225
Space: 274 nodes
Visited Size: 2343
------------------------------
------------------------------
Search: graph-search on astar max_moves
Input File: input_files/sample04.txt
(0, 2) --> (2, 2)
(2, 0) --> (0, 2)
(3, 2) --> (1, 2)
(2, 4) --> (2, 2)
(4, 2) --> (2, 4)
(2, 1) --> (2, 3)
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(3, 1) --> (1, 3)
(0, 2) --> (2, 4)
(2, 4) --> (2, 2)
Duration: 701.5600 seconds
Nodes Visited: 2218
Space: 532 nodes
Visited Size: 2343
------------------------------
------------------------------
Search: graph-search on astar min_moves
Input File: input_files/sample04.txt
(2, 4) --> (2, 2)
(4, 2) --> (2, 4)
(1, 1) --> (3, 3)
(2, 4) --> (4, 2)
(3, 1) --> (3, 3)
(2, 0) --> (2, 2)
(1, 3) --> (3, 1)
(0, 2) --> (2, 2)
(3, 3) --> (1, 1)
(4, 2) --> (2, 0)
(2, 0) --> (0, 2)
Duration: 147.0782 seconds
Nodes Visited: 2218
Space: 954 nodes
Visited Size: 2343
------------------------------
------------------------------
Search: tree-search on idastar min_moves
Input File: input_files/sample04.txt
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(3, 2) --> (1, 2)
(3, 3) --> (1, 3)
(0, 2) --> (2, 2)
(2, 0) --> (0, 2)
(4, 2) --> (2, 0)
(1, 3) --> (3, 1)
(2, 0) --> (2, 2)
(3, 1) --> (1, 3)
(0, 2) --> (2, 4)
Duration: 765.7645 seconds
Nodes Visited: 609858
Space: 11 nodes
------------------------------
```