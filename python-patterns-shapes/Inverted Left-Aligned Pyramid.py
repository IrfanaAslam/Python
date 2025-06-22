print("--- Inverted Left-Aligned Pyramid Pattern ---")

try:
    height = int(input("Enter height (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0:
    print("Height must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(height, 0, -1): # i = height, height-1, ... 1
    print("#" * i)

print("\nDone!")