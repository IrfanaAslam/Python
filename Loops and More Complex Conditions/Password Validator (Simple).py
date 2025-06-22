# Project 15: Password Validator (Simple)

# This project is my first attempt at a security-related program!
# The idea is to have a super simple password validator.
# I'll hardcode a "correct" password, ask the user to enter *their* password,
# and then tell them if it's correct or not.
# This project is great for practicing string comparison and `if`/`else` statements.

# --- My Simple Password Validation Strategy ---

# 1. Setting the secret password:
#    Just like the secret number in my last game, this password is hardcoded for now.
#    In a real application, this would be handled very differently for security!
correct_password = "mysecretpassword123" # This is the password the user needs to guess!

print("Welcome to my Simple Password Validator!")
print("Please try to enter the correct password.")

# 2. Getting the user's password attempt:
#    I'm using `input()` to get what the user types. Since passwords are text,
#    I don't need to convert this to an `int()` or `float()`.
user_attempt = input("Enter the password: ")

# 3. Comparing the attempt to the correct password:
#    This is where the validation happens! I use the `==` operator to check
#    if the `user_attempt` string is exactly the same as the `correct_password` string.
#    It's case-sensitive, so "Password123" is different from "password123"!
if user_attempt == correct_password:
    print("Access granted! Welcome to the system.")
else:
    print("Access denied! Incorrect password. Please try again.")

# --- What I learned ---
# - How to compare strings using the `==` operator.
# - Using `if`/`else` statements to create simple decision-making logic.
# - The concept of a hardcoded value for quick testing (and why it's not secure for real apps!).
# - Building a program that simulates a basic security check.
