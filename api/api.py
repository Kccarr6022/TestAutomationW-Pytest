import uvicorn
from fastapi import FastAPI
from game.tic_tac_toe import TicTacToeGame
from create_api import create_api
from pydantic import BaseModel

game = TicTacToeGame()
app = create_api()

class Move(BaseModel):
    row: int
    col: int


@app.get("/game")
def get_game():
    return {
        "board": game.board.board,
        "game_over": game.is_game_over(),
        "winner": game.get_winner(),
    }

@app.post("/game/move")
def move(move: Move):
    print(move.row, move.col)
    game.move(move.row, move.col)
    return {
        "board": game.board,
        "game_over": game.is_game_over(),
        "winner": game.get_winner(),
    }

@app.post("/game/reset")
def reset():
    game.reset()
    return {
        "board": game.board,
        "game_over": game.is_game_over(),
        "winner": game.get_winner(),
    }

if __name__ == "__main__":
    uvicorn.run(app, port=5000)