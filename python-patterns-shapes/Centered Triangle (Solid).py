print("--- Centered Solid Triangle Pattern ---")

try:
    height = int(input("Enter the height of the triangle (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0:
    print("Height must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(height): # r will be 0, 1, 2, ... height-1
    # Calculate number of characters for this row (1, 3, 5, ...)
    num_chars = 2 * r + 1
    # Calculate number of leading spaces for centering
    num_spaces = height - 1 - r

    print(" " * num_spaces + "#" * num_chars)

print("\nDone!")