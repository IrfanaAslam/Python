print("--- Alternating Row Pattern ---")

try:
    rows = int(input("How many rows? (e.g., 6): "))
    cols = int(input("How many columns per row? (e.g., 10): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if rows <= 0 or cols <= 0:
    print("Dimensions must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(rows):
    if r % 2 == 0: # Even rows
        print("+" * cols)
    else:          # Odd rows
        print("-" * cols)

print("\nDone!")