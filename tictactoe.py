"""
Tic Tac Toe Player
"""

import math
import copy
from util import Node, StackFrontier, QueueFrontier
import time
from pygame.sprite import RenderUpdates

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
    xnumber = 0
    onumber = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xnumber += 1
            elif board[i][j] == O:
                onumber += 1
    if xnumber > onumber:
        return O
    else:
        return X


def actions(board):
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    xnumber = 0
    onumber = 0
    xtrue = True
    if board[action[0]][action[1]] != EMPTY:
        raise Exception
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xnumber += 1
            elif board[i][j] == O:
                onumber += 1
    if xnumber > onumber:
        xtrue = False
    newboard = copy.deepcopy(board)
    if xtrue == True:
        newboard[action[0]][action[1]] = X
    else:
        newboard[action[0]][action[1]] = O
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == X and board[i][1] == X and board[i][2] == X) or (board[0][i] == X and board[1][i] == X and board[2][i] == X):
            return X
        elif (board[i][0] == O and board[i][1] == O and board[i][2] == O) or (board[0][i] == O and board[1][i] == O and board[2][i] == O):
            return O
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    draw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                draw = False
    if draw == True:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        return 0
    return None


def minimax(board, depth, lastbest):
    start_time = time.time()
    Player = player(board)
    Actions = actions(board)
    Bestmove = ()
    if Player == X:
        Bestvalue = -math.inf
    else:
        Bestvalue = math.inf  
    if depth == 0:
        if Player == X:
            lastbest = -math.inf
        else:
            lastbest = math.inf 
    if terminal(board):
        score = utility(board)
        return score    
    for i in Actions:
        newboard = result(board, i)
        Result = minimax(newboard, depth + 1, lastbest)
        if Player == X:
            if Result > Bestvalue:
                Bestmove = i
                Bestvalue = Result
            if Result > lastbest and lastbest != -math.inf and depth != 0:
                break
        else:
            if Result < Bestvalue:
                Bestmove = i
                Bestvalue = Result
            if Result < lastbest and lastbest != math.inf and depth != 0:
                break
        lastbest = Bestvalue
    if depth != 0:
        return Bestvalue
    if depth == 0:
        print("--- %s seconds ---" % (time.time() - start_time))
        return Bestmove
