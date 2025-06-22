print("--- Stepped Grid with Inner Content ---")

try:
    size = int(input("Enter size (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if size <= 0:
    print("Size must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(size): # r = 0, 1, ... size-1
    leading_spaces = r * 2 # Increase indentation for each step
    print(" " * leading_spaces, end="")

    # Content of the step
    for c in range(size - r): # Characters decrease with each step
        if c % 2 == 0:
            print("[", end="")
        else:
            print("]", end="")
    print()

print("\nDone!")