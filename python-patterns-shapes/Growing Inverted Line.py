print("--- Growing Inverted Line Pattern ---")

try:
    max_length = int(input("Enter max length (e.g., 10): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if max_length <= 0:
    print("Max length must be positive.")
    exit()

print("\nHere is your pattern:")

for i in range(1, max_length + 1): # i = 1, 2, ... max_length
    line = "#" * i
    # Pad the line with spaces on the left to reach max_length width
    print(line.rjust(max_length)) # rjust pads on the left

print("\nDone!")