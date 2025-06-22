print("--- Growing L-Shape ---")

try:
    size = int(input("Enter size (e.g., 6): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if size <= 0:
    print("Size must be positive.")
    exit()

print("\nHere is your pattern:")

for r in range(size):
    if r == size - 1: # Last row is a full line
        print("#" * size)
    else: # Other rows have a vertical part and horizontal part
        print("#" + " " * (r - 1) + "#" if r > 0 else "#")
        # For r=0, print "#"
        # For r>0, print "#" + (r-1 spaces) + "#"

print("\nDone!")