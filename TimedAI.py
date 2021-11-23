from time import time



#maxDuration est en secondes
def getBestMoveTime(ai,board,color,heuristic,maxDuration):

    startTime = time()
    bestMove = None
    depth = 0

    while time() - startTime < maxDuration:
        bestMove = ai(board,color,heuristic,depth)
        depth += 1

    return bestMove
