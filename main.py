import chess
from Heuristics import *
from MinMax import *
from Fight import *



board = chess.Board()
board.set_piece_at(chess.parse_square("e3"),chess.Piece(chess.ROOK,chess.WHITE))
minmaxVSminmax(board,basicHeuristic,basicHeuristic,2,2)
