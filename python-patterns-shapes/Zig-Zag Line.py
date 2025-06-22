print("--- Zig-Zag Line Pattern ---")

try:
    width = int(input("Enter width (e.g., 10): "))
    height = int(input("Enter height (e.g., 7): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

if width < 3 or height < 2:
    print("Width min 3, Height min 2.")
    exit()

print("\nHere is your pattern:")

for r in range(height):
    pos = r % (width * 2 - 2) # Pattern repeats
    if pos >= width: # If we're on the way back
        pos = (width * 2 - 2) - pos

    print(" " * pos + "*")

print("\nDone!")