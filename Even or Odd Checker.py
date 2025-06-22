# Project 6: Even or Odd Checker

# This project feels a bit like a fun puzzle! My goal here is to take a
# whole number from the user and figure out if it's an "even" number
# or an "odd" number. This is where I get to use a new operator: the modulo operator!

# --- My Even/Odd Detection Process ---

# 1. Getting the number from the user:
#    I'm going back to `int()` for this project, because even and odd
#    are usually concepts for whole numbers, not decimals.
#    So, `input()` to get the text, and `int()` to convert it.
print("Welcome to my Even or Odd Checker!")
number_str = input("Please enter a whole number: ")
number = int(number_str) # Converting the text into an integer

# --- The Magic of the Modulo Operator (%) ---
# This was the coolest new thing for this project!
# The modulo operator (`%`) gives you the *remainder* of a division.
# For example:
# 5 % 2 = 1 (because 5 divided by 2 is 2 with a remainder of 1)
# 4 % 2 = 0 (because 4 divided by 2 is 2 with no remainder)
# An even number always has a remainder of 0 when divided by 2.
# An odd number always has a remainder of 1 when divided by 2.

# 2. Checking if the number is even or odd:
#    I'm using an `if`/`else` statement based on the result of the modulo operation.
if number % 2 == 0:
    # If the remainder is 0, it's an even number.
    print(f"The number {number} is an EVEN number.")
else:
    # Otherwise (if the remainder is not 0, it must be 1 for whole numbers), it's odd.
    print(f"The number {number} is an ODD number.")

# --- What I learned (and found pretty neat!) ---
# - The modulo operator (`%`) and how it helps find remainders.
# - Using the modulo operator to easily check for even or odd numbers.
# - More practice with `input()`, `int()`, and `if`/`else` statements.
# - How understanding a new operator can unlock new kinds of programs!
