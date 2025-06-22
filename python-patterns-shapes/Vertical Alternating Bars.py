print("--- Vertical Alternating Bars ---")

try:
    rows = int(input("Enter number of rows (e.g., 7): "))
    cols = int(input("Enter number of columns (e.g., 10): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if rows <= 0 or cols <= 0:
    print("Dimensions must be positive.")
    exit()

print("\nHere is your pattern:")

char1 = '|'
char2 = ':'

for r in range(rows):
    for c in range(cols):
        if c % 2 == 0: # Even columns
            print(char1, end="")
        else:          # Odd columns
            print(char2, end="")
    print()

print("\nDone!")