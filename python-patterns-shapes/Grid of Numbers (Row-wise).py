print("--- Grid of Numbers (Row-wise) ---")

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

current_num = 1
for r in range(rows):
    for c in range(cols):
        # Using .ljust() to align numbers if they get multi-digit
        print(str(current_num).ljust(3), end="") # Print num, then 2 spaces
        current_num += 1
    print()

print("\nDone!")