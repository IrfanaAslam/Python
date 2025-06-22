# Project 18: Number Doubler Loop

# This project is a cool way to keep a program running for as long as the user wants!
# My goal is to repeatedly ask the user for a number, double it, and print the result.
# The program should only stop when the user types a specific word, like 'exit'.
# This really helps me practice `while` loops again, along with handling different
# types of input (numbers and a special 'exit' command).

# --- My Doubler Loop Strategy ---

# 1. Starting the loop (and setting up for the first input):
#    I need the loop to run at least once to ask for the first number.
#    So, I'm using a `while True:` loop, which means it will run forever
#    unless I explicitly tell it to `break` out. This is a common pattern!
print("Welcome to my Number Doubler Loop!")
print("I'll double any whole number you give me. Type 'exit' to quit.")

while True: # This loop will keep running indefinitely until I tell it to stop
    # 2. Getting input from the user:
    #    I ask the user to enter a number or 'exit'.
    user_input_str = input("Enter a whole number (or 'exit' to quit): ")

    # 3. Checking for the 'exit' command:
    #    This is the crucial part for stopping the loop!
    #    If the user types 'exit' (I'm making it case-insensitive with `.lower()`),
    #    I'll print a goodbye message and use `break` to jump out of the loop.
    if user_input_str.lower() == 'exit': # .lower() converts "Exit", "EXIT", "eXit" to "exit"
        print("Thanks for using the Doubler! Goodbye!")
        break # This command immediately stops the 'while True' loop

    # --- If it's not 'exit', then it must be a number! ---
    # 4. Converting the input to a number:
    #    If the user didn't type 'exit', I assume they typed a number.
    #    So, I convert it to an integer using `int()`.
    #    (I'm assuming valid number input for simplicity here, but later I might
    #    learn to handle cases where they type something else!)
    try: # I learned a trick to handle potential errors if they don't enter a number!
        number_to_double = int(user_input_str)
        # 5. Doubling the number:
        doubled_number = number_to_double * 2

        # 6. Printing the result:
        print(f"Your number doubled is: {doubled_number}")
    except ValueError:
        # If int() can't convert the input (e.g., if they typed "hello"), this runs.
        print("That's not a valid whole number. Please try again or type 'exit'.")


# --- What I learned (taking control of loops!) ---
# - How to create an "infinite" loop using `while True`.
# - The powerful `break` statement to exit a loop conditionally.
# - Handling different types of user input (numbers vs. command strings).
# - A little peek into error handling with `try-except` (even if it's just basic for now!).
# - Making my programs run interactively for as long as the user desires.
