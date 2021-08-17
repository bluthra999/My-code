# Print the options menu

def PrintMenu():
    print("1. Look for substring")
    print("2. Replace substring")
    print("3. Split string")
    print("4. Convert to title case")
    print("5. Swap case")
    print("6. Exit")
    print("Choose option: ", end = "")

# Get an integer from the user to so that an option from menu is chosen
# This function always returns an integer. It will keep looping until
# a valid integer is typed.

def GetUserInput():
    while True:
        s = input()
        try:
            i = int(s)
            return i
        except:
            print("You entered an invalid number. Please try again.")

# Main program

while True:
    PrintMenu()
    i = GetUserInput()

    # Find a substring in a string
    if i == 1:
        print("\nThis option finds a substring in the supplied string.")
        inputstr = input("Enter the string: ")
        substr = input("Enter the substring: ")
        substrpos = 0
        while substrpos != -1:
            substrpos = inputstr.find(substr, substrpos)
            if substrpos != -1:
                print("Substring starts at offset: ", substrpos)
                substrpos += 1

    # Replace substring
    elif i == 2:
        print("\nThis option replaces \"good\" by \"best\" in the supplied string.")
        inputstr = input("Enter the string: ")
        newstr = inputstr.replace("good", "best")
        print(newstr)

    # Split string
    elif i == 3:
        print("\nThis option splits the string using the delimiter \";\".")
        inputstr = input("Enter the string: ")
        substrings = inputstr.split(";")
        for substr in substrings:
            print(substr)

    # Title case
    elif i == 4:
        print("\nThis option converts the supplied string to title case.")
        inputstr = input("Enter the string: ")
        newstr = inputstr.title()
        print(newstr)

    # Toggle case
    elif i == 5:
        print("\nThis option toggles the case of the supplied string.")
        inputstr = input("Enter the string: ")
        newstr = inputstr.swapcase()
        print(newstr)

    # Exit
    elif i == 6:
        break
    else:
        print("Unknown option: ", i)

    print("")