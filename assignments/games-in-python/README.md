# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection by creating a word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Create the Hangman Game

#### Description
Write a Python program that implements the Hangman game. The game should randomly select a word from a predefined list, accept letter guesses from the player, and display the current progress. The player wins by guessing all letters before running out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the user
- Display the current progress (e.g., _ _ a _ _ _)
- Track and display the number of incorrect guesses remaining
- End the game when the word is guessed or attempts are exhausted
- Show a win message if the player succeeds, or a lose message with the correct word if not

Example:
```text
Word: apple
Guess a letter: a
Current: a _ _ _ _
Guess a letter: e
Current: a _ _ _ e
...etc...
```

### 🛠️	Enhance the Game (Optional Challenge)

#### Description
Add extra features to make your Hangman game more fun or user-friendly.

#### Requirements
Completed program could:

- Show letters already guessed
- Allow the player to choose difficulty (number of attempts)
- Use a larger or themed word list
- Add simple ASCII art for the hangman
