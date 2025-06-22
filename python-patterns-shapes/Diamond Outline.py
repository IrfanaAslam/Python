print("--- Diamond Outline Pattern ---")

try:
    half_height = int(input("Enter half height of the diamond (e.g., 4, will make total height 7): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if half_height <= 0:
    print("Half height must be positive.")
    exit()

print("\nHere is your pattern:")

# Top half (including middle row)
for r in range(half_height): # r = 0, 1, 2, ... half_height-1
    # Spaces before the first char
    leading_spaces = half_height - 1 - r
    print(" " * leading_spaces, end="")

    # First character
    print("$", end="")

    # Spaces between characters
    if r > 0: # Only for rows after the first
        middle_spaces = 2 * r - 1
        print(" " * middle_spaces, end="")
        print("$", end="") # Second character

    print() # New line after each row

# Bottom half (excluding middle row)
for r in range(half_height - 2, -1, -1): # r = half_height-2 down to 0
    leading_spaces = half_height - 1 - r
    print(" " * leading_spaces, end="")

    print("$", end="")

    if r > 0:
        middle_spaces = 2 * r - 1
        print(" " * middle_spaces, end="")
        print("$", end="")

    print()

print("\nDone!")