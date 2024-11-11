import math

# Constants representing the players
HUMAN = 'O'
AI = 'X'

# Empty board initialization
board = [' ' for _ in range(9)]  # 3x3 board

# Display the Tic-Tac-Toe board
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check if the current board state is a win for a player
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

# Check for a draw
def check_draw(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    # Base cases: terminal states
    if check_winner(board, AI):
        return 1  # AI wins
    if check_winner(board, HUMAN):
        return -1  # Human wins
    if check_draw(board):
        return 0  # Draw

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
        return min_eval

# Get the best move for AI
def get_best_move(board):
    best_value = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            move_value = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move

# Main game loop
def play_game():
    while True:
        print_board(board)

        # Human move
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[human_move] = HUMAN

        if check_winner(board, HUMAN):
            print_board(board)
            print("Human wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = get_best_move(board)
        board[ai_move] = AI

        if check_winner(board, AI):
            print_board(board)
            print("AI wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
play_game()