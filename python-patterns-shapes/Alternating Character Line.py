print("--- Alternating Character Line Pattern ---")

try:
    length = int(input("Enter the length of the line (e.g., 10): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if length <= 0:
    print("Length must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(length):
    if i % 2 == 0:  # If index is even
        print("#", end="")
    else:           # If index is odd
        print("-", end="")
print() # New line after the pattern

print("\nDone!")