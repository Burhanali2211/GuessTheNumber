# Number Guessing Game

## Overview
The **Number Guessing Game** is a fun and interactive Python program where users try to guess a randomly generated number. The program provides feedback to guide the user and keeps track of their attempts. The game runs continuously until the user guesses correctly or decides to exit.

This project is part of my **"30 Python Projects in 30 Days"** challenge to enhance my Python programming skills.

---

## Features
- Randomly generates a number between 1 and 100.
- Allows multiple guesses until the correct number is found.
- Provides feedback for each guess:
  - "Too high!" if the guess is above the number.
  - "Too low!" if the guess is below the number.
- Tracks the number of attempts made.
- Handles invalid inputs gracefully.
- Lets users exit the game anytime by typing "exit".

---

## How to Run the Program
1. Make sure you have Python 3 installed on your system.
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Burhanali2211/GuessTheNumber.git

3. Navigate to the project folder:
   ```bash
   cd GuessTheNumber
4. Run the python script:
   ```bash
   python GuessTheNumber.py
##Example Usage
```bash
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Type 'exit' to quit the game anytime.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 65
Congratulations! You guessed it in 3 attempts.
