import React, { useState, useEffect } from "react"
import axios from "axios"

const App = () => {
    const [game, setGame] = useState({
        board: [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ],
        gameOver: false,
        winner: null,
    })

    useEffect(() => {
        getGame()

        setInterval(getGame, 500)

        return () => {
            // cleanup
            reset()
        }
    }, [])

    const getGame = async () => {
        axios.get("http://localhost:5000/game").then(
            res => {
                setGame({
                    gameOver: res.data.game_over,
                    winner: res.data.winner,
                    board: res.data.board,
                })
            },
            {
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                },
            }
        )
    }

    const move = async (row, col) => {
        axios.post("http://localhost:5000/game/move", { row, col }).then(
            res => {
                setGame({
                    gameOver: res.data.game_over,
                    winner: res.data.winner,
                    board: res.data.board,
                })
            },
            {
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                },
            }
        )
    }

    const reset = async () => {
        axios.post("http://localhost:5000/game/reset").then(res => {
            setGame({
                gameOver: res.data.game_over,
                winner: res.data.winner,
                board: res.data.board,
            })
        })
    }

    return (
        <div className="relative w-screen h-screen bg-red-900">
            <h1 className="text-center text-4xl font-bold">
                Tic Tac Toe <br /> Online
            </h1>
            {game.gameOver && (
                <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white w-1/3 h-1/3">
                    <div className="h-1/2 w-1/2 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                        <h1 id="winner" className="text-center text-4xl font-bold text-green-400">
                            {game.winner === null ? "Draw" : game.winner + " Wins!"}
                        </h1>
                        <button
                            id="reset"
                            className="bg-green-300 text-gray-50 px-4 py-2 rounded-md mt-4 w-1/2 mx-auto block"
                            onClick={() => {
                                reset()
                            }}
                        >
                            Play Again
                        </button>
                    </div>
                </div>
            )}
            <div className="w-1/2 h-1/2 bg-slate-950 grid grid-cols-3 mx-auto mt-12 overflow-hidden">
                {game.board.map((row, row_index) => {
                    return (
                        <div className="row-span-1 border-gray-700 grid overflow-hidden" key={row_index}>
                            {row.map((cell, cell_index) => {
                                return (
                                    <div
                                        className="col-span-1 text-gray-50 grid-rows-1 flex items-center justify-center border-4 border-lime-50 overflow-hidden"
                                        id={row_index.toString() + "-" + cell_index.toString()}
                                        key={cell_index}
                                        onClick={() => {
                                            if (cell === " " && !game.gameOver) {
                                                move(row_index, cell_index)
                                            }
                                        }}
                                    >
                                        {cell === " " ? "-" : cell}
                                    </div>
                                )
                            })}
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

export default App
