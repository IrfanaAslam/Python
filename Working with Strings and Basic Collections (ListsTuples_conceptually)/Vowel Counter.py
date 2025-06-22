# Project 22: Vowel Counter

# After playing around with reversing strings, I wanted to try another cool
# text-based project: counting how many vowels are in a word or phrase!
# My goal for this program is to:
# 1. Ask the user for some text.
# 2. Go through each letter of that text, one by one.
# 3. Check if each letter is a vowel (a, e, i, o, u).
# 4. Keep a running tally of how many vowels I find.
# 5. Print the final count.
# This project really helped me understand how to "loop" through a string and
# make decisions about individual characters.

# --- My Vowel Counting Plan ---

# 1. Getting the text from the user:
#    Just like with the string reverser, `input()` is perfect for getting text.
#    No need for number conversions here!
print("Welcome to my Vowel Counter!")
user_text = input("Please enter a word or phrase: ")

# 2. Preparing for the count:
#    I need a way to keep track of the vowels I find. So, I created a variable
#    called `vowel_count` and started it at 0. This is my "accumulator" for the count!
vowel_count = 0

#    I also need to define what a vowel is. I put them all in a string and
#    made them lowercase, so I can easily check for them later, regardless
#    of whether the user types "A" or "a".
vowels = "aeiou" # My list of vowels to check against

# --- Looping Through the Text (Character by Character!) ---
# This is the core of the program! I use a `for` loop, which is perfect
# for going through each item in a sequence, and a string is a sequence of characters!

# 3. Iterating through each character:
print("\nCounting vowels...")
for char in user_text: # Python automatically gives me each character, one at a time
    # 4. Making sure the character is lowercase for checking:
    #    If the user types "Hello", the 'H' and 'o' are different cases.
    #    To make my check simple, I convert each character to lowercase before comparing.
    lower_char = char.lower()

    # 5. Checking if the character is a vowel:
    #    I use the `in` operator here. It's super handy for checking if
    #    a character exists within my `vowels` string.
    if lower_char in vowels:
        # If it *is* a vowel, I add 1 to my `vowel_count`.
        vowel_count = vowel_count + 1 # Or: vowel_count += 1
        # print(f"Found a vowel: {char}") # (Optional: for debugging, uncomment this to see it in action!)

# 6. Displaying the final count:
#    After the loop finishes checking every character, I print the total.
print(f"The text '{user_text}' has {vowel_count} vowel(s).")
print("That was fun!")

# --- What I learned (getting detailed with strings!) ---
# - How to loop directly through each character of a string using a `for` loop.
# - The importance of initializing a counter variable (`vowel_count = 0`).
# - Using the `in` operator to check for membership within a string (or a collection).
# - The `.lower()` string method for case-insensitive comparisons.
# - Combining loops and `if` statements to analyze text data.
