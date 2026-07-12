<div align="center">

# ⭕ Tic-Tac-Toe ❌

### *Classic 3×3 strategy — play a friend, or take on the computer.*

```
   X | O | X
  ---+---+---
   O | X | O
  ---+---+---
   X |   |
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-Enabled-FFD43B?style=for-the-badge)
![Modes](https://img.shields.io/badge/Modes-PvP%20%7C%20PvC-6E44FF?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-Terminal-000000?style=for-the-badge&logo=windowsterminal&logoColor=white)
![Status](https://img.shields.io/badge/Status-Practice%20Project-orange?style=for-the-badge)

</div>

---

## ✨ Overview

**Tic-Tac-Toe CLI** is a clean, colorful terminal version of the classic game, built with a fully modular Python codebase. Play head-to-head with a friend, or challenge a computer opponent — complete with row/column input, win/draw detection, and a "play again" loop that keeps the games coming.

## 🎨 Preview

```

  T I C   T A C   T O E
 -------+-------+-------
    T   |   T   |   T
 -------+-------+-------
    I   |   A   |   O
 -------+-------+-------
    C   |   C   |   E

Welcome to Tic-Tac-Toe....
You have to enter row and column (eg.,0 2) to put the symbol there.
If three of the symbols are same in a row, column, or diagonal you win.

Choose mode : (1) Player v/s Player (2) Player v/s Computer: 2

   |   |
---+---+---
   |   |
---+---+---
   |   |

It's X's turn.
Please enter a row and column (row, column) (eg.,0 2):1 1

   |   |
---+---+---
   | X |
---+---+---
   |   |

It's O's turn.
...
Congratulations! X Wins.
Do you wanna play again? y/n:
```

## 🧩 Features Explained

<div align="center">

| Feature | How it works |
|:---|:---|
| 🧑‍🤝‍🧑 **Two Game Modes** | Choose **Player vs Player** or **Player vs Computer** from the main menu — the same game loop powers both. |
| 🎯 **Row/Column Input** | Moves are entered as two numbers, e.g. `1 1`, mapping directly to `board[row][col]` — no clunky 1-9 keypad numbering. |
| 🖍️ **Live Colored Board** | The board redraws after every move using `colorama`, so the current state is always front and center. |
| 🧠 **Win Detection** | After every move, the board is checked across **all 3 rows**, **all 3 columns**, and **both diagonals** for three-in-a-row. |
| 🤝 **Draw Detection** | If all 9 cells are filled with no winner, the game ends cleanly in a tie instead of looping forever. |
| 🤖 **Computer Opponent** | In PvC mode, the computer (`O`) picks a **random valid empty cell** from the board — a lightweight "easy" AI. |
| 🚫 **Move Validation** | Out-of-range coordinates, already-taken cells, and non-numeric input are all caught and re-prompted instead of crashing the game. |
| 🔄 **Turn Switching** | Turns automatically alternate between `X` and `O` after every valid move. |
| 🖥️ **Auto Screen Clear** | The terminal clears before each redraw, so every turn feels like a fresh, uncluttered board. |
| 🔁 **Replay Loop** | After a win or draw, you're asked to play again — no need to restart the script. |

</div>

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Installation

```bash
git clone https://github.com/vineetgaira/Tic-Tac-Toe.git
cd Tic-Tac-Toe
pip install -r requirements.txt
```

### Run it

```bash
python main.py
```

## 🕹️ How to Play

1. Choose a mode: **(1)** Player vs Player or **(2)** Player vs Computer.
2. On your turn, enter your move as **row column**, e.g. `0 2` for the top-right cell.
3. The board redraws after every move, showing the latest state.
4. Get **three of your symbol in a row** — horizontally, vertically, or diagonally — to win.
5. If all 9 cells fill up with no winner, it's a **tie**.
6. Choose `y` to play another round, or `n` to exit.

### 🗺️ Board Coordinates

```
 (0,0) | (0,1) | (0,2)
-------+-------+-------
 (1,0) | (1,1) | (1,2)
-------+-------+-------
 (2,0) | (2,1) | (2,2)
```

## 🗂️ Project Structure

```
Tic-Tac-Toe/
├── main.py             # Entry point — runs the main game loop
├── board.py             # Board creation, rendering & mark placement
├── game.py               # Win-checking (rows/cols/diagonals) & draw logic
├── player.py               # Human move input & game mode selection
├── ai.py                     # Computer opponent's move logic
├── display.py                 # Welcome banner, prompts & result messages
├── utils.py                     # Screen clearing & "play again" prompt
├── constants.py                   # Board size configuration
├── requirements.txt                 # Project dependencies
├── src/                               # Reserved for future modularization
├── tests/                              # Reserved for future test coverage
└── docs/                                # Reserved for future documentation
```

## 🧠 How Win Detection Works

Every move triggers three independent checks against the current player's symbol:

```
Rows      →  any row where all 3 cells match
Columns   →  any column where all 3 cells match
Diagonals →  top-left→bottom-right OR top-right→bottom-left match
```

If any check passes, the game ends immediately with a winner. If the board fills up with no match, it's declared a draw.

## 🛠️ Built With

- 🐍 **Python** — core game & win-checking logic
- 🎨 **Colorama** — cross-platform colored terminal text
- 🎲 **random (stdlib)** — powers the computer opponent's move selection

## 📈 Roadmap

- [ ] Upgrade the AI from random moves to a **minimax** strategy (unbeatable mode)
- [ ] Add difficulty levels for the computer opponent
- [ ] Move logic into `src/` for cleaner structure
- [ ] Add unit tests under `tests/`
- [ ] Track win/loss/draw stats across a session

## ⚠️ Disclaimer

This is a **practice project** built for learning Python fundamentals — 2D lists, modular code organization, game-state checking, and building a simple AI opponent.

## 📄 License

Open source — free to use, learn from, and build upon.

---

<div align="center">

Made with 🐍 Python — *three in a row, every time.* ⭕❌

</div>
