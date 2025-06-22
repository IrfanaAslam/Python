# Project 13: Multiplication Table (up to 10)

# After counting up and down, I wanted to apply loops to something
# more practical – like generating a multiplication table!
# My goal for this project is to ask the user for a number, and then
# print its multiplication table from 1 up to 10.
# This feels like a great way to combine input, loops, and arithmetic.

# --- My Multiplication Table Journey ---

# 1. Getting the number from the user:
#    I need a whole number for my multiplication table, so `int()` is the way to go.
#    I'll ask the user which table they want to see.
print("Welcome to my Multiplication Table Generator!")
table_number_str = input("Please enter a whole number to see its multiplication table (e.g., 5): ")
table_number = int(table_number_str) # Converting the text to an integer

# --- Using a `for` loop for repetitions! ---
# This is where the `for` loop shines again! I know I want to repeat
# the multiplication 10 times (for 1 through 10).
# So, `range(1, 11)` is perfect because it goes from 1 up to (but not including) 11.

# 2. Generating and printing the table:
print(f"\nHere is the multiplication table for {table_number}:")
for multiplier in range(1, 11): # Loop from 1 to 10 (inclusive)
    # Inside the loop, I perform the multiplication.
    product = table_number * multiplier

    # Then, I print each line of the table.
    # I'm using an f-string to make the output look exactly like a multiplication fact.
    print(f"{table_number} x {multiplier} = {product}")

# 3. Final message:
#    Once the loop finishes all 10 multiplications, I print a friendly closing message.
print("\nThat's the end of the table!")
print("Hope it was helpful!")

# --- What I learned (and reinforced) ---
# - Powerful application of the `for` loop with `range()` for repetitive tasks.
# - Combining numerical input, loops, and arithmetic (`*`).
# - Generating structured output that's easy to read.
# - More confidence in using f-strings for precise formatting.
# - Building a program that creates useful information!
