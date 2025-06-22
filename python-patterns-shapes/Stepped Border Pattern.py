print("--- Stepped Border Pattern ---")

try:
    size = int(input("Enter the size of the steps (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if size <= 0:
    print("Size must be positive.")
    exit()

print("\nHere is your pattern:")

# Top part
for i in range(size):
    print(" " * i + "####") # Indent increases, fixed number of characters

# Bottom part (inverted indentation)
for i in range(size - 2, -1, -1): # From size-2 down to 0
    print(" " * i + "####")

print("\nDone!")