print("--- Inverted Alternating Line Pyramid ---")

try:
    height = int(input("Enter height (e.g., 6): "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if height <= 0:
    print("Height must be positive.")
    exit()

print("\nHere is your pattern:")

char_even_row = '='
char_odd_row = '+'

for r in range(height, 0, -1): # r = height, height-1, ... 1
    if r % 2 == 0: # Even length lines (e.g., 6, 4, 2)
        print(char_even_row * r)
    else: # Odd length lines (e.g., 5, 3, 1)
        print(char_odd_row * r)

print("\nDone!")