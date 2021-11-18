import chess
from Heuristics import *
from MinMax import *
from Fight import *



board = chess.Board()
userVSminmax(board,basicHeuristic,2)
