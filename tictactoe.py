"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
           [EMPTY, EMPTY, EMPTY],
           [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return "X"
    xcount = 0
    ocount = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == "X":
                xcount += 1
            elif board[i][j] == "O":
                ocount += 1
    if xcount > ocount:
        return "O"
    else:
        return "X"

        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        print(action)
        raise NameError('InvalidActionException')
    board_copy = copy.deepcopy(board)
    i, j = action
    board_copy[i][j] = player(board)

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
       
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game if over, False otherwise.
    """

    if winner(board):
        return True

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0

final_action = None
def minimax(board):
    """
    Returns the optimal action (i, j) for the current player on the board.
    """
    global final_action

    if terminal(board):
        return None
    
    if player(board) ==  "X":
        #max_player
        value = max_value(board)
        print("max_player")
    else:
        #min_player
        value = min_value(board)
        print("min_player")
    print(value)
    return final_action

def max_value(board):
    global final_action

    if terminal(board):
        return utility(board)

    v = float('-inf')
    for action in actions(board):
        min_val = min_value(result(board, action))
        if min_val >= v:
            final_action = action
        v = max(v,min_val)
        if v == 1:
            final_action = action
            return v
       
    return v

def min_value(board):

    global final_action

    if terminal(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        max_val = max_value(result(board, action))
        if max_val <= v:
            final_action = action
        v = min(v, max_val)
        if v == -1:
            final_action = action
            return v
        
    return v