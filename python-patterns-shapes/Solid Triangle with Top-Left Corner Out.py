print("--- Solid Triangle (Top-Left Cut) Pattern ---")

try:
    size = int(input("Enter size (e.g., 6): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if size <= 0:
    print("Size must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(size):
    # Print leading spaces for the "cut" part
    print(" " * r, end="")
    # Print characters for the rest of the row
    print("#" * (size - r))

print("\nDone!")