print("--- Simple Cross Pattern ---")

try:
    size = int(input("Enter size (e.g., 7, preferably odd): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if size <= 0:
    print("Size must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(size):
    for c in range(size):
        # Check for diagonal conditions
        if r == c or r + c == size - 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()

print("\nDone!")