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
