# Project 24: Palindrome Checker

# Building on my string reversal skills, I thought a fun challenge
# would be to check for "palindromes"! A palindrome is a word, phrase,
# number, or other sequence of characters which reads the same backward as forward
# (like "madam" or "racecar").
# My goal for this program is to:
# 1. Get a word or phrase from the user.
# 2. Reverse it.
# 3. Compare the original and the reversed versions to see if they match.
# This project really uses the string slicing trick I learned earlier!

# --- My Palindrome Checking Strategy ---

# 1. Getting the text from the user:
#    As always when working with text, `input()` is my friend here.
print("Welcome to my Palindrome Checker!")
original_text = input("Please enter a word or phrase (e.g., 'madam' or 'level'): ")

# --- Preparing for Comparison ---
# For a fair comparison, I need to make sure both the original and reversed
# versions are treated consistently. This means usually ignoring case and spaces/punctuation.
# For simplicity in this beginner project (no libraries!), I'll just focus on
# making everything lowercase to handle cases like "Racecar" vs "racecar".
# I'll also remove spaces if the user enters a phrase, for a slightly better check.

# 2. Cleaning the text (making it lowercase and removing spaces):
#    I'm making the input lowercase first using `.lower()`.
#    Then, I'm removing any spaces using `.replace(' ', '')`.
#    This makes the comparison much more reliable for simple palindromes.
cleaned_original_text = original_text.lower().replace(' ', '')
# print(f"(Internal: Cleaned text for comparison: '{cleaned_original_text}')") # Optional debug print

# 3. Reversing the cleaned text:
#    This is where I reuse my awesome string slicing trick: `[::-1]`!
reversed_text = cleaned_original_text[::-1]

# 4. Comparing the original (cleaned) with the reversed text:
#    Now, I just need to see if my `cleaned_original_text` is exactly the same
#    as my `reversed_text`. The `==` operator is perfect for this.
if cleaned_original_text == reversed_text:
    print(f"\n'{original_text}' IS a palindrome!")
    print("It reads the same forwards and backward (after ignoring case and spaces).")
else:
    print(f"\n'{original_text}' is NOT a palindrome.")
    print(f"Original (cleaned): '{cleaned_original_text}'")
    print(f"Reversed (cleaned): '{reversed_text}'")
    print("They don't match.")

# --- What I learned (making smarter text comparisons!) ---
# - How to combine string methods (`.lower()`, `.replace()`) to clean input for analysis.
# - Reusing the string slicing trick (`[::-1]`) for reversal.
# - Applying `if`/`else` for a clear true/false outcome in text analysis.
# - The concept of palindromes and how to programmatically check for them.
# - My text processing skills are growing!
