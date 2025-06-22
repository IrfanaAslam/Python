print("--- Number Pyramid (Repeated) ---")

try:
    rows = int(input("Enter the number of rows (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0:
    print("Number of rows must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(1, rows + 1): # i will be 1, 2, 3, ... rows
    print(str(i) * i) # Convert i to string, then repeat it i times

print("\nDone!")