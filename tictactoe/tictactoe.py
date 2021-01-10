"""
Tic Tac Toe Player
"""
import copy
import math
from random import randint

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
    elif terminal(board):
        return None
    else:
        return 'X'


def actions(board):
    possible_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))
    print(possible_actions)
    return possible_actions


def result(board, action):
    (i, j) = action

    if board[i][j] is not EMPTY:
        raise RuntimeError('This move is not valid.')

    new_board = copy.deepcopy(board)
    play = player(board)

    new_board[i][j] = play

    return new_board


def winner(board):
    print('in winner')
    # straight across top row
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]

    # straight across middle row
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]

    # straight across bottom row
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]

    # straight down left column
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]

    # straight down center column
    if board[0][1] == board[1][1] and board[0][1] == board[1][2]:
        return board[0][1]

    # straight down right column
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]

    # diagonal top-left to bottom-right
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]

    # diagonal bottom-left to top-right
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        return board[2][0]

    return None


def terminal(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    if board == initial_state():
        return (randint(0, 2), randint(0, 2))

    if player(board) == 'X':
        value = -math.inf
        move = (-1, -1)
        for action in actions(board):
            minv = MIN_VALUE(result(board, action))
            if minvalue > value:
                value = minvalue
                move = action
        return move

    if player(board) == 'O':
        value = math.inf
        move = (-1, -1)
        for action in actions(board):
            maxvalue = MAX_VALUE(result(board, action))
            if maxvalue < value:
                value = maxv
                move = action
        return move


def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board, action)))
    return v


def MIN_VALUE(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, MAX_VALUE(result(board, action)))
    return v
