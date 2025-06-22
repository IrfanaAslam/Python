print("--- Solid Hourglass Pattern ---")

try:
    height = int(input("Enter height (e.g., 5, must be odd for symmetry): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height % 2 == 0 or height <= 0:
    print("Height must be a positive odd number.")
    exit()

print("\nHere is your pattern:")

# Top half (including middle row)
for i in range(height, 0, -2): # i will be height, height-2, ... 1
    leading_spaces = (height - i) // 2
    print(" " * leading_spaces + "@" * i)

# Bottom half (excluding middle row)
for i in range(3, height + 1, 2): # i will be 3, 5, ... height
    leading_spaces = (height - i) // 2
    print(" " * leading_spaces + "@" * i)

print("\nDone!")