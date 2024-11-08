import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Prompt user for a guess
user_guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess is correct
if user_guess == random_number:
    print("Right! You guessed it correctly.")
else:
    print(f"Wrong! The correct number was {random_number}.")
