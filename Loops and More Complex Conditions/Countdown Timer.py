# Project 11: Countdown Timer

# For this project, I wanted to create a simple countdown timer.
# The idea is that the user tells me a number, and then my program
# counts down from that number all the way to zero, printing each step.
# This project is my first dive into using loops, specifically the `while` loop!

# --- My Countdown Process ---

# 1. Getting the starting number for the countdown:
#    I need a whole number to count down from, so `int()` is perfect here.
#    I'll ask the user to input the number, and then convert it.
print("Welcome to my Countdown Timer!")
start_number_str = input("Please enter a whole number to start the countdown from: ")
current_number = int(start_number_str) # Converting the text to an integer

# --- The Magic of the `while` loop! ---
# This is the exciting part! A `while` loop keeps running *as long as* a condition is true.
# In my case, I want the loop to continue as long as `current_number` is greater than or equal to 0.

# 2. Starting the countdown loop:
while current_number >= 0:
    # Inside the loop, first I print the current number.
    print(current_number)

    # Then, I reduce the number by 1. This is crucial!
    # If I don't reduce the number, the condition `current_number >= 0` would always be true,
    # and the loop would run forever (an "infinite loop"!).
    current_number = current_number - 1 # Or I could use the shorthand: current_number -= 1

# 3. Message after the countdown:
#    Once `current_number` becomes less than 0 (e.g., -1), the `while` loop's condition
#    `current_number >= 0` becomes false, and the loop stops.
#    Then, the program moves on to print this final message.
print("Countdown finished! Blast off!")

# --- What I learned (a big step!) ---
# - How to use a `while` loop to repeat actions based on a condition.
# - The importance of changing the loop's condition inside the loop itself
#   to prevent infinite loops (decrementing the counter).
# - More practice with `input()`, `int()`, and `print()`.
# - Understanding sequential execution of code (what runs after the loop finishes).
