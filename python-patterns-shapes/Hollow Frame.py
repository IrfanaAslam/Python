print("--- Hollow Frame Pattern ---")

try:
    width = int(input("Enter width (min 3): "))
    height = int(input("Enter height (min 3): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if width < 3 or height < 3:
    print("Dimensions must be at least 3 for a visible frame.")
    exit()

print("\nHere is your pattern:")

for r in range(height):
    for c in range(width):
        # Top-left corner
        if r == 0 and c == 0:
            print("/", end="")
        # Top-right corner
        elif r == 0 and c == width - 1:
            print("\\", end="")
        # Bottom-left corner
        elif r == height - 1 and c == 0:
            print("\\", end="")
        # Bottom-right corner
        elif r == height - 1 and c == width - 1:
            print("/", end="")
        # Top or Bottom edge (horizontal lines)
        elif r == 0 or r == height - 1:
            print("-", end="")
        # Left or Right edge (vertical lines)
        elif c == 0 or c == width - 1:
            print("|", end="")
        else:
            print(" ", end="") # Inside is empty
    print() # New line after each row

print("\nDone!")