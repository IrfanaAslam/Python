# Project 3: Basic Subtractor

# After building my simple adder, I thought, why not a subtractor too?
# This project is all about taking two numbers and finding the difference between them.
# It's a great way to reinforce what I learned about getting numbers from the user
# and performing another basic arithmetic operation.

# --- My Process for Subtraction ---

# 1. Getting the first number (the one I'll subtract from):
#    Just like before, I used `input()` to ask for the first number.
#    And, super important, I converted it to an `int()` right away,
#    because numbers entered as text can't do math!
print("Welcome to my Basic Subtractor!")
num1_str = input("Please enter the first whole number (the one you'll subtract from): ")
num1 = int(num1_str) # Converting input text to an integer

# 2. Getting the second number (the one I'll subtract):
#    Same idea here! Ask for the second number and convert it to an integer.
num2_str = input("Please enter the second whole number (the one you'll subtract): ")
num2 = int(num2_str) # Converting input text to an integer

# --- A quick thought on order ---
# I realized that with subtraction, the order matters a lot!
# 5 - 3 is different from 3 - 5. So, the prompts need to be clear!

# 3. Performing the subtraction:
#    This was the simple part, just using the `-` operator.
difference_result = num1 - num2

# 4. Displaying the result:
#    Finally, I used an f-string with `print()` again to show the calculated difference.
#    It's cool to see how easy it is to change the operation!
print(f"The difference between {num1} and {num2} is: {difference_result}")

# --- What I reinforced (and learned a little extra) ---
# - Taking multiple numerical inputs.
# - Converting input strings to integers (`int()`).
# - Using the subtraction operator (`-`).
# - Understanding that operation order matters for subtraction.
# - Continuing to make my output clear and readable with f-strings.
