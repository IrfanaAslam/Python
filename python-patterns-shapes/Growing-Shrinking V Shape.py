print("--- Growing/Shrinking V-Shape ---")

try:
    half_size = int(input("Enter half size (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if half_size <= 0:
    print("Half size must be positive.")
    exit()

print("\nHere is your pattern:")

# Growing part
for i in range(half_size): # i = 0, 1, 2, ... half_size-1
    leading_spaces = i
    middle_spaces = (half_size - 1 - i) * 2 # Calculate space between V arms
    print(" " * leading_spaces + "\\" + " " * middle_spaces + "/")

# Shrinking part (excluding the top row of the second V)
for i in range(half_size - 2, -1, -1): # i = half_size-2, ... 0
    leading_spaces = i + 1 # Adjust for symmetry
    middle_spaces = (half_size - 2 - i) * 2 + 1 # Adjust for symmetry
    print(" " * leading_spaces + "/" + " " * middle_spaces + "\\")

print("\nDone!")