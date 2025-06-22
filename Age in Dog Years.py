# Project 8: Age in Dog Years

# This project is a fun little calculator! I wanted to make a program
# that takes a person's age and converts it into "dog years."
# The rule I'm using is super simple: 1 human year equals 7 dog years.
# It's a straightforward way to practice input, basic multiplication, and output.

# --- My Dog Year Calculation Process ---

# 1. Getting the human's age:
#    I'm asking the user for their age using `input()`.
#    Since age is usually a whole number (like 25, not 25.5 for this simple case),
#    I'm converting the input text to an integer using `int()`.
print("Welcome to my Age in Dog Years Calculator!")
human_age_str = input("Please enter your age in human years (a whole number): ")
human_age = int(human_age_str) # Converting the text to an integer

# --- The Dog Year Conversion Formula ---
# This is where the magic happens! I'm just multiplying the human age by 7.
# It's a simple bit of arithmetic.

# 2. Calculating the age in dog years:
dog_age = human_age * 7

# 3. Displaying the result:
#    I'm using an f-string again to present the result clearly and friendly.
#    It's satisfying to see the converted age right there!
print(f"If you are {human_age} human years old, then in dog years, you are {dog_age} years old!")
print("Woof woof!")

# --- What I learned (and practiced) ---
# - Taking numerical input from the user.
# - Converting input strings to integers (`int()`).
# - Performing simple multiplication (`*`).
# - Creating clear and concise output using f-strings.
# - Building a program that does a simple, fun calculation!
