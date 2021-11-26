from random import shuffle
from time import time



def stillTime(startTime,maxDuration):
    return time() - startTime < maxDuration
    


def ABtimed(board,color,heuristic,depth,startTime,maxDuration):
    alpha = -161
    beta = 161

    moves = []
    for move in board.generate_legal_moves():
        moves += [move]
    shuffle(moves)

    for move in moves:

        board.push(move)
        moveScore = getMinABtimed(board,color,heuristic,depth,alpha,beta,startTime,maxDuration)

        if  moveScore > alpha:
            alpha = moveScore
            bestMove = move
        board.pop()

    return bestMove



def getMaxABtimed(board,color,heuristic,depth,alpha,beta,startTime,maxDuration):
    if not stillTime(startTime,maxDuration):
        return 0

    if depth == 0 or board.is_game_over():
        return heuristic(board,color)

    for move in board.generate_legal_moves():

        board.push(move)

        score = getMinABtimed(board,color,heuristic,depth-1,alpha,beta,startTime,maxDuration)
        if  score > alpha:
            alpha = score

        if alpha >= beta:
            board.pop()
            return beta

        board.pop()

    return alpha



def getMinABtimed(board,color,heuristic,depth,alpha,beta,startTime,maxDuration):
    if not stillTime(startTime,maxDuration):
        return 0

    if depth == 0 or board.is_game_over():
        return heuristic(board,color)

    for move in board.generate_legal_moves():

        board.push(move)

        score = getMaxABtimed(board,color,heuristic,depth-1,alpha,beta,startTime,maxDuration)
        if  score < beta:
            beta = score

        if alpha >= beta:
            board.pop()

            return alpha

        board.pop()


    return beta
