import chess
from Heuristics import *
from AlphaBetaTimed import *
from Fight import *



board = chess.Board()
aiVSai(board,ABtimed,ABtimed,betterHeuristic,basicHeuristic,5,5)
#userVSai(board,ABtimed,betterHeuristic,10)

#dans le mode user vs ai il faut entrer la case de départ puis d'arrivée de la piece déplacée
