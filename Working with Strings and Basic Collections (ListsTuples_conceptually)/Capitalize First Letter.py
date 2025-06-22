# Project 27: Capitalize First Letter

# After extracting the first and last characters, I wanted to try
# modifying a string by changing its capitalization.
# My goal for this project is to:
# 1. Ask the user for a word.
# 2. Convert that word so only its first letter is capitalized (and the rest are lowercase).
# 3. Print the modified word.
# This project introduces me to a handy string method called `.capitalize()`.

# --- My Capitalization Strategy ---

# 1. Getting the word from the user:
#    Still working with text, so `input()` is the way to get it.
print("Welcome to my First Letter Capitalizer!")
user_word = input("Please enter a word (e.g., 'hello' or 'PYTHON'): ")

# --- The `.capitalize()` Method: So Easy! ---
# I discovered that Python strings have built-in functions called "methods"
# that can do specific actions on them. The `.capitalize()` method is perfect
# for this task: it takes the string, makes its first letter uppercase,
# and makes all other letters lowercase. It handles words like "pYtHoN" beautifully!

# 2. Capitalizing the first letter:
capitalized_word = user_word.capitalize()

# 3. Displaying the original and capitalized words:
#    Using an f-string to show both versions helps illustrate what the program does.
print(f"\nYour original word was: '{user_word}'")
print(f"With the first letter capitalized: '{capitalized_word}'")
print("Simple but effective!")

# --- What I learned (more string power!) ---
# - The concept of string "methods" (functions that belong to strings).
# - How to use the `.capitalize()` method to easily format a word.
# - The `.capitalize()` method also makes the *rest* of the string lowercase, which is useful!
# - Continued practice with input/output and f-strings.
# - It's cool to see how much Python can do with strings right out of the box!
