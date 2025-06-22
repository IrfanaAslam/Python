print("--- Numbered Grid (Snake Pattern) ---")

try:
    rows = int(input("Enter number of rows (e.g., 5): "))
    cols = int(input("Enter number of columns (e.g., 6): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if rows <= 0 or cols <= 0:
    print("Dimensions must be positive.")
    exit()

print("\nHere is your pattern:")

current_num = 1
for r in range(rows):
    if r % 2 == 0: # Even rows: L-R
        for c in range(cols):
            print(str(current_num).ljust(3), end="")
            current_num += 1
    else: # Odd rows: R-L
        # Calculate numbers for this row first, then print in reverse
        row_numbers = []
        for _ in range(cols):
            row_numbers.append(current_num)
            current_num += 1
        for num in reversed(row_numbers):
            print(str(num).ljust(3), end="")
    print()

print("\nDone!")