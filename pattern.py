# A simple square pattern
rows = 5
for i in range(rows):
    # This inner loop prints 5 asterisks for each row
    for j in range(rows):
        print("*", end=" ")
    print()  # Move to the next line after each row


# A right-angled triangle pattern
rows = 5
for i in range(rows):
    # The number of asterisks is (i + 1)
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("*****************")
# An inverted right-angled triangle
rows = 5
for i in range(rows, 0, -1):
    # The number of asterisks is i
    for j in range(i):
        print("*", end=" ")
    print()



# An inverted right-angled triangle
rows = 5
for i in range(rows, 0, -1):
    # The number of asterisks is i
    for j in range(i):
        print("*", end=" ")
    print()





# A full pyramid pattern
rows = 5
for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")
    print()



rows = 5
for i in range(rows):
    for j in range(rows -1 - i):
        print("*", end="")
    print()
