# Project 26: First/Last Character

# After counting the full length of a word, I wanted to try getting
# just specific parts of it – specifically, the very first and very last characters.
# My goal for this program is:
# 1. Ask the user for a word.
# 2. Extract its first character.
# 3. Extract its last character.
# 4. Print both.
# This project introduces me to "string indexing," which is super useful for grabbing individual characters.

# --- My First/Last Character Strategy ---

# 1. Getting the word from the user:
#    Still working with text, so `input()` is the right tool.
print("Welcome to my First/Last Character Extractor!")
user_word = input("Please enter a word (e.g., 'Python' or 'hello'): ")

# --- String Indexing: Grabbing Characters by Position! ---
# This is a key concept! In Python (and many other programming languages),
# characters in a string are numbered, starting from 0.
# So, for "hello":
# H e l l o
# 0 1 2 3 4
#
# To get a character, you put its number (its "index") in square brackets `[]` after the string variable.
# There's also a cool trick for the last character: negative indexing!
# -1 means the *last* character, -2 means the second to last, and so on.

# 2. Getting the first character:
#    The first character is always at index 0.
first_char = user_word[0]

# 3. Getting the last character:
#    The last character is always at index -1. This is simpler than calculating `len(word) - 1`!
last_char = user_word[-1]

# 4. Displaying the results:
#    An f-string helps me show the original word and its extracted characters clearly.
print(f"\nYour word was: '{user_word}'")
print(f"The first character is: '{first_char}'")
print(f"The last character is: '{last_char}'")
print("Easy peasy!")

# --- What I learned (pinpointing parts of strings!) ---
# - The fundamental concept of "string indexing" (characters have numbered positions).
# - How to access individual characters using square brackets `[]` and their index.
# - That indexing starts at 0 for the first character.
# - The convenience of negative indexing (e.g., `-1` for the last character).
# - More practice with input/output and f-strings.
# - This feels like it lays groundwork for much more complex text analysis!
