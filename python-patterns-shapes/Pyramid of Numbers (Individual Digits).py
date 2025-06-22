print("--- Pyramid of Numbers Pattern ---")

try:
    height = int(input("Enter height (e.g., 5, max 9 for single digits): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0 or height > 9:
    print("Height must be between 1 and 9.")
    exit()

print("\nHere is your pattern:")

for i in range(1, height + 1): # i = 1, 2, ... height
    # Leading spaces for centering
    print(" " * (height - i), end="")
    # Numbers going up
    for j in range(1, i + 1):
        print(j, end="")
    # Numbers going down (excluding the peak number)
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print() # New line

print("\nDone!")