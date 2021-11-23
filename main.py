import chess
from Heuristics import *
from MinMax import *
from AlphaBeta import *
from TimedAI import *
from Fight import *



board = chess.Board()
#aiVSai(board,getBestMoveAB,getBestMoveAB,basicHeuristic,basicHeuristic,4,4)
userVSai(board,getBestMoveAB,basicHeuristic,2)
