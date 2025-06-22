# Project 23: Consonant Counter

# Building on my Vowel Counter, I thought it would be a great idea
# to make a program that counts consonants! It's very similar, but
# with a slight twist in the logic. My goal is to:
# 1. Ask the user for some text.
# 2. Go through each character.
# 3. Determine if each character is a consonant (i.e., it's a letter, but NOT a vowel).
# 4. Keep a running tally of consonants.
# 5. Print the final count.
# This project helps me refine my conditional checks and string iteration.

# --- My Consonant Counting Plan ---

# 1. Getting the text from the user:
#    Just like before, `input()` is perfect for getting string data.
print("Welcome to my Consonant Counter!")
user_text = input("Please enter a word or phrase: ")

# 2. Preparing for the count:
#    I need a variable to accumulate the count of consonants.
consonant_count = 0

#    I also need to know what vowels are, because a consonant is basically
#    any letter that isn't a vowel. And I need a way to check if a character
#    is an actual letter, not a space, number, or symbol.
vowels = "aeiou" # My reference list of lowercase vowels
alphabet_letters = "abcdefghijklmnopqrstuvwxyz" # My reference for all lowercase letters

# --- Looping Through the Text and Checking! ---
# The `for` loop is my go-to for character-by-character checking.

# 3. Iterating through each character:
print("\nCounting consonants...")
for char in user_text:
    # 4. Making sure the character is lowercase for consistent checking:
    lower_char = char.lower()

    # 5. Checking if the character is a letter AND NOT a vowel:
    #    This is the main logic!
    #    First, I check if `lower_char` is actually one of the `alphabet_letters`.
    #    This prevents counting spaces, numbers, or symbols as consonants.
    #    Second, if it IS a letter, I then check if it's NOT in my `vowels` string.
    #    If both conditions are true, then it's a consonant!
    if lower_char in alphabet_letters and lower_char not in vowels:
        consonant_count = consonant_count + 1 # Or: consonant_count += 1
        # print(f"Found a consonant: {char}") # (Optional: for debugging, uncomment this to see it in action!)

# 6. Displaying the final count:
#    After the loop finishes, I print the total.
print(f"The text '{user_text}' has {consonant_count} consonant(s).")
print("Another character counting success!")

# --- What I learned (more precise string analysis!) ---
# - How to combine multiple conditions in an `if` statement using `and`.
# - Using the `not in` operator to check if an item is *not* present in a sequence.
# - The importance of checking if a character is an actual letter before classifying it as a consonant or vowel.
# - Reinforcing iteration (`for` loop) and counter variables.
# - My programs are getting smarter at analyzing text!
