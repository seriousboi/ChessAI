from time import time
from random import shuffle



def stillTime(startTime,maxDuration):
    return time() - startTime < maxDuration



#maxDuration est en secondes
def getBestMoveTime(ai,board,color,heuristic,maxDuration):

    startTime = time()
    bestMove = None
    depth = 0

    while stillTime(startTime,maxDuration):
        nextMove = ai(board,color,heuristic,depth,startTime,maxDuration)

        #on vérifie si le l'ia n'a pas été interrompue
        if stillTime(startTime,maxDuration):
            bestMove = nextMove

        depth += 1

    return bestMove



def ABtime(board,color,heuristic,depth,startTime,maxDuration):
    alpha = -161
    beta = 161

    moves = []
    for move in board.generate_legal_moves():
        moves += [move]
    shuffle(moves)

    for move in moves:

        board.push(move)
        moveScore = getMinABtime(board,color,heuristic,depth,alpha,beta,startTime,maxDuration)

        if  moveScore > alpha:
            alpha = moveScore
            bestMove = move
        board.pop()

    return bestMove



def getMaxABtime(board,color,heuristic,depth,alpha,beta,startTime,maxDuration):
    if not stillTime(startTime,maxDuration):
        return 0

    if depth == 0 or board.is_game_over():
        return heuristic(board,color)

    for move in board.generate_legal_moves():

        board.push(move)

        score = getMinABtime(board,color,heuristic,depth-1,alpha,beta,startTime,maxDuration)
        if  score > alpha:
            alpha = score

        if alpha >= beta:
            board.pop()
            return beta

        board.pop()

    return alpha



def getMinABtime(board,color,heuristic,depth,alpha,beta,startTime,maxDuration):
    if not stillTime(startTime,maxDuration):
        return 0

    if depth == 0 or board.is_game_over():
        return heuristic(board,color)

    for move in board.generate_legal_moves():

        board.push(move)

        score = getMaxABtime(board,color,heuristic,depth-1,alpha,beta,startTime,maxDuration)
        if  score < beta:
            beta = score

        if alpha >= beta:
            board.pop()

            return alpha

        board.pop()


    return beta
