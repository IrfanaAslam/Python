print("--- Solid Triangle (Bottom-Left Cut) Pattern ---")

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
    # Print characters for the main part
    print("#" * (r + 1), end="")
    # Print trailing spaces for the "cut" part
    print(" " * (size - 1 - r)) # -1 because the last row has no cut

print("\nDone!")