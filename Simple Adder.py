# Project 2: Simple Adder

# This program is my second project! I wanted to build something
# that could take two numbers from the user and simply add them together.
# It helped me practice getting different types of input and doing basic math.

# --- My Step-by-step Process ---

# 1. Getting the first number:
#    Just like in my first program, I used `input()` to ask the user for a number.
#    However, `input()` always gives me text (a string). For math, I need actual numbers!
#    So, I learned about `int()` (for integers) to convert the text input into a whole number.
print("Welcome to my Simple Adder!")
num1_str = input("Please enter the first whole number: ")
num1 = int(num1_str) # Converting the text to an integer

# 2. Getting the second number:
#    I repeated the process to get the second number, making sure to convert it to an integer again.
num2_str = input("Please enter the second whole number: ")
num2 = int(num2_str) # Converting the text to an integer

# --- Important Note on Data Types ---
# I discovered that if I want to work with numbers that have decimals (like 3.14),
# I should use `float()` instead of `int()`. For this simple adder, whole numbers were fine!
# Example for decimals (if I wanted to do that):
# num_decimal_str = input("Enter a decimal number: ")
# num_decimal = float(num_decimal_str)

# 3. Performing the addition:
#    This was the straightforward part! I just used the `+` operator to add my two numbers.
sum_result = num1 + num2

# 4. Displaying the result:
#    Finally, I used an f-string again with `print()` to show the user the sum.
#    It's really satisfying to see the program do the calculation and show the answer!
print(f"The sum of {num1} and {num2} is: {sum_result}")

# --- What I learned ---
# - How to take multiple inputs.
# - The crucial step of converting input text into numbers (`int()`).
# - Basic arithmetic operations (`+`).
# - Continuing to use f-strings for clear output.
