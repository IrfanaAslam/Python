print("--- Growing Alternating Character Pattern ---")

try:
    rows = int(input("How many rows? (e.g., 7): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0:
    print("Rows must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(1, rows + 1): # r = 1, 2, ... rows
    for c in range(r): # c = 0, 1, ... r-1
        if c % 2 == 0:
            print("$", end="")
        else:
            print("#", end="")
    print()

print("\nDone!")