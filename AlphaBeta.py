from random import choice



def getBestMoveAB(board,color,heuristic,depth):

    bestMoves = []
    alpha = -160
    beta = 160

    for move in board.generate_legal_moves():

        board.push(move)
        moveScore = getMinAB(board,color,heuristic,depth,alpha,beta)

        if  moveScore > alpha:
            alpha = moveScore
            bestMoves = [move]

        elif moveScore == alpha:
            bestMoves += [move]

        board.pop()

    return choice(bestMoves)


def getMaxAB(board,color,heuristic,depth,alpha,beta):
    if depth == 0:
        return heuristic(board,color)

    for move in board.generate_legal_moves():

        board.push(move)
        score = getMinAB(board,color,heuristic,depth-1,alpha,beta)
        if  score > alpha:
            alpha = score
        if alpha >= beta:
            board.pop()
            return beta
        board.pop()

    return alpha



def getMinAB(board,color,heuristic,depth,alpha,beta):
    if depth == 0:
        return heuristic(board,color)

    for move in board.generate_legal_moves():

        board.push(move)
        score = getMaxAB(board,color,heuristic,depth-1,alpha,beta)
        if  score < beta:
            beta = score
        if alpha >= beta:
            board.pop()
            return alpha
        board.pop()

    return beta
