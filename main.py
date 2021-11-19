import chess
from Heuristics import *
from MinMax import *
from AlphaBeta import *
from Fight import *



board = chess.Board()
board.set_piece_at(chess.parse_square("e3"), chess.Piece(chess.ROOK,chess.WHITE))
#userVSminmax(board,basicHeuristic,2)
aiVSai(board,getBestMoveAB,getBestMoveAB,basicHeuristic,basicHeuristic,3,3)
