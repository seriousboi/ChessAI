from Heuristics import *
from AlphaBetaTimed import *
from TimedAI import *
import chess



AItime = 3



def giveAImove():
    global AItime
    FEN, color = getInput()
    board = chess.Board(FEN)
    move = getBestMoveTime(ABtimed,board,color,betterHeuristic,AItime)
    giveOuput(move)



def getInput():
    file = open("../ChessAI/gameData/input.txt","r")
    lines = file.readlines()
    file.close()
    if lines[3].strip() == "1":
        color = chess.BLACK
    if lines[3].strip() == "0":
        color = chess.WHITE
    return lines[1],color



def giveOuput(move):
    lines = ["New\n",
    chess.SQUARE_NAMES[move.from_square]+"\n",
    chess.SQUARE_NAMES[move.to_square]+"\n"]
    file= open("../ChessAI/gameData/output.txt","w")
    file.writelines(lines)
    file.close()



giveAImove()
