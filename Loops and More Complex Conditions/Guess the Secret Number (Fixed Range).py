# Project 14: Guess the Secret Number (Fixed Range)

# This is my first proper guessing game! The idea is simple:
# I've thought of a secret number (hardcoded for now, no random numbers yet!).
# The user's job is to guess what that number is.
# My program will then tell them if their guess is too high, too low, or just right!
# This project is a great way to use loops (`while` again!) and `if`/`elif`/`else`
# for game logic.

# --- My Guessing Game Strategy ---

# 1. Setting the secret number:
#    For now, I'm just picking a number and putting it directly in the code.
#    Later, I might learn how to make Python pick a random one!
secret_number = 7 # This is the number the user needs to guess!

# 2. Initializing the guess variable:
#    I need a variable to store the user's guess. I'll give it a starting value
#    that is different from the secret number so my `while` loop starts correctly.
#    I'm choosing 0 here, as it's unlikely to be the secret number often.
guess = 0 # Initialize with a value that is not the secret number

print("Welcome to my 'Guess the Secret Number' game!")
print("I'm thinking of a whole number between 1 and 10. Can you guess it?")

# --- The Guessing Loop (`while` loop power!) ---
# I'm using a `while` loop here because I don't know how many guesses
# it will take the user to get it right. The loop should keep going
# *as long as* their guess is not equal to the `secret_number`.

# 3. Starting the guessing loop:
while guess != secret_number:
    # Inside the loop, I first ask for the user's guess.
    # It's important to convert it to an integer using `int()`.
    guess_str = input("Enter your guess: ")
    guess = int(guess_str) # Convert the text input to an integer

    # 4. Giving hints based on the guess:
    #    Now, I use `if`/`elif`/`else` to compare their guess to the `secret_number`
    #    and give them feedback.

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        # This 'else' block only runs if `guess == secret_number` is True.
        # This means the loop condition `guess != secret_number` became False,
        # so the loop will stop after this print statement.
        print(f"Congratulations! You guessed it! The secret number was {secret_number}.")

# --- What I learned (game-changing stuff!) ---
# - How to set up a basic guessing game structure.
# - Using a `while` loop to continue an action until a specific condition is met.
# - Applying `if`/`elif`/`else` statements for game logic and feedback.
# - The concept of a "hardcoded" value for simplicity (for now!).
# - Making my programs more interactive and fun!
