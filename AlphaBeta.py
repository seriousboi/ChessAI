import random



def getBestMoveAB(board,color,heuristic,depth):
    alpha = -161
    beta = 161

    moves = []
    for move in board.generate_legal_moves():
        moves += [move]
    random.shuffle(moves)

    for move in moves:

        board.push(move)
        moveScore = getMinAB(board,color,heuristic,depth,alpha,beta)

        if  moveScore > alpha:
            alpha = moveScore
            bestMove = move
        board.pop()

    return bestMove



def getMaxAB(board,color,heuristic,depth,alpha,beta):
    if depth == 0 or board.is_game_over():
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
    if depth == 0 or board.is_game_over():
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
