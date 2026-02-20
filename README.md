# 🟩 Wordle Game & Solver

A Python implementation of the classic **Wordle** word-guessing game, complete with an intelligent **AI Solver** that can crack the puzzle in an average of ~4 guesses.

---

## 📁 Project Structure

```
wordle-Project/
├── WordleSolver.py                        # Pygame-based Wordle game (GUI)
├── solver.py                               # AI-powered Wordle solver
└── assests/
    ├── dictionary_5_letter.txt             # All valid 5-letter guesses
    └── targets_5_letter.txt                # Possible answer words
```

---

## 🎮 Wordle Game (`WordleGame.py`)

A fully functional Wordle clone built with **Pygame**, featuring a clean UI and color-coded feedback.

### Features

- 🟩 **Green** → Correct letter, correct position
- 🟨 **Yellow** → Correct letter, wrong position
- ⬜ **Grey** → Letter not in the word
- 6 attempts to guess the hidden 5-letter word
- Displays the correct answer if you run out of guesses
- Press **Space** to instantly start a new game
- Press **Escape** to quit

### How to Play

```bash
pip install pygame
python game.py
```

**Controls:**

| Key         | Action                              |
| ----------- | ----------------------------------- |
| `A-Z`       | Type a letter                       |
| `Backspace` | Delete last letter                  |
| `Enter`     | Submit guess (must be a valid word) |
| `Space`     | New game                            |
| `Escape`    | Quit                                |

---

## 🤖 Wordle Solver (`WordleSolver.py`)

An intelligent solver that uses **letter frequency analysis** and **positional scoring** to eliminate candidates and find the answer efficiently.

### How It Works

1. **Letter Frequency** — Scores candidate words based on how common their letters are across the remaining answer space, prioritizing words that reveal the most information.
2. **Positional Scoring** — As a tiebreaker, favors words where each letter appears frequently _in that specific position_.
3. **Smart Filtering** — After each guess, filters the answer space using the color-coded result, correctly handling duplicate letters.

### Running the Solver

**Interactive mode** (you enter the result manually):

```bash
python solver.py
```

After each suggested guess, enter the result as a 5-character string:

- `g` → Green (correct position)
- `y` → Yellow (wrong position)
- `x` → Grey (not in word)

**Example:**

```
2315 words remaining in dict.
Current guess: raise
Guess result: xgxyx
847 words remaining in dict.
Current guess: ...
```

**AI Benchmark mode** — To test the solver against the full answer list, set `ai = True` in `solver.py`:

```python
ai = True  # Run solver against all words automatically
```

### Performance

| Metric          | Result      |
| --------------- | ----------- |
| Average guesses | ~4          |
| Worst case      | ≤ 6 guesses |

---

## ⚙️ Requirements

```
python >= 3.8
pygame
```

Install dependencies:

```bash
pip install pygame
```

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/your-username/wordle.git
cd wordle-Project

# Install dependencies
pip install pygame

# Play the game
python WordleGame.py

# Or run the solver
python WordleSolver.py
```

---

## 👤 Author

Made with ❤️ by **Mohamed Saber**
