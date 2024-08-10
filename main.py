# This file is where the tic-tac-toe game is implemented. 
# The board is represented as a 3x3 list of lists, 
# where each element is a string representing the state of the board at that position. 
# The functions display_board, update_board, is_valid_move, is_winner, is_tie, and minimax are used to display the board, 
# update the board with a player's move, check if a move is valid, check if a player has won, check if the game is a tie, 
# and implement the minimax algorithm to determine the best move for the computer, respectively. 
# The PLAYER and COMPUTER constants are used to represent the player and computer symbols, respectively.

# Implementing the game logic
from setup import *

while not is_winner(PLAYER) and not is_winner(COMPUTER) and not is_tie():
    display_board()
    while True:
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        if is_valid_move(row, col):
            update_board(row, col, PLAYER)
            break
        else:
            print('Invalid move. Try again.')
    if is_winner(PLAYER):
        display_board()
        print('You win!')
        break
    elif is_tie():
        display_board()
        print('It\'s a tie!')
        break
    computer_move()
    if is_winner(COMPUTER):
        display_board()
        print('Computer wins!')
        break
    elif is_tie():
        display_board()
        print('It\'s a tie!')
        break
