print("--- Solid Diamond Pattern ---")

try:
    half_height = int(input("Enter half height of the diamond (e.g., 4, total height 7): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if half_height <= 0:
    print("Half height must be positive.")
    exit()

char = input("Enter the character to use (e.g., $): ")[0] # Take first char if multiple typed

print("\nHere is your pattern:")

# Top half (including middle row)
for r in range(half_height):
    num_chars = 2 * r + 1
    num_spaces = half_height - 1 - r
    print(" " * num_spaces + char * num_chars)

# Bottom half (excluding middle row)
for r in range(half_height - 2, -1, -1):
    num_chars = 2 * r + 1
    num_spaces = half_height - 1 - r
    print(" " * num_spaces + char * num_chars)

print("\nDone!")