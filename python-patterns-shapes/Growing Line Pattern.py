print("--- Growing Line Pattern ---")

try:
    rows = int(input("How many rows do you want? (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0:
    print("Number of rows must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(1, rows + 1): # i will go from 1 up to 'rows'
    # Print the character 'i' number of times
    print("#" * i)

print("\nDone!")