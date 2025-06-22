# Project 25: Word Length Counter

# After my palindrome checker, I wanted to do something even simpler with strings
# but still useful: just counting the length of a word!
# My goal for this program is straightforward:
# 1. Ask the user for a word.
# 2. Figure out how many characters are in that word.
# 3. Print the length.
# This project is a quick win and teaches me about the `len()` function.

# --- My Word Length Counting Strategy ---

# 1. Getting the word from the user:
#    As with all my text-based projects, `input()` is the way to go.
#    No numerical conversions needed here, which keeps things simple!
print("Welcome to my Word Length Counter!")
user_word = input("Please enter a word (e.g., 'hello' or 'Python'): ")

# --- The `len()` Function: My New Best Friend for Lengths! ---
# This was the super easy part! Python has a built-in function called `len()`
# that instantly tells you how many items are in something. For a string,
# it tells you how many characters it has. It even counts spaces and symbols!

# 2. Calculating the length of the word:
word_length = len(user_word)

# 3. Displaying the result:
#    An f-string helps me clearly show the original word and its calculated length.
#    It's satisfying to see Python just know the length right away!
print(f"\nThe word '{user_word}' has {word_length} characters.")
print("Short and sweet!")

# --- What I learned (a handy new tool!) ---
# - The existence and usage of the built-in `len()` function.
# - How `len()` works with strings (counting all characters, including spaces).
# - Reinforcing basic input/output and f-string usage.
# - Discovering more of Python's handy built-in capabilities!
