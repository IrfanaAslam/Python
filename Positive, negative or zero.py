# Project 7: Positive, Negative, or Zero

# Building on my experience with the Even/Odd checker, I wanted to try
# classifying numbers in a different way: are they positive, negative, or zero?
# This project felt like a good way to practice using `if`, `elif` (else if),
# and `else` statements to handle different conditions.

# --- My Number Classification Process ---

# 1. Getting the number from the user:
#    Since numbers can be positive, negative, or zero, and can also be decimals
#    (like -5.5 or +2.1), I decided to use `float()` this time.
#    It's good practice to pick the right data type for the job!
print("Welcome to my Positive, Negative, or Zero Checker!")
number_str = input("Please enter any number (it can be whole or a decimal): ")
number = float(number_str) # Converting the text into a floating-point number

# 2. Checking the number's sign:
#    This is where the `if`/`elif`/`else` structure really shines!
#    I'm checking conditions in a specific order:

#    First, check if it's greater than zero (positive).
if number > 0:
    print(f"The number {number} is a POSITIVE number.")
#    If the first condition isn't true, then check if it's less than zero (negative).
#    `elif` is short for "else if" – it only gets checked if the `if` was false.
elif number < 0:
    print(f"The number {number} is a NEGATIVE number.")
#    If it's *not* greater than zero AND it's *not* less than zero,
#    then the only option left is that it must be zero!
else:
    print(f"The number {number} is ZERO.")

# --- What I learned (and practiced a lot!) ---
# - When to use `float()` for input if I expect decimal numbers.
# - The power of `if`, `elif`, and `else` for handling multiple possible outcomes.
# - How to structure conditional checks so they flow logically.
# - Reinforcing my input/output skills and using f-strings.
