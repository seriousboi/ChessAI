import chess
from Heuristics import *
from MinMax import *
from AlphaBeta import *
from Fight import *



board = chess.Board()
board.clear_board()
board.set_piece_at(chess.parse_square("c8"), chess.Piece(chess.KING,chess.BLACK))
board.set_piece_at(chess.parse_square("a1"), chess.Piece(chess.KING,chess.WHITE))
board.set_piece_at(chess.parse_square("a7"), chess.Piece(chess.ROOK,chess.WHITE))
board.set_piece_at(chess.parse_square("h2"), chess.Piece(chess.QUEEN,chess.WHITE))

#board.set_piece_at(chess.parse_square("e3"), chess.Piece(chess.ROOK,chess.WHITE))
#userVSminmax(board,basicHeuristic,2)
aiVSai(board,getBestMoveMM,getBestMoveMM,basicHeuristic,basicHeuristic,2,2)
