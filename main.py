import chess
from Heuristics import *
from TimedAI import *
from Fight import *



board = chess.Board()
aiVSai(board,ABtime,ABtime,basicHeuristic,basicHeuristic,15,15)
#userVSai(board,ABtime,basicHeuristic,10)

#dans le mode user vs ai il faut entrer la case de départ puis d'arrivée de la piece déplacée
