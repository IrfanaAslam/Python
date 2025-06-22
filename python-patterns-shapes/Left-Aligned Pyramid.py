print("--- Left-Aligned Pyramid Pattern ---")

try:
    height = int(input("Enter height (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0:
    print("Height must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(1, height + 1): # i = 1, 2, ... height
    print("#" * i)

print("\nDone!")