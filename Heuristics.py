import chess




def betterHeuristic(board,color):
    if board.is_game_over():
        if board.outcome().winner == color:
            return 160
        elif board.outcome().winner == (not color):
            return -160
        elif board.outcome().winner == None:
            return 0

    hasQueen = False
    enemyHasQueen = False

    kingSquare = None
    enemyKingSquare = None

    map = board.piece_map()
    score = 0

    for square in map:
        piece = map[square]

        if piece.piece_type == chess.PAWN:
            value = 1 + getCentralPieceBonus(square) #getAdvancedPawnBonus(piece.color,square)

        elif piece.piece_type == chess.KNIGHT:
            value = 3 + getCentralPieceBonus(square)

        elif piece.piece_type == chess.BISHOP:
            value = 3.25 #+ getCentralPieceBonus(square)

        elif piece.piece_type == chess.ROOK:
            value = 5 + getRookSquareBonus(square,color)

        elif piece.piece_type == chess.QUEEN:
            value = 9
            if piece.color == color:
                hasQueen = True
            else:
                enemyHasQueen = True

        elif piece.piece_type == chess.KING:
            value = 0
            if piece.color == color:
                kingSquare = square
            else:
                enemyKingSquare = square

        if piece.color != color:
            value = -value

        score += value

    #on favorise un roi protégé si la reine est sur le plateau
    #on favorise un roi central si la reine enemie n'est plus sur le plateau

    if enemyHasQueen:
        score += getCetralKingSquareMalus(kingSquare,color)
    else:
        score += getCentralPieceBonus(kingSquare)*2

    if hasQueen:
        score -= getCetralKingSquareMalus(enemyKingSquare,not color)
    else:
        score -= getCentralPieceBonus(enemyKingSquare)*2

    # /!\ mauvais, incite principalement a ne pas castle
    if board.has_castling_rights(color):
        score += 0.2
    if  board.has_castling_rights(not color):
        score -= 0.2

    return score



#+1 au centre, +0.5 autour du centre, +0 à une case du bord, -0.5 au bord (*1/2)
def getCentralPieceBonus(square):
    fileBonus = (1 - 0.5*(abs(3.5-chess.square_file(square))-0.5))/2
    rankBonus = (1 - 0.5*(abs(3.5-chess.square_rank(square))-0.5))/2
    return min(fileBonus,rankBonus)



squares = [
['a1','a2','a3','a4','a5','a6','a7','a8'],
['b1','b2','b3','b4','b5','b6','b7','b8'],
['c1','c2','c3','c4','c5','c6','c7','c8'],
['d1','d2','d3','d4','d5','d6','d7','d8'],
['e1','e2','e3','e4','e5','e6','e7','e8'],
['f1','f2','f3','f4','f5','f6','f7','f8'],
['g1','g2','g3','g4','g5','g6','g7','g8'],
['h1','h2','h3','h4','h5','h6','h7','h8']
]



#une tour est favorisée sur une colonne libre
#trop couteux
def getOpenFileBonus(board,square):
    global squares
    file = chess.square_file(square)

    obstructingPawns = 0
    for rank in range(1,7):

        piece = board.piece_at(chess.parse_square(squares[file][rank]))
        if piece != None and piece.piece_type == chess.PAWN:
            obstructingPawns += 1

    if  obstructingPawns >= 2:
        return 0
    elif obstructingPawns == 1:
        return 0.75
    elif obstructingPawns == 0:
        return 1.5



#une tour est favorisée sur une colonne centrale
def getRookSquareBonus(square,color):
    fileBonus = (1 - 0.5*(abs(3.5-chess.square_file(square))-0.5))/2
    return fileBonus



#analogue au bonus central
fileMaluses = [-0.25,-0,-0.5,-1,-1,-0.5,-0,-0.25]
def getCetralKingSquareMalus(square,color):
    global fileMaluses
    if color: #blanc
        rankMalus = -(chess.square_rank(square)/14)
    else: #noir
        rankMalus = -((7-chess.square_rank(square))/14)

    fileMalus = fileMaluses[chess.square_file(square)]
    return rankMalus + fileMalus #négatif car c'est un malus



whitePawnBonus = [0,0,1/4,2/4,3/4,1,4,0]
blackPawnBonus = [0,4,1,3/4,2/4,1/4,0,0]

def getAdvancedPawnBonus(pawnColor,square):
    global whitePawnBonus, blackPawnBonus
    rank = chess.square_rank(square)

    if pawnColor == chess.WHITE:
        return whitePawnBonus[rank]
    elif pawnColor == chess.BLACK:
        return blackPawnBonus[rank]



def basicHeuristic(board,color):

    if board.is_game_over():
        if board.outcome().winner == color:
            return 160
        elif board.outcome().winner == (not color):
            return -160
        elif board.outcome().winner == None:
            return 0

    map = board.piece_map()
    score = 0

    for key in map:
        piece = map[key]

        if piece.piece_type == chess.PAWN:
            value = 1
        elif piece.piece_type == chess.KNIGHT:
            value = 3
        elif piece.piece_type == chess.BISHOP:
            value = 3
        elif piece.piece_type == chess.ROOK:
            value = 5
        elif piece.piece_type == chess.QUEEN:
            value = 9
        elif piece.piece_type == chess.KING:
            value = 0

        if piece.color != color:
            value = -value

        score += value
    return score
