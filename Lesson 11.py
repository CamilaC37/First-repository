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

def test_evaluate():
    # Test when there is a win for 'x'
    board1 = "xxx-----------------"
    assert evaluate(board1) == 'x', f"Test failed for board: {board1}"
    
    # Test when there is a win for 'o'
    board2 = "------ooo-----------"
    assert evaluate(board2) == 'o', f"Test failed for board: {board2}"
    
    # Test when the board is full and results in a draw
    board3 = "xoxoxoxoxoxoxoxoxoxo"
    assert evaluate(board3) == '!', f"Test failed for board: {board3}"
    
    # Test when the game is still ongoing
    board4 = "xoxoxoxoxoxo-------"
    assert evaluate(board4) == '-', f"Test failed for board: {board4}"
    
    # Test an ongoing game with no immediate winner
    board5 = "xoxo---oxox--xoxox-"
    assert evaluate(board5) == '-', f"Test failed for board: {board5}"
    
    print("All evaluate tests passed!")

def test_move():
    # Test a valid move for 'x'
    board1 = "--------------------"
    new_board1 = move(board1, 'x', 5)
    assert new_board1 == "-----x--------------", f"Test failed for board: {board1} with move at position 5"
    
    # Test a valid move for 'o'
    board2 = "x-------------------"
    new_board2 = move(board2, 'o', 1)
    assert new_board2 == "xo------------------", f"Test failed for board: {board2} with move at position 1"
    
    print("All move tests passed!")

# Run the tests
test_evaluate()
test_move()

"""
1. What is a Python module and how does it differ from a Python package?
   - A Python module is a single file containing Python code, which can define functions, classes, and variables. It is a way to organize and reuse code. 
   A Python package, on the other hand, is a collection of modules organized in directories that include a special __init__.py file, making it easy to structure and distribute large codebases.

2. What are side effects and give some examples.
   - Side effects are that any changes in state or observable interactions with outside systems that occur when executing a function. 
   Examples include modifying a global variable, writing to a file, printing to the console, or altering the state of an external system like a database or an external service.

3. What are Exceptions and what to do if third-party code that we use throws them?
   - Exceptions are events that disrupt the normal flow of a program's execution, typically indicating errors. 
   When third-party code throws exceptions, you should handle them using try-except blocks to prevent the program from crashing, log the errors for debugging, 
   and potentially provide fallback behavior or user-friendly error messages.

4. Using which keywords can you create, throw and catch your new custom Exception?
    - You can create a new custom Exception by defining a class that inherits from the built-in Exception class. 
    You can throw an exception using the raise keyword and catch exceptions using the try-except block.
"""