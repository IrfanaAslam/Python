print("--- Simple Checkerboard Pattern ---")
print("This will print a small 5x5 checkerboard.")

print("\nHere is your pattern:")

for row in range(5): # 5 rows (0, 1, 2, 3, 4)
    for col in range(5): # 5 columns (0, 1, 2, 3, 4)
        # If the sum of row and column is even, print '#', else print ' '
        if (row + col) % 2 == 0:
            print("#", end="") # Print character without new line
        else:
            print(" ", end="") # Print space without new line
    print() # Move to the next line after each row is complete

print("\nDone!")