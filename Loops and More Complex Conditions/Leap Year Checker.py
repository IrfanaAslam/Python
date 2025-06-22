# Project 20: Leap Year Checker

# This project was a fun challenge because it involved a slightly more complex
# set of rules than my previous `if`/`else` statements. My goal was to create
# a program that takes a year from the user and then determines if that year
# is a "leap year" or not.

# --- The Rules for a Leap Year (It's a bit tricky!) ---
# I learned there are a few rules for leap years:
# 1. A year MUST be divisible by 4.
# 2. BUT, if it's divisible by 100, it is NOT a leap year...
# 3. UNLESS it's also divisible by 400.
# So, essentially:
# - Years like 2004, 2024 are leap years (divisible by 4).
# - Years like 1900, 2100 are NOT leap years (divisible by 100, but not 400).
# - Years like 2000, 2400 ARE leap years (divisible by 400).

# --- My Leap Year Detection Strategy ---

# 1. Getting the year from the user:
#    Years are whole numbers, so `int()` is the perfect choice for converting
#    the user's input.
print("Welcome to my Leap Year Checker!")
year_str = input("Please enter a year (e.g., 2024 or 1900): ")
year = int(year_str) # Converting the text to an integer

# 2. Applying the leap year rules using nested `if`/`elif`/`else`:
#    This part required careful thought to get the order of checks right.

if (year % 4 == 0): # Rule 1: Check if divisible by 4
    if (year % 100 == 0): # Rule 2: If divisible by 4 AND 100...
        if (year % 400 == 0): # Rule 3: ...then check if also divisible by 400
            print(f"The year {year} IS a leap year! (It's divisible by 400)")
        else:
            print(f"The year {year} is NOT a leap year. (It's divisible by 100 but not 400)")
    else:
        print(f"The year {year} IS a leap year! (It's divisible by 4 but not 100)")
else: # If not divisible by 4, it's definitely not a leap year
    print(f"The year {year} is NOT a leap year. (It's not divisible by 4)")

# --- What I learned (making complex decisions!) ---
# - How to handle more intricate conditional logic with nested `if` statements.
# - The importance of checking conditions in the correct order for rules-based programs.
# - Applying the modulo operator (`%`) multiple times to check for divisibility.
# - It felt really satisfying to get all the rules for leap years working correctly!
