# Project 29: Basic Shopping List Manager (Text-based)

# After creating silly stories, I wanted to build something a bit more
# "utility-like," even if it's super simple for now.
# My goal for this project is to simulate a very basic shopping list.
# For a beginner, without using actual Python list data structures yet
# (as per the "no external libraries/complex concepts" rule, although built-in
# lists are technically fine, I'm keeping it super fundamental here),
# this means I'll ask about a few fixed items and confirm if they're "added."
# It's a stepping stone to understanding how to manage collections of data.

# --- My Basic Shopping List Idea ---

print("Welcome to my Basic Shopping List Manager!")
print("Let's add some items to your conceptual list.")
print("I can help you add a few common grocery items.")

# 1. Asking about the first item:
#    I'll ask the user if they want to "add" a specific item.
#    Their input will just be a confirmation, not the item itself.
item1_name = "Milk"
add_item1 = input(f"Do you want to add '{item1_name}' to your shopping list? (yes/no): ").lower()

# 2. Confirming addition for the first item:
if add_item1 == 'yes':
    print(f"'{item1_name}' has been conceptually added to your list!")
else:
    print(f"Okay, '{item1_name}' not added.")

# 3. Asking about the second item:
item2_name = "Bread"
add_item2 = input(f"Do you want to add '{item2_name}' to your shopping list? (yes/no): ").lower()

# 4. Confirming addition for the second item:
if add_item2 == 'yes':
    print(f"'{item2_name}' has been conceptually added to your list!")
else:
    print(f"Okay, '{item2_name}' not added.")

# 5. Asking about the third item:
item3_name = "Eggs"
add_item3 = input(f"Do you want to add '{item3_name}' to your shopping list? (yes/no): ").lower()

# 6. Confirming addition for the third item:
if add_item3 == 'yes':
    print(f"'{item3_name}' has been conceptually added to your list!")
else:
    print(f"Okay, '{item3_name}' not added.")

# --- What I learned (thinking about "collections") ---
# - How to guide a user through a series of choices for different items.
# - Using `input()` for yes/no confirmations.
# - The `.lower()` string method to make input case-insensitive (so 'Yes' or 'YES' works).
# - This project hints at how I'll eventually manage actual lists of items in Python,
#   even though I'm not using formal list structures yet.
# - It's cool to make programs that feel like simple tools!
