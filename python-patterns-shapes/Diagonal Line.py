print("--- Diagonal Line Pattern ---")

try:
    size = int(input("Enter the size of the diagonal (e.g., 7): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if size <= 0:
    print("Size must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(size): # i will be 0, 1, 2, ... size-1
    # Print 'i' spaces, then one character
    print(" " * i + "\\") # Using backslash as the character

print("\nDone!")