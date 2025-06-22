print("--- Simple Pyramid/Mountain Outline ---")
print("This will print a fixed-size outline.")

height = 5 # Fixed height for simplicity
width = 9  # Fixed width, must be an odd number (2*height - 1)

print("\nHere is your pattern:")

for r in range(height): # r for row (0 to 4)
    for c in range(width): # c for column (0 to 8)
        # Condition for printing the outline
        # (r, c) represents coordinates of each cell

        # Bottom row
        if r == height - 1:
            print("#", end="")
        # Left side diagonal
        elif c == height - 1 - r:
            print("#", end="")
        # Right side diagonal
        elif c == height - 1 + r:
            print("#", end="")
        else:
            print(" ", end="") # Print space for inside

    print() # Move to the next line

print("\nDone!")