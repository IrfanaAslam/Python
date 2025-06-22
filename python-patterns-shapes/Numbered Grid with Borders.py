print("--- Numbered Grid with Borders ---")

try:
    rows = int(input("Enter number of rows (min 3): "))
    cols = int(input("Enter number of columns (min 3): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if rows < 3 or cols < 3:
    print("Dimensions must be at least 3 for borders.")
    exit()

print("\nHere is your pattern:")

current_num = 1
for r in range(rows):
    for c in range(cols):
        if r == 0 or r == rows - 1: # Top or bottom border
            print("-", end="")
        elif c == 0 or c == cols - 1: # Left or right border
            print("|", end="")
        else: # Inside the grid, print numbers
            print(str(current_num % 10), end="") # Use modulo to keep numbers single digit
            current_num += 1
    print()

print("\nDone!")