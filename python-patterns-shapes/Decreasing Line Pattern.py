print("--- Decreasing Line Pattern ---")

try:
    start_length = int(input("Enter the starting length of the longest line (e.g., 7): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if start_length <= 0:
    print("Starting length must be positive.")
    exit()

print("\nHere is your pattern:")

# Loop from 'start_length' down to 1
for i in range(start_length, 0, -1):
    print("=" * i)

print("\nDone!")