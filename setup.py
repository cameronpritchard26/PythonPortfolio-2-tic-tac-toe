# This file contains the board and functions used for tic-tac-toe

# Setting the player to be 'X' and the computer to be 'O'
PLAYER = 'X'
COMPUTER = 'O'

# Creating the board
board = [[' ' for i in range(3)] for j in range(3)]

def display_board() -> None:
    """Displays the board and the current state of the game"""
    print('  0 1 2')
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(board[i][j], end=' ')
        print()

def update_board(row, col, player) -> None:
    """Updates the board with the player's move"""
    board[row][col] = player

def is_valid_move(row, col) -> bool:
    """Checks if the move is valid"""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def is_winner(player) -> bool:
    """Checks if the player has won"""
    for i in range(3):
        # Checking if all elements in a row or column are the same
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # Checking if all elements in a diagonal are the same
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    # If no winning condition is met
    return False

def is_tie() -> bool:
    """Checks if the game is a tie"""
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(is_maximizing) -> int:
    """Minimax algorithm to determine the best move for the computer"""
    # Determining if the game has ended
    if is_winner(PLAYER):
        return -1
    if is_winner(COMPUTER):
        return 1
    if is_tie():
        return 0

    # Maximizing the computer's score and minimizing the player's score
    if is_maximizing:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = COMPUTER
                    score = minimax(False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    score = minimax(True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def computer_move() -> None:
    """Determines the computer's move"""
    best_score = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = COMPUTER
                score = minimax(False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    update_board(best_move[0], best_move[1], COMPUTER)