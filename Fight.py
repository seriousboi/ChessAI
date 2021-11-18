import chess
from random import choice
from Heuristics import *
from MinMax import *



def minmaxVSminmax(board,minMaxHeuristic1,minMaxHeuristic2,minMaxDepth1,minMaxDepth2):
    print(board)

    while not board.is_game_over():

        print("----------")
        print("White to move")
        minMax1Move = getBestMove(board,chess.WHITE,minMaxHeuristic1,minMaxDepth1)
        board.push(minMax1Move)
        print(board)

        if not board.is_game_over():

            print("----------")
            print("Black to move")
            minMax2Move = getBestMove(board,chess.BLACK,minMaxHeuristic2,minMaxDepth2)
            board.push(minMax2Move)
            print(board)
            
    print(board.result())

    return board



def minmaxVSrandom(board,minMaxHeuristic,minMaxDepth):
    print(board)

    while not board.is_game_over():

        print("White to move")
        minMaxMove = getBestMove(board,chess.WHITE,minMaxHeuristic,minMaxDepth)
        board.push(minMaxMove)

        print(board)

        if not board.is_game_over():
            print("Black to move")
            randMaxMove = getRandomMove(board)
            board.push(randMaxMove)

            print("----------")
            print(board)
    print(board.result())

    return board



def getRandomMove(board):
    return choice([move for move in board.generate_legal_moves()])
