# Project 10: Area of a Rectangle

# For my tenth project, I decided to tackle a classic geometry problem:
# calculating the area of a rectangle. This project is a great way to
# apply what I've learned about getting numerical input and performing
# basic multiplication, similar to my earlier calculator projects,
# but in a new context.

# --- My Area Calculation Process ---

# 1. Getting the length of the rectangle:
#    Since lengths can be whole numbers or have decimals, I'm using `float()`
#    to make sure the input can handle values like 5.0 or 7.5.
#    `input()` gets the text, and `float()` converts it.
print("Welcome to my Rectangle Area Calculator!")
length_str = input("Please enter the length of the rectangle: ")
length = float(length_str) # Converting the text to a floating-point number

# 2. Getting the width of the rectangle:
#    I'm doing the same for the width, ensuring it can also handle decimals.
width_str = input("Please enter the width of the rectangle: ")
width = float(width_str) # Converting the text to a floating-point number

# --- The Area Formula ---
# This is the core formula for a rectangle's area: Area = Length × Width.
# Simple multiplication is all it takes!

# 3. Calculating the area:
area = length * width

# 4. Displaying the result:
#    Using an f-string again to present the calculated area clearly.
#    It's satisfying to see the dimensions go in and the area pop out!
print(f"A rectangle with length {length} and width {width} has an area of {area}.")
print("Geometry made easy with Python!")

# --- What I learned (and reinforced) ---
# - Continual practice with `float()` for handling decimal numerical inputs.
# - Applying basic multiplication (`*`) to solve a simple mathematical problem.
# - Reinforcing the importance of clear input prompts and informative output messages.
# - Building small, practical tools that perform specific calculations.
