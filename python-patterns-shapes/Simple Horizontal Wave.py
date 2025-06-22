print("--- Simple Horizontal Wave ---")

try:
    rows = int(input("How many rows? (e.g., 7): "))
    wave_length = 5 # Fixed for simplicity
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if rows <= 0:
    print("Rows must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(rows):
    if r % 4 == 0: # Top of wave
        print("  " * 0 + "~~~")
    elif r % 4 == 1: # Moving down
        print("  " * 1 + "~~~")
    elif r % 4 == 2: # Bottom of wave
        print("  " * 2 + "~~~")
    elif r % 4 == 3: # Moving up
        print("  " * 1 + "~~~")

print("\nDone!")