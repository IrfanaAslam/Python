print("--- Numbered Sequential Pattern ---")

try:
    rows = int(input("How many rows do you want? (e.g., 6): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0:
    print("Number of rows must be positive.")
    exit()

print("\nHere is your pattern:")

current_number = 1
for r in range(1, rows + 1):
    for _ in range(r): # Print 'r' numbers in this row
        print(current_number, end=" ") # Print number and a space
        current_number += 1
    print() # New line after each row

print("\nDone!")