print("--- Growing and Shrinking Ladder Pattern ---")

try:
    max_width = int(input("Enter the maximum width (e.g., 7, must be odd): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if max_width <= 0 or max_width % 2 == 0:
    print("Max width must be a positive odd number.")
    exit()

print("\nHere is your pattern:")

# Growing phase
for i in range(1, max_width + 1, 2): # i: 1, 3, 5, ... max_width
    print(" " * ((max_width - i) // 2) + "#" * i)

# Shrinking phase (starts from max_width - 2 down to 1)
for i in range(max_width - 2, 0, -2): # i: max_width-2, max_width-4, ... 1
    print(" " * ((max_width - i) // 2) + "#" * i)

print("\nDone!")