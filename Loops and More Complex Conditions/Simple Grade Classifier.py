# Project 19: Simple Grade Classifier

# For this project, I wanted to build something that could take a numeric score
# (like a test score) and tell me if it's a "Pass" or a "Fail".
# It's a straightforward way to practice using `if` and `else` statements
# to make a simple decision based on a number.

# --- My Grade Classification Strategy ---

# 1. Getting the score from the user:
#    Scores can be whole numbers (like 85) or sometimes have decimals (like 72.5),
#    so I decided to use `float()` to handle any type of numerical input.
#    `input()` gets the text, and `float()` converts it.
print("Welcome to my Simple Grade Classifier!")
score_str = input("Please enter the student's score (e.g., 75 or 88.5): ")
score = float(score_str) # Converting the text to a floating-point number

# --- The Grading Rule (`if`/`else` decision!) ---
# I'm setting a simple rule:
# If the score is 50 or higher, it's a "Pass".
# Otherwise, it's a "Fail".

# 2. Classifying the grade:
#    I'm using an `if`/`else` statement to check the condition.
if score >= 50: # Check if the score is 50 or greater
    print(f"\nA score of {score} means: PASS!")
else: # If the score is NOT 50 or greater, then it must be less than 50
    print(f"\nA score of {score} means: FAIL.")

# --- What I learned (making clear decisions!) ---
# - How to use `if` and `else` statements for binary (two-way) decisions.
# - Applying comparison operators (`>=` for "greater than or equal to").
# - More practice with `float()` for flexible numerical input.
# - Creating a program that provides clear feedback based on a condition.
# - This feels like a stepping stone to more complex grading systems later!
