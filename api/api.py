from fastapi import FastAPI
from game.tic_tac_toe import TicTacToeGame

game = TicTacToeGame()
app = FastAPI()

@app.get("/game")
def get_game():
    return {
        "board": game.board.board,
        "game_over": game.is_game_over(),
        "winner": game.get_winner(),
    }

@app.post("/move")
def move(row: int, col: int):
    game.move(row, col)
    return {
        "board": game.board.board,
        "game_over": game.is_game_over(),
        "winner": game.get_winner(),
    }

@app.post("/reset")
def reset():
    game.reset()
    return {
        "board": game.board.board,
        "game_over": game.is_game_over(),
        "winner": game.get_winner(),
    }