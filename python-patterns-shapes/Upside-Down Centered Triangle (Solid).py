print("--- Upside-Down Centered Solid Triangle Pattern ---")

try:
    height = int(input("Enter the height of the triangle (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0:
    print("Height must be positive.")
    exit()

print("\nHere is your pattern:")

# Loop from height-1 down to 0
for r in range(height - 1, -1, -1):
    num_chars = 2 * r + 1
    num_spaces = height - 1 - r

    print(" " * num_spaces + "*" * num_chars)

print("\nDone!")