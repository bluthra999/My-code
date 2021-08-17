# Enter the two strings
firststring = input("Enter the first string: ")
secondstring = input("Enter the second string: ")

# Convert to sets
firstset = set(firststring)
secondset = set(secondstring)

# Get the intersection i.e. the characters common to both
common = firstset.intersection(secondset)

if len(common) == 0:
    print("There are no characters common to both sets")
else:
    print("The characters common to both sets are:")
    for c in common:
        print(c, end=" ")
    print("")

# Get the difference i.e. the characters not in both
common = firstset.symmetric_difference(secondset)

if len(common) == 0:
    print("There are no characters not in both sets")
else:
    print("The characters not in both sets are:")
    for c in common:
        print(c, end=" ")
    print("")
