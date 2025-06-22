print("--- Alphabetical Pattern ---")

try:
    rows = int(input("How many rows do you want? (e.g., 5, max 26): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0 or rows > 26:
    print("Number of rows must be between 1 and 26.")
    exit()

print("\nHere is your pattern:")

start_char_ascii = ord('A') # Get ASCII value of 'A'

for r in range(rows): # r = 0, 1, 2, ... rows-1
    for c in range(r + 1): # c = 0, 1, ... r
        # Calculate the ASCII value of the character to print
        # A, B, C, ...
        char_to_print_ascii = start_char_ascii + c
        print(chr(char_to_print_ascii), end=" ") # Convert ASCII back to character
    print()

print("\nDone!")