import chess
from random import choice
from Heuristics import *
from MinMax import *


def userVSminmax(board,minMaxHeuristic,minMaxDepth):
    print(board)

    while not board.is_game_over():

        print("----------")
        print("User turn")

        legalMove = False
        while not legalMove:

            validInput = False
            while not validInput:

                try:
                    start = str(input())
                    end = str(input())
                    #cant promote yet
                    userMove = chess.Move(chess.parse_square(start),chess.parse_square(end))
                    validInput = True
                except ValueError:
                    print("invalid input")

            if userMove in board.generate_legal_moves():
                board.push(userMove)
                legalMove = True
            else:
                print("illegal move")

        print(board)

        if not board.is_game_over():

            print("----------")
            print("AI turn")
            minMax2Move = getBestMoveMM(board,chess.BLACK,minMaxHeuristic,minMaxDepth)
            board.push(minMax2Move)
            print(board)

    print(board.result())

    return board


def aiVSai(board,ai1,ai2,heuristic1,heuristic2,depth1,depth2):
    print(board)

    while not board.is_game_over():

        print("----------")
        print("White to move")
        ai1Move = ai1(board,chess.WHITE,heuristic1,depth1)
        board.push(ai1Move)
        print(board)

        if not board.is_game_over():

            print("----------")
            print("Black to move")
            ai2Move = ai2(board,chess.BLACK,heuristic2,depth2)
            board.push(ai2Move)
            print(board)

    print(board.result())

    return board



def aiVSrandom(board,ai,heuristic,depth):
    print(board)

    while not board.is_game_over():

        print("White to move")
        aiMove = ai(board,chess.WHITE,heuristic,depth)
        board.push(aiMove)

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
