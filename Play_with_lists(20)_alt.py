# We'll use a global list
mylist = []

# Input the list
# Return the number of itms entered
def InputList():
    print("Enter the list of numbers or strings. Enter -1 to exit:")

    numitems = 0
    while True:
        print("Enter item %d: " % (numitems,), end="")
        s = input()
        try:
            x = float(s)
            if x == -1:
                return numitems
            mylist.append(x)
        except:
            mylist.append(s)
        numitems += 1

# Main program

numitems = InputList()
if numitems == 0:
    print("No data entered")
    sys.exit()
print("You entered %d items" % (numitems))

# Find out if all items are numbers or strings

allnumbers = True
allstrings = True
for n in mylist:
    try:
        x = float(n)
        allstrings = False
    except:
        allnumbers = False

if allnumbers:
    print("The list contains only numbers")
elif allstrings:
    print("The list contains only strings")
else:
    print("The list contains numbers and strings")

# If the list is all numbers count the odd numbers

if allnumbers:
    oddnumbers = 0
    for x in mylist:
        if x % 2 == 1:
            oddnumbers += 1

    print("The list contains %d odd numbers" % (oddnumbers,))

# If the list is all strings find the largest string

if allstrings:
    maxlen = 0
    maxstring = ""
    for s in mylist:
        if len(s) > maxlen:
            maxlen = len(s)
            maxstring = s

    print("The longest string in the list is " + maxstring)

# If the list is all strings count the numeric and non-numeric strings

if allstrings:
    numnumeric = 0
    numnonnumeric = 0
    for s in mylist:
        numdigits = 0
        for c in s:
            if c >= "0" and c <= "9":
                numdigits += 1
        if numdigits == 0:
            numnonnumeric += 1
        else:
            numnumeric += 1

    print("The number of strings with numeric characters is %d" % (numnumeric))
    print("The number of strings with no numeric characters is %d" % (numnonnumeric))
