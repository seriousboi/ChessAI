import chess



def basicHeuristic(board,color):

    if board.is_checkmate():
        if board.outcome().winner == color:
            return 160
        else:
            return -160
    if board.is_stalemate():
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