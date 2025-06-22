print("--- Alphabet Pyramid (Single Letter Rows) ---")

try:
    height = int(input("Enter height (e.g., 5, max 26): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0 or height > 26:
    print("Height must be between 1 and 26.")
    exit()

print("\nHere is your pattern:")

start_char_ascii = ord('A')

for r in range(height): # r = 0, 1, 2, ... height-1
    num_chars = 2 * r + 1
    num_spaces = height - 1 - r
    current_char = chr(start_char_ascii + r) # 'A', 'B', 'C', ...

    print(" " * num_spaces + current_char * num_chars)

print("\nDone!")