from copy import copy
import random
import sys
from copy import deepcopy
import math

class maxConnect4Game:
    def __init__(self, calculation):
        self.playBoard = [[0 for _ in range(7)] for _ in range(6)]
        self.presentTurn = 0
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.gameFile = None
        self.calculation = calculation
        self.depth = 0  

    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.playBoard for piece in row if piece)

    def printPlayBoard(self):
        print ('-----------------')
        for i in range(6):
            for j in range(7):
                print('%d' % self.playBoard[i][j]),
            print ("\n")
        print ('-----------------')

    def writePlayBoardToFile(self, file, turn):
        for i in range(6):
            for j in range(7):
                file.write('%d' % self.playBoard[i][j]),
            file.write ("\n")
        file.write(str(turn))
        file.write ("\n")

    def printPlayBoardToFile(self):
        for row in self.playBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        self.gameFile.write('%s\r\n' % str(self.presentTurn))

    def playPiece(self, column):
        if not self.playBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.playBoard[i][column]:
                    self.playBoard[i][column] = self.presentTurn
                    self.pieceCount += 1
                    return 1

    def playDummyPiece(self, board, column, turn):
        if not board[0][column]:
            for i in range(5, -1, -1):
                if not board[i][column]:
                    board[i][column] = turn
                    return board
        return None

    def aiPlay(self):
        org_board = deepcopy(self.playBoard)
        new_board = deepcopy(self.playBoard)
        evalMax = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        col = None
        for j in range(7):
            new_board = self.playDummyPiece(deepcopy(org_board), j, self.presentTurn)
            if new_board:
                if self.presentTurn == 1:
                    next_turn = 2
                else:
                    next_turn = 1
                eval = self.dfs(new_board, next_turn, 1, alpha, beta)
                if eval > evalMax:
                    evalMax = eval
                    col = j 
                alpha = max(alpha, evalMax)
                if beta <= alpha:
                    break
        self.playBoard = org_board
        self.playPiece(col)
        print('\n\nmove %d: Player %d, column %d\n' % (self.pieceCount, self.presentTurn, col+1))
        if self.presentTurn == 1:
            self.presentTurn = 2
        elif self.presentTurn == 2:
            self.presentTurn = 1

    def isBoardFull(self, board):
        for j in range(7):
            if board[0][j] == 0:
                return False
        return True

    def dfs(self, new_board, turn, rec_depth, alpha, beta):
        if rec_depth >= self.depth or self.isBoardFull(new_board):
            return self.calculation.calculate(new_board, self.presentTurn)

        org_board = new_board
        if turn == self.presentTurn:
            evalMax = -float('inf')
            for j in range(7):
                new_board = self.playDummyPiece(deepcopy(org_board), j, turn)
                if new_board:
                    if turn == 1:
                        next_turn = 2
                    else:
                        next_turn = 1
                    eval = self.dfs(new_board, next_turn, rec_depth+1, alpha, beta)
                    evalMax = max(evalMax, eval)
                    alpha = max(alpha, evalMax)
                    if beta <= alpha:break
            return evalMax
        else:
            evalMin = +float('inf')
            for j in range(7):
                new_board = self.playDummyPiece(deepcopy(org_board), j, turn)
                if new_board:
                    if turn == 2:
                        next_turn = 1
                    else:
                        next_turn = 2
                    eval = self.dfs(new_board, next_turn, rec_depth+1, alpha, beta)
                    evalMin = min(evalMin, eval)
                    beta = min(beta, evalMin)
                    if beta <= alpha:break
            return evalMin