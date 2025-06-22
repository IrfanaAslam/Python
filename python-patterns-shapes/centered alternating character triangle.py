print("--- Centered Alternating Character Triangle ---")

try:
    height = int(input("Enter the height of the triangle (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0:
    print("Height must be positive.")
    exit()

print("\nHere is your pattern:")

char1 = '#'
char2 = '-'

for r in range(height): # r will be 0, 1, 2, ... height-1
    num_chars = 2 * r + 1
    num_spaces = height - 1 - r

    row_chars = ""
    for c_idx in range(num_chars):
        if c_idx % 2 == 0:
            row_chars += char1
        else:
            row_chars += char2
            
    print(" " * num_spaces + row_chars)

print("\nDone!")