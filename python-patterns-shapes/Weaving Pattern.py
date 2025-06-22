print("--- Weaving Pattern ---")

try:
    rows = int(input("How many rows? (e.g., 8): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0:
    print("Rows must be positive.")
    exit()

print("\nHere is your pattern:")

width = 6 # Fixed width for simplicity

for r in range(rows):
    if r % 2 == 0: # Even rows
        print("# " * (width // 2))
    else: # Odd rows
        print(" #" * (width // 2))
print("\nDone!")