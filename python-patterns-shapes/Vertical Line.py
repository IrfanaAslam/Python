print("--- Vertical Line Pattern ---")

try:
    height = int(input("Enter the height of the line (e.g., 8): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0:
    print("Height must be positive.")
    exit()

print("\nHere is your pattern:")

for _ in range(height): # '_' is used when the loop variable itself isn't needed
    print("|")

print("\nDone!")