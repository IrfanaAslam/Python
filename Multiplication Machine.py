# Project 4: Multiplication Machine

# Alright, time to tackle multiplication! After addition and subtraction,
# it feels pretty natural to move on to multiplying numbers.
# This program will take two whole numbers from the user and then give back their product.
# It's another great chance to practice getting numerical input and doing basic math.

# --- My Multiplication Process ---

# 1. Asking for the first number:
#    Just like my previous projects, I'm using `input()` to grab text from the user.
#    And critically, I'm converting that text into a proper whole number using `int()`.
#    If I forget this step, Python gets confused when I try to multiply!
print("Welcome to my Multiplication Machine!")
num1_str = input("Please enter the first whole number: ")
num1 = int(num1_str) # Converting the text into an integer

# 2. Asking for the second number:
#    Repeating the same pattern here to get the second number and convert it.
#    Consistency helps me remember the steps!
num2_str = input("Please enter the second whole number: ")
num2 = int(num2_str) # Converting the text into an integer

# --- A quick reminder about whole vs. decimal numbers ---
# For these projects, I'm sticking to `int()` for whole numbers.
# If I needed to work with decimals (like 2.5 * 4.0), I'd use `float()` instead!

# 3. Doing the actual multiplication:
#    This is the core of the project! Python makes multiplication easy with the `*` operator.
product_result = num1 * num2

# 4. Showing off the result:
#    An f-string again for a clear and friendly output!
#    It's satisfying to see the numbers go in and the correct product come out.
print(f"The product of {num1} and {num2} is: {product_result}")

# --- What I'm solidifying (and expanding on) ---
# - My ability to get multiple numbers from user input.
# - The importance of `int()` for converting text to whole numbers for calculations.
# - How to use the multiplication operator (`*`).
# - Keeping my program's output user-friendly with f-strings.
