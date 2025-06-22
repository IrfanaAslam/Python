# Project 16: Login Simulator

# Building on my simple password validator, I decided to create a more complete
# login simulator. This time, I'll need both a correct username AND a correct password.
# The program will ask for both, and only grant access if both are exactly right.
# This project helps me practice combining string comparisons and using logical operators
# like `and` in my `if` statements.

# --- My Login Simulation Strategy ---

# 1. Setting the correct username and password:
#    Just like before, these are hardcoded for simplicity. In a real-world app,
#    these would be securely stored and managed!
correct_username = "pythonuser"
correct_password = "secure_password_abc"

print("Welcome to my Simple Login System!")
print("Please enter your username and password to log in.")

# 2. Getting the user's username attempt:
#    I'm using `input()` to get the username. No conversion needed as it's text.
user_username_attempt = input("Enter your username: ")

# 3. Getting the user's password attempt:
#    And similarly for the password.
user_password_attempt = input("Enter your password: ")

# 4. Checking both username AND password:
#    This is the key part! I'm using the `and` logical operator.
#    The `if` condition `user_username_attempt == correct_username and user_password_attempt == correct_password`
#    will only be `True` if *both* individual comparisons are `True`.
#    If even one of them is `False`, the whole condition is `False`.
if user_username_attempt == correct_username and user_password_attempt == correct_password:
    print("\nLogin successful! Welcome to your account.")
else:
    # If the combined condition is `False`, it means either the username was wrong,
    # or the password was wrong, or both were wrong.
    print("\nLogin failed. Incorrect username or password. Please try again.")

# --- What I learned (new logical power!) ---
# - How to handle multiple pieces of user input (username and password).
# - The importance and usage of the `and` logical operator to check multiple conditions at once.
# - Combining string comparison with logical operators for more complex decision-making.
# - Building a slightly more advanced security simulation.
