# Project 17: Basic Menu System

# After building a login screen, I thought it would be cool to create a simple
# text-based menu. The idea is to present the user with a few options (like adding
# numbers or subtracting them) and then let them choose what they want to do.
# This project is perfect for practicing how to display options and use
# `if`/`elif`/`else` statements to react to the user's choice.

# --- My Menu System Strategy ---

# 1. Displaying the menu options:
#    The first step is to clearly show the user what they can choose from.
#    I'm using `print()` statements for each option, giving them a number
#    so the user can easily select.
print("Welcome to my Basic Menu System!")
print("Please choose an option by entering its number:")
print("1. Add Two Numbers")
print("2. Subtract Two Numbers")
print("3. Say Hello")
print("4. Exit")

# 2. Getting the user's choice:
#    I'll use `input()` to get their choice. Since they're entering a number,
#    I'll convert it to an integer using `int()`.
choice_str = input("Enter your choice (1, 2, 3, or 4): ")
choice = int(choice_str) # Convert the text input to an integer

# --- Responding to the user's choice (`if`/`elif`/`else` power!) ---
# This is where the program makes a decision based on what the user picked.
# Each `if`/`elif` block checks for a specific choice, and the `else` catches
# anything that isn't a valid option.

if choice == 1:
    # If they chose '1', I'll ask for two numbers and print their sum.
    # Reusing logic I learned from my "Simple Adder" project!
    print("\nYou chose: Add Two Numbers")
    num1_str = input("Enter first number: ")
    num1 = int(num1_str)
    num2_str = input("Enter second number: ")
    num2 = int(num2_str)
    sum_result = num1 + num2
    print(f"The sum is: {sum_result}")
elif choice == 2:
    # If they chose '2', I'll ask for two numbers and print their difference.
    # Reusing logic from my "Basic Subtractor" project!
    print("\nYou chose: Subtract Two Numbers")
    num1_str = input("Enter first number: ")
    num1 = int(num1_str)
    num2_str = input("Enter second number: ")
    num2 = int(num2_str)
    difference_result = num1 - num2
    print(f"The difference is: {difference_result}")
elif choice == 3:
    # If they chose '3', a simple hello message.
    print("\nYou chose: Say Hello")
    print("Hello there! It's nice to see you using my menu system.")
elif choice == 4:
    # If they chose '4', they want to exit.
    print("\nYou chose: Exit")
    print("Exiting the menu. Goodbye!")
else:
    # If none of the above numbers were entered, it's an invalid choice.
    print("\nInvalid choice. Please enter a number between 1 and 4.")

# --- What I learned (making programs more interactive!) ---
# - How to design and display a basic text-based menu.
# - Using `if`/`elif`/`else` to control program flow based on user input for multiple options.
# - Reusing code concepts (like getting numbers and performing math) within different parts of a program.
# - Making programs more interactive and guided for the user.
