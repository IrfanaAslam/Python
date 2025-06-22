# Project 5: Division Calculator

# I'm moving on to division now! This one felt a bit trickier because
# you can't divide by zero, and the results can often be decimals.
# My goal for this program is to take two numbers, divide the first by the second,
# and then print the result. I also want to make sure I handle that tricky "divide by zero" situation.

# --- My Division Process ---

# 1. Getting the first number (the dividend):
#    Using `input()` as usual. For division, I thought it was important to
#    use `float()` instead of `int()` right away. This way, if someone enters a
#    whole number like '5', it's treated as '5.0', which helps if the answer
#    is going to be a decimal (like 5 / 2 = 2.5).
print("Welcome to my Division Calculator!")
num1_str = input("Please enter the first number (the dividend): ")
num1 = float(num1_str) # Converting to a float to handle decimals

# 2. Getting the second number (the divisor):
#    Same idea here, converting to a float. This number is super important
#    because it can't be zero!
num2_str = input("Please enter the second number (the divisor): ")
num2 = float(num2_str) # Converting to a float

# --- Handling the "Divide by Zero" problem! ---
# This was a new challenge. I learned that if you try to divide any number by zero,
# Python throws an error! So, I added an `if` statement to check if the second number
# is zero *before* trying to do the division. If it is, I print an error message instead.

if num2 == 0:
    print("Error: Cannot divide by zero! Please try again with a different second number.")
else:
    # 3. Performing the actual division:
    #    If the second number isn't zero, then it's safe to do the division
    #    using the `/` operator.
    division_result = num1 / num2

    # 4. Showing the result:
    #    An f-string again for a nice, clear output. It's cool how Python handles
    #    the decimal part automatically when using floats for division!
    print(f"The result of {num1} divided by {num2} is: {division_result}")

# --- What I learned (new and reinforced) ---
# - When to use `float()` instead of `int()` for numerical input (especially for division).
# - How to handle potential errors (like division by zero) using `if`/`else` statements.
# - Using the division operator (`/`).
# - The importance of thinking about edge cases in my programs.
# - Still loving f-strings for output!
