# TIC-TAC-TOE using minimax
A simple Human vs AI tic-tac-toe using [minimax algorithm](https://en.wikipedia.org/wiki/Minimax#Pseudocode). The AI never loses :)

Minimax works here because the max possible states of the board is $3^9<20000$ ('X' or 'O' or nothing in each cell). So the game tree is very small and easy to evaluate. For games like chess which has large no of states, we need to optimize minimax algo (e.g with alpha-beta pruning)