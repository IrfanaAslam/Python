# Project 12: Count Up

# After making my countdown timer, I thought, why not a count-up counter too?
# This project is the reverse! The user will tell me a number, and then
# my program will count *up* from 1 all the way to that number.
# This is my first time really using a `for` loop with the `range()` function,
# which feels pretty powerful for counting.

# --- My Count Up Process ---

# 1. Getting the upper limit for counting:
#    I need a whole number that my program will count up to.
#    So, `input()` to get the text, and `int()` to convert it.
print("Welcome to my Count Up Program!")
end_number_str = input("Please enter a whole number to count up to: ")
end_number = int(end_number_str) # Converting the text to an integer

# --- The Power of the `for` loop and `range()`! ---
# This is what's different from the `while` loop!
# A `for` loop with `range()` is perfect when I know exactly how many times
# I want to repeat something, or when I want to iterate through a sequence of numbers.

# `range(start, stop)` generates numbers starting from `start` (inclusive)
# up to `stop` (exclusive). So, to count from 1 up to and including `end_number`,
# I need to set `range(1, end_number + 1)`.

# 2. Starting the count-up loop:
for current_number in range(1, end_number + 1):
    # Inside the loop, I just print the `current_number` as it goes through the range.
    print(current_number)

# 3. Message after the count-up:
#    Once the `for` loop has gone through all the numbers in the `range()`, it finishes.
#    Then, my program moves on to print this final message.
print("Count up complete! We reached the target!")

# --- What I learned (a big new tool!) ---
# - How to use a `for` loop for iterating through a sequence.
# - The `range()` function and how to use it to generate sequences of numbers.
# - The difference between `for` and `while` loops (when to use each!).
# - More practice with `input()`, `int()`, and `print()`.
# - Building another fundamental counting program.
