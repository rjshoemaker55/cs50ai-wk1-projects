"""
Tic Tac Toe Player
"""

import math

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
    x_spaces = 0
    o_spaces = 0

    for row in board:
        for cell in row:
            if cell == 'X':
                x_spaces += 1
            elif cell == 'O':
                o_spaces += 1

    if x_spaces > o_spaces:
        return 'O'
    else:
        return 'X'


def actions(board):
    possible_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    player = player(board)
    copy.deepcopy(board)

    if action not in actions(board):
        raise RuntimeError('This action is not valid for this board.')

    board[action] == player
    return board


def winner(board):
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
