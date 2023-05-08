from time import time



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

    print("Depth",depth)
    return bestMove
