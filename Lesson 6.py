import random

def evaluate(board: str) -> str:
    # Check for a win for 'x'
    if 'xxx' in board:
        return 'x'
    # Check for a win for 'o'
    elif 'ooo' in board:
        return 'o'
    # Check if the board is full
    elif '-' not in board:
        return '!'
    # The game is still ongoing
    else:
        return '-'

def move(board: str, mark: str, position: int) -> str:
    if position < 0 or position >= len(board):
        raise ValueError("Position must be between 0 and 19.")
    if board[position] != '-':
        raise ValueError("Position is already occupied.")
    if mark not in ('x', 'o'):
        raise ValueError("Mark must be 'x' or 'o'.")
    
    # Place the mark on the board
    new_board = board[:position] + mark + board[position + 1:]
    return new_board

def player_move(board: str, mark: str) -> str:
    while True:
        try:
            position = int(input("Enter the position (0-19) where you want to place your mark: "))
            if position < 0 or position >= 20:
                print("Invalid position! Please enter a number between 0 and 19.")
            elif board[position] != '-':
                print("Position already occupied! Please choose another position.")
            else:
                return move(board, mark, position)
        except ValueError:
            print("Invalid input! Please enter a valid number between 0 and 19.")

def pc_move(board: str) -> str:
    while True:
        position = random.randint(0, 19)
        if board[position] == '-':
            return move(board, 'o', position)

def tictactoe_1d():
    board = "-" * 20
    current_player = 'x'
    
    while True:
        print(f"Current board: {board}")
        if current_player == 'x':
            board = player_move(board, current_player)
        else:
            board = pc_move(board)
        
        result = evaluate(board)
        
        if result in ('x', 'o'):
            print(f"Player {result} wins!")
            print(f"Final board: {board}")
            break
        elif result == '!':
            print("The game is a draw!")
            print(f"Final board: {board}")
            break
        
        # Switch player
        current_player = 'o' if current_player == 'x' else 'x'

if __name__ == "__main__":
    tictactoe_1d()