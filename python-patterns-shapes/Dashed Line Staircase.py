print("--- Dashed Line Staircase ---")

try:
    steps = int(input("How many steps? (e.g., 6): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if steps <= 0:
    print("Steps must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(1, steps + 1): # i will be 1, 2, 3... steps
    # Create a repeating pattern like "-#-#"
    line_pattern = "-#" * i
    # Trim to correct length if needed (optional for exact pattern)
    # For simplicity, we'll just let it extend
    print(line_pattern)

print("\nDone!")