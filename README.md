# Peg-Solitaire

Written using Python3.4 with numpy 1.9.2

Analysis of Search Strategies
=============================
Of all the search strategies, depth first search (DFS) performed the best by far. I had anticipated that it would perform far better than breadth first search (BFS): all the available solutions occur at depth 13, and they are fairly numerous. What I had not anticipated was how poorly A* and IDA* performed. It occurred to me that the heuristics that we were testing with were not ideal, but I had presumed that they would manage to find a solution at least as quickly as DFS. In actuality though, the opposite it true: A* found a solution only marginally faster than BFS, and was several factors of magnitude slower than uninformed DFS. Upon more careful inspection this is due to the fact that the heuristics that are being used are extremely poor predictors of performance.

Applying DFS to the peg puzzle is especially effective due to the fact the nature of the puzzle solves most of the ‘problems’ that typically emerge in dealing with DFS: namely completeness and optimality. Regarding completeness, naive DFS in most search spaces can easily end up getting trapped in loops around the same states. In the peg puzzle, this is not the case: although there are duplicate states, no move will ever lead to itself again and so there is not risk of falling into loops. Regarding optimality, the peg puzzle does not really have an ‘optimal’ solution, in that all solutions will always occur after the same number of moves and therefore all paths are in fact optimal.

Extra Credit
============

Manhattan Distance
------------------
For my extra credit, I implemented a manhattan distance function that calculated the manhattan distance from every peg to every other peg on the board, and then divided that score by the number of pegs on the board. I chose this heuristic because it favored board configurations that were more clumped together (the average distance being smaller) and punished boards that were too spread out (which might indicate a path leading to a dead end). Overall, the heuristic performed quite well! It was the only one of the heuristics to beat the simple DFS implementation, and performed consistently better by several factors of magnitude on every board I could find than anything else.

One downside of this heuristic is the abysmal computational overhead. My manhattan distance heuristic takes O(N^4) operations, where N is the length or width of the board. The heuristic performed quite well on boards under 8x8, but past this point the heuristic slowed down the search considerably.

Symmetry Check
--------------
I also implemented another form of graph search that checks for symmetrical board configurations, and adds those to the visited list too. The symmetry check helps prune the search tree of duplicate branches that are merely a rotation of another a branch.

Over all, I was enormously impressed by huge efficiency boost that was granted by checking for symmetrical branches. On [the provided search board](/input_files/ortho.txt), every tested search strategy and heuristic performed vastly better with symmetry checking than with normal tree search. Symmetry checking is especially effective in puzzles that posses vertical *and* horizontal symmetry, as they can take use of all 3 'reflections' to prune their search tree.

Of course, duplication checking has its downfalls. The process of creating the new reflecting boards is a computationally non-trivial operation. Perhaps even more damningly, using reflection checking will cause 4 entries on visited list for every node visited. That being said, I have found the use of symmetry-checking did not significantly increase the size of the visited list. On the above mentioned board, the search strategies yielded an average of a 2% increase in the size of the visited list, but for a tradeoff of an over 300% decrease in computational time over the graph-search alternative.

Sample Output
=============
```
------------------------------
Search: tree-search on dfs
Input File: input_files/ortho.txt
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
Duration: 0.0650 seconds
Nodes Visited: 33
Space: 12 nodes
------------------------------
------------------------------
Search: tree-search on bfs
Input File: input_files/ortho.txt
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
Duration: 331.4075 seconds
Nodes Visited: 167668
Space: 88392 nodes
------------------------------
------------------------------
Search: graph-search on bfs
Input File: input_files/ortho.txt
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
Duration: 70.2885 seconds
Nodes Visited: 2303
Space: 721 nodes
Visited Size: 2339
------------------------------
------------------------------
Search: symmetry on bfs
Input File: input_files/ortho.txt
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
Duration: 23.5259 seconds
Nodes Visited: 585
Space: 195 nodes
Visited Size: 2372
------------------------------
------------------------------
Search: graph-search on astar max_movable_pegs
Input File: input_files/ortho.txt
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
Duration: 61.0204 seconds
Nodes Visited: 2225
Space: 274 nodes
Visited Size: 2343
------------------------------
------------------------------
Search: symmetry on astar max_movable_pegs
Input File: input_files/ortho.txt
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
Duration: 19.4585 seconds
Nodes Visited: 582
Space: 73 nodes
Visited Size: 2376
------------------------------
------------------------------
Search: graph-search on astar max_moves
Input File: input_files/ortho.txt
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
Duration: 59.7559 seconds
Nodes Visited: 2218
Space: 532 nodes
Visited Size: 2343
------------------------------
------------------------------
Search: symmetry on astar max_moves
Input File: input_files/ortho.txt
(0, 2) --> (2, 2)
(2, 0) --> (0, 2)
(3, 2) --> (1, 2)
(2, 4) --> (2, 2)
(0, 2) --> (2, 4)
(2, 1) --> (2, 3)
(2, 4) --> (2, 2)
(4, 2) --> (2, 0)
(3, 3) --> (1, 1)
(2, 0) --> (0, 2)
(0, 2) --> (2, 2)
Duration: 20.0654 seconds
Nodes Visited: 576
Space: 282 nodes
Visited Size: 2376
------------------------------
------------------------------
Search: graph-search on astar min_moves
Input File: input_files/ortho.txt
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
Duration: 61.1046 seconds
Nodes Visited: 2218
Space: 954 nodes
Visited Size: 2343
------------------------------
------------------------------
Search: symmetry on astar min_moves
Input File: input_files/ortho.txt
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(3, 1) --> (1, 3)
(2, 0) --> (2, 2)
(1, 3) --> (3, 1)
(4, 2) --> (2, 2)
(0, 2) --> (2, 0)
(2, 0) --> (4, 2)
(3, 3) --> (1, 3)
(1, 3) --> (3, 1)
(4, 2) --> (2, 0)
Duration: 21.1977 seconds
Nodes Visited: 572
Space: 298 nodes
Visited Size: 2376
------------------------------
------------------------------
Search: graph-search on astar man
Input File: input_files/ortho.txt
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(4, 2) --> (2, 4)
(2, 0) --> (4, 2)
(1, 1) --> (3, 1)
(3, 1) --> (1, 3)
(2, 4) --> (2, 2)
(3, 2) --> (1, 2)
(0, 2) --> (2, 2)
(1, 3) --> (3, 1)
(4, 2) --> (2, 0)
Duration: 0.1688 seconds
Nodes Visited: 24
Space: 33 nodes
Visited Size: 55
------------------------------
------------------------------
Search: symmetry on astar man
Input File: input_files/ortho.txt
(0, 2) --> (2, 2)
(2, 4) --> (0, 2)
(4, 2) --> (2, 4)
(2, 0) --> (4, 2)
(1, 1) --> (3, 1)
(3, 1) --> (1, 3)
(2, 4) --> (2, 2)
(3, 2) --> (1, 2)
(0, 2) --> (2, 2)
(1, 3) --> (3, 1)
(4, 2) --> (2, 0)
Duration: 0.1817 seconds
Nodes Visited: 23
Space: 28 nodes
Visited Size: 196
------------------------------
------------------------------
Search: tree-search on idastar min_moves
Input File: input_files/ortho.txt
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
Duration: 2239.1996 seconds
Nodes Visited: 609858
Space: 11 nodes
------------------------------
```
