print("--- Pattern with Inverted Gap ---")

try:
    size = int(input("Enter size (e.g., 5): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if size <= 0:
    print("Size must be positive.")
    exit()

print("\nHere is your pattern:")

# Top half (growing gap)
for i in range(size): # i = 0, 1, 2, ... size-1
    left_chars = size - i
    middle_spaces = 2 * i # Gap grows by 2 each time
    print("#" * left_chars + " " * middle_spaces + "#" * left_chars)

# Bottom half (shrinking gap) - skip first row to avoid duplication
for i in range(size - 2, -1, -1): # i = size-2, ... 0
    left_chars = size - i
    middle_spaces = 2 * i
    print("#" * left_chars + " " * middle_spaces + "#" * left_chars)

print("\nDone!")