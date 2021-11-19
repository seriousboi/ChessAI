from random import choice



def getBestMoveMM(board,color,heuristic,depth):

    bestMoves = []
    bestScore = -160

    for move in board.generate_legal_moves():

        board.push(move)
        moveScore = minMax(board,color,heuristic,depth)

        if  moveScore > bestScore:
            bestMoves = [move]
            bestScore = moveScore
        elif moveScore == bestScore:
            bestMoves += [move]

        board.pop()

    return choice(bestMoves)



def maxMin(board,color,heuristic,depth):

    if depth == 0:
        return heuristic(board,color)

    best = -160
    for move in board.generate_legal_moves():

        board.push(move)
        score = minMax(board,color,heuristic,depth-1)
        if  score > best:
            best = score
        board.pop()

    return best



def minMax(board,color,heuristic,depth):

    if depth == 0:
        return heuristic(board,color)

    worst = 160
    for move in board.generate_legal_moves():

        board.push(move)
        score = maxMin(board,color,heuristic,depth-1)
        if  score < worst:
            worst = score
        board.pop()

    return worst
