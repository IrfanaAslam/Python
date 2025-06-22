print("--- Double Line Border Pattern ---")

try:
    length = int(input("Enter the length of the lines (e.g., 12): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if length <= 0:
    print("Length must be positive.")
    exit()

print("\nHere is your pattern:")

print("=" * length) # First line
print("-" * length) # Second line

print("\nDone!")