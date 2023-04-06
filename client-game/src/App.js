import React, { useState, useEffect } from "react"
import axios from "axios"
import "./App.css"

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
  }, [])

  const getGame = async () => {
    axios.get("http://localhost:5000/game").then(res => {
      setGame(res.data)
    })
  }

  return (
    <div className="App">
      <h1>Tic Tac Toe</h1>
      <div className="board">
        {game.board.map((row, i) => {
          return (
            <div className="row" key={i}>
              {row.map((cell, j) => {
                return (
                  <div className="cell" key={j}>
                    {cell}
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
