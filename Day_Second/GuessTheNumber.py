# the second day project i am going to create is a number guessing game made in python from scratch, well this will not be so much difficult to make, but its todays project so let's make it
# in this i am going to use the pythons very interesting library that is random.


import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'exit' to quit the game anytime.")

    # Generate a random number
    random_number = random.randint(1, 100)
    attempts = 0  # Counter for attempts

    while True:
        # Get user input
        user_input = input("Enter your guess: ").strip()

        # Exit condition
        if user_input.lower() == 'exit':
            print(
                f"The game is over. The number was {random_number}. Goodbye!")
            break

        # Validate input
        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid number or type 'exit' to quit.")
            continue

        # Increment the attempt counter
        attempts += 1

        # Check the guess
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break


# Run the game
number_guessing_game()
