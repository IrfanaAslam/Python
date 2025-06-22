print("--- Grid of Numbers (Column-wise) ---")

try:
    rows = int(input("Enter number of rows (e.g., 4): "))
    cols = int(input("Enter number of columns (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if rows <= 0 or cols <= 0:
    print("Dimensions must be positive.")
    exit()

print("\nHere is your pattern:")

# Create a 2D list to store numbers first
grid = [[0 for _ in range(cols)] for _ in range(rows)]

current_num = 1
# Fill grid column by column
for c in range(cols):
    for r in range(rows):
        grid[r][c] = current_num
        current_num += 1

# Print the grid row by row
for r in range(rows):
    for c in range(cols):
        print(str(grid[r][c]).ljust(3), end="")
    print()

print("\nDone!")