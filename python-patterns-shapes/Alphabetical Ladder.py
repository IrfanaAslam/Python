print("--- Alphabetical Ladder Pattern ---")

try:
    rows = int(input("How many rows? (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0 or rows > 26:
    print("Rows must be between 1 and 26.")
    exit()

print("\nHere is your pattern:")

start_ascii = ord('A')

for r in range(rows): # r = 0, 1, 2...
    current_char_ascii = start_ascii + r
    print(chr(current_char_ascii) * (r + 1)) # Repeat current letter r+1 times

print("\nDone!")