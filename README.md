<div align="center">

```
| |                                           
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
```

### A colorful, ASCII-animated Hangman game for your terminal 🎮

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-0.4.6-FFD43B?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-2.34.2-000000?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📖 About

**Hangman** is a classic word-guessing game reimagined for the command line, complete with a colorized interface, a 7-stage animated ASCII gallows, and words pulled live from a random-word API (with a 300+ word local fallback for when you're offline). It's a practice project built to work through clean function decomposition, game-loop design, and separating game logic from display logic across multiple files.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **Colorized UI** | Every prompt, word, and message is styled with `colorama` |
| 🖼️ **Animated Gallows** | 7 hand-drawn ASCII art stages (`stage_6` → `stage_0`) track your remaining lives |
| 🌐 **Live Word Fetching** | Pulls a random word from the [Random Word API](https://random-word-api.herokuapp.com/word) each round |
| 📚 **Offline Fallback** | Falls back to a built-in list of 300+ words if the API call fails or times out |
| 🔁 **Replay Loop** | Play as many rounds as you like without restarting the script |
| ✅ **Input Validation** | Rejects empty input, multi-character input, and repeated guesses with clear feedback |
| 🧹 **Clean Screen Refresh** | Clears the terminal between turns so the board never feels cluttered |

---

## 📂 Project Structure

```
Hangman/
├── main.py          # Entry point — runs the main game loop
├── game.py          # Core game logic: state, guesses, win/lose checks
├── display.py       # All terminal output: word progress, hangman, results
├── words.py         # Word source: API fetch + local fallback word bank
├── constants.py      # Game constants (e.g. MAX_LIVES)
├── ascii_art.py      # The 7 ASCII-art gallows stages
├── requirements.txt   # Project dependencies
├── data/             # Reserved for future use
├── docs/              # Reserved for future use
├── src/                # Reserved for future use
└── tests/              # Reserved for future use
```

---

## 🖥️ Terminal Preview

```
$ python main.py

     _                                             
| |                                           
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

_ _ _ _ _ _ _

Guess a letter : p

p _ _ p _ _ _

Guess a letter : z
You have already guessed the letter z
```

---

## 🧩 How It Works

```
┌──────────────┐     ┌────────────────┐     ┌───────────────┐
│  start_game   │ --> │  get_guess      │ --> │  update_game   │
│  picks a word │     │  reads & vali-  │     │  applies the   │
│  resets lives │     │  dates input    │     │  guess, loses  │
└──────────────┘     └────────────────┘     │  a life on miss │
                                              └───────┬────────┘
                                                       │
                                     ┌─────────────────┴─────────────────┐
                                     │                                   │
                              ┌──────▼──────┐                    ┌───────▼──────┐
                              │  check_win   │                    │  check_lose   │
                              │  all letters │                    │  lives <= 0   │
                              │  guessed?    │                    │               │
                              └──────┬──────┘                    └───────┬──────┘
                                     │                                   │
                                     └────────────┬──────────────────────┘
                                                  │
                                          ┌───────▼────────┐
                                          │  show_result    │
                                          │  play_again()   │
                                          └────────────────┘
```

---

## 🔧 Function Breakdown

### `main.py`
- **`main()`** — Orchestrates the whole game: clears the screen, shows the welcome banner, and loops through rounds until the player chooses not to continue.

### `game.py`
- **`start_game()`** — Picks a new secret word and resets `guessed_letters` and `lives`.
- **`get_guess(guessed_letters)`** — Reads a single-letter guess and returns a status of `"ok"`, `"invalid"`, or `"repeat"`.
- **`update_game(secret_word, guess, guessed_letters, lives)`** — Records the guess and deducts a life on a miss.
- **`check_win(secret_word, guessed_letters)`** — True once every letter in the word has been guessed.
- **`check_lose(lives)`** — True once lives hit zero.
- **`play_again()`** — Asks the player whether to start another round.

### `display.py`
- **`clear_screen()`** — Clears the terminal using ANSI escape codes.
- **`welcome()`** — Prints the ASCII-art title banner.
- **`show_word(secret_word, guessed_letters)`** — Renders the word with unguessed letters masked as `_`.
- **`show_wrong_letters(guessed_letters, secret_word)`** — Lists the incorrect guesses so far.
- **`show_hangman(lives)`** — Prints the ASCII gallows stage matching the current lives.
- **`show_result(won, secret_word)`** — Prints the win/lose message and reveals the word.

### `words.py`
- **`get_word_from_api()`** — Fetches a random word from the Random Word API, returning `None` on failure.
- **`get_random_word()`** — Tries the API first, falling back to a local 300+ word list if it's unavailable.

### `ascii_art.py`
- **`HANGMAN_STAGES`** — A list of 7 ASCII-art strings (`stage_0` to `stage_6`), indexed directly by the player's remaining lives.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+

### Installation
```bash
git clone https://github.com/vineetgaira/Hangman.git
cd Hangman
pip install -r requirements.txt
```

### Run the game
```bash
python main.py
```

---

## 🎯 Learning Goals

- [x] Structuring a project across multiple files by responsibility (game logic vs. display vs. data)
- [x] Managing mutable game state (`guessed_letters`, `lives`) across a loop
- [x] Handling and validating user input robustly
- [x] Working with an external API and building a graceful offline fallback
- [x] Using `colorama` for cross-platform terminal color styling
- [x] Building multi-line ASCII art driven by game state (list indexing by `lives`)

---

## ⚠️ Disclaimer

This is a **practice project** built for learning Python fundamentals — functions, state management, terminal I/O, and basic API integration. It isn't intended for production use.

---

<div align="center">

Made while learning Python 🐍

</div>
