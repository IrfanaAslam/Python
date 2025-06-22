print("--- Customizable Checkerboard Grid ---")

try:
    rows = int(input("Enter number of rows (e.g., 6): "))
    cols = int(input("Enter number of columns (e.g., 8): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if rows <= 0 or cols <= 0:
    print("Dimensions must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(rows):
    for c in range(cols):
        if (r + c) % 2 == 0:
            print("#", end="")
        else:
            print(" ", end="")
    print()

print("\nDone!")