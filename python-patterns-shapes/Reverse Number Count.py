print("--- Reverse Number Count Pattern ---")

try:
    rows = int(input("How many rows? (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0:
    print("Rows must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(1, rows + 1): # Outer loop for rows
    for num in range(r, 0, -1): # Inner loop for numbers in reverse
        print(num, end=" ")
    print() # New line for the next row

print("\nDone!")