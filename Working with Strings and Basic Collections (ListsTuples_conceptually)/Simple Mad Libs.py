# Project 28: Simple "Mad Libs"

# After playing with individual words, I wanted to try building a small,
# interactive story generator, kind of like a "Mad Libs" game!
# My goal for this program is to:
# 1. Ask the user for a few specific types of words (like a noun, verb, adjective).
# 2. Take those words and plug them into a simple, pre-written story template.
# 3. Print the completed, silly story.
# This project is a great way to combine `input()` with f-strings to create dynamic text.

# --- My Mad Libs Story Strategy ---

print("Welcome to my Simple Mad Libs game!")
print("Help me create a silly story by providing a few words!")

# 1. Getting words from the user:
#    I'll ask for each type of word separately. Since they are all text,
#    I just use `input()` directly.

#    Asking for a noun (a person, place, or thing)
noun = input("Enter a noun (e.g., 'cat', 'tree', 'doctor'): ")

#    Asking for a verb (an action word)
verb = input("Enter a verb (e.g., 'run', 'sing', 'dance'): ")

#    Asking for an adjective (a descriptive word)
adjective = input("Enter an adjective (e.g., 'sleepy', 'shiny', 'loud'): ")

#    Asking for another noun (to make the story more interesting!)
another_noun = input("Enter another noun (e.g., 'shoe', 'cloud', 'car'): ")

# --- The Story Template (using f-strings to fill in the blanks!) ---
# This is the fun part! I've written a short story, and where I want the
# user's words to go, I've put placeholder curly braces `{}` with my variable names inside.

# 2. Constructing the story:
print("\n--- Your Silly Story ---")
story = f"Once upon a time, a {adjective} {noun} decided to {verb} all the way to the {another_noun}. It was a truly remarkable adventure!"

# 3. Printing the completed story:
#    The f-string does all the work of inserting the words, and `print()` displays the final story.
print(story)
print("\nHope you enjoyed your custom story!")

# --- What I learned (making dynamic text!) ---
# - How to collect multiple pieces of text input from the user for different purposes.
# - The powerful and flexible use of f-strings to build complex sentences and stories
#   by embedding multiple variables.
# - The concept of a story template with placeholders.
# - Building a program that creates unique content based on user interaction.
# - This feels like a fun creative outlet for my Python skills!
