from fastapi import FastAPI
from typing import List

class TicTacToeGame:
    board: List[List[str]]
    player: str

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = 'X'

    def __str__(self):
        board = ""
        for row in self.board:
            board += "|" + "|".join(row) + "|\n"
        return board


    def move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid move')
            return False
        if self.board[row][col] != ' ':
            return False
        self.board[row][col] = self.player
        self.player = 'O' if self.player == 'X' else 'X'
        return True

    def is_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        if self.is_full():
            return False
        return False

    def is_full(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False
        return True

    def is_game_over(self):
        return self.is_full() or self.is_winner('X') or self.is_winner('O')

    def get_winner(self):
        if self.is_winner('X'):
            return 'X'
        if self.is_winner('O'):
            return 'O'
        return None

    def get_empty_squares(self):
        squares = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    squares.append((i, j))
        return squares

    def play(self):
        while not self.is_game_over():
            print(self.board)
            if self.player == 'X':
                row = int(input('Enter row: '))
                col = int(input('Enter col: '))
                self.move(row, col)
            else:
                move = self.ai.move(self.board)
                self.move(move[0], move[1])
        self.print_winner()

    def print_winner(self):
        winner = self.board.get_winner()
        print(self.board)
        if winner is None:
            print('Tie')
        else:
            print(winner, 'wins')
    
    def reset(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = 'X'

class TicTacToeAI:
    def minimax(self, board, player):
        if board.is_game_over():
            if board.is_winner('X'):
                return 1
            elif board.is_winner('O'):
                return -1
            else:
                return 0
        best_score = -float('inf') if player == 'X' else float('inf')
        for move in board.get_empty_squares():
            board.move(move[0], move[1])
            score = self.minimax(board, 'O' if player == 'X' else 'X')
            board.move(move[0], move[1])
            if player == 'X':
                best_score = max(score, best_score)
            else:
                best_score = min(score, best_score)
        return best_score