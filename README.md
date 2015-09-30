# Peg-Solitaire

Written using Python3.4 with numpy 1.9.2

Analysis of Search Strategies
=============================
Of all the search strategies, depth first search (DFS) performed the best by far. I had anticipated that it would perform far better than breadth first search (BFS): all the available solutions occur at depth 13, and they are fairly numerous. What I had not anticipated was how poorly A* and IDA* performed. It occurred to me that the heuristics that we were testing with were not ideal, but I had presumed that they would manage to find a solution at least as quickly as DFS. In actuality though, the opposite it true: A* found a solution only marginally faster than BFS, and was several factors of magnitude slower than uninformed DFS. Upon more careful inspection this is due to the fact that the heuristics that are being used are extremely poor predictors of performance.

Applying DFS to the peg puzzle is especially effective due to the fact the nature of the puzzle solves most of the ‘problems’ that typically emerge in dealing with DFS: namely completeness and optimality. Regarding completeness, naive DFS in most search spaces can easily end up getting trapped in loops around the same states. In the peg puzzle, this is not the case: although there are duplicate states, no move will ever lead to itself again and so there is not risk of falling into loops. Regarding optimality, the peg puzzle does not really have an ‘optimal’ solution, in that all solutions will always occur after the same number of moves and therefore all paths are in fact optimal.

*Extra Credit*: For my extra credit, I implemented a manhattan distance function that calculated the manhattan distance from every peg to every other peg on the board, and then divided that score by the number of pegs on the board. I chose this heuristic because it favored board configurations that were more clumped together (the average distance being smaller) and punished boards that were too spread out (which might indicate a path leading to a dead end). Overall, the heuristic performed quite well! It was the only one of the heuristics to beat the simple DFS implementation, and performed consistently better by several factors of magnitude on every board I could find than anything else.

One downside of this heuristic is the abismal computational overhead. My manhattan distance heuristic takes O(N^4) operations, where N is the length or width of the board. The heuristic performed quite well on boards under 8x8, but past this point the heuristic slowed down the search considerably.


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
