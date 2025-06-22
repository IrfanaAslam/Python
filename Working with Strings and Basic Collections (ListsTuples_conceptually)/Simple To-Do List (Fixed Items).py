# Project 30: Simple To-Do List (Fixed Items)

# After my basic shopping list, I wanted to try creating a super simple
# "To-Do List." For this beginner version, I'm not actually storing a list
# that changes. Instead, I'll have a few fixed tasks, and the user can
# "mark" one of them as done by choosing its number.
# My goal is to:
# 1. Display a short list of pre-defined tasks.
# 2. Ask the user which task they want to mark as complete.
# 3. Print the tasks again, showing the chosen task as "(DONE)".
# This project helps me practice using `if`/`elif`/`else` with numerical choices
# to modify how information is displayed.

# --- My Simple To-Do List Idea ---

print("Welcome to my Simple To-Do List!")
print("Here are your tasks for today:")

# 1. Defining the fixed tasks:
#    I'm just using simple string variables for each task.
task1 = "1. Finish Python Project 30"
task2 = "2. Buy groceries"
task3 = "3. Call a friend"

# 2. Displaying the initial tasks:
print(task1)
print(task2)
print(task3)

# 3. Getting the user's choice for a completed task:
#    I'll ask the user to enter the number of the task they completed.
#    Remember to convert the input to an integer.
choice_str = input("\nEnter the number of the task you completed (1, 2, or 3): ")
choice = int(choice_str) # Convert the text input to an integer

# --- Marking a Task as Done (Conditional Display) ---
# This is the core logic. Based on the user's `choice`, I'll print
# the tasks again, but add "(DONE)" next to the selected one.

print("\n--- Updated To-Do List ---")
if choice == 1:
    print(f"{task1} (DONE)")
    print(task2)
    print(task3)
elif choice == 2:
    print(task1)
    print(f"{task2} (DONE)")
    print(task3)
elif choice == 3:
    print(task1)
    print(task2)
    print(f"{task3} (DONE)")
else:
    # If the choice isn't 1, 2, or 3, it's an invalid input.
    print("Invalid choice. No task was marked as completed.")
    print("Your tasks remain:")
    print(task1)
    print(task2)
    print(task3)

print("\nGreat job on your tasks!")

# --- What I learned (making information interactive!) ---
# - How to display pre-defined information to the user.
# - Using `if`/`elif`/`else` to respond to numerical user choices for modifying display.
# - The concept of "marking" an item as complete by changing its printed output.
# - This project hints at how I'll eventually manipulate actual lists of items
#   when I learn about Python's list data structures!
# - It's cool to create programs that manage simple information.
