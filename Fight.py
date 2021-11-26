from TimedAI import *
from random import choice
import chess



def userVSai(board,ai,heuristic,maxDuration):
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
            aiMove = getBestMoveTime(ai,board,chess.BLACK,heuristic,maxDuration)
            board.push(aiMove)
            print(board)

    print(board.result())
    print(board.outcome().termination)

    return board



def aiVSai(board,ai1,ai2,heuristic1,heuristic2,maxDuration1,maxDuration2):
    print(board)

    while not board.is_game_over():

        print("----------")
        print("White to move")
        ai1Move = getBestMoveTime(ai1,board,chess.WHITE,heuristic1,maxDuration1)
        board.push(ai1Move)
        print(board)

        if not board.is_game_over():

            print("----------")
            print("Black to move")
            ai2Move = getBestMoveTime(ai2,board,chess.BLACK,heuristic2,maxDuration2)
            board.push(ai2Move)
            print(board)

    print(board.result())
    print(board.outcome().termination)

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
    print(board.outcome().termination)

    return board



def getRandomMove(board):
    return choice([move for move in board.generate_legal_moves()])
