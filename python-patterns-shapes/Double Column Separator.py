print("--- Double Column Separator ---")

try:
    rows = int(input("Enter rows (e.g., 8): "))
    width = int(input("Enter total width (e.g., 15, must be > 4): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if rows <= 0 or width <= 4:
    print("Rows must be positive, width > 4.")
    exit()

print("\nHere is your pattern:")

# Decide positions for the two vertical bars
bar1_pos = width // 3
bar2_pos = (width * 2) // 3

for r in range(rows):
    for c in range(width):
        if c == bar1_pos or c == bar2_pos:
            print("|", end="")
        else:
            print(".", end="") # Fill empty space with dots
    print()

print("\nDone!")