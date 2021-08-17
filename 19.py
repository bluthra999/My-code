import csv

# Get an integer from the user
# This function always returns an integer. It will keep looping until
# a valid integer is typed.

def GetInt():
    while True:
        s = input()
        try:
            i = int(s)
            return i
        except:
            print("You entered an invalid number. Please try again.")

# Create the CSV file containing names and marks

print("Enter the student names and marks.")
print("Enter the name exit to end the list.")

with open("Q19.csv", "w", newline="") as f:
    csvwriter = csv.writer(f)

    numstudents = 0
    while True:
        print("Student %d name: " % (numstudents+1,), end="")
        name = input()

        # Check for end of list
        if name == "exit":
            if numstudents >= 3:
                break
            else:
                print("You need to enter at least three students")
                continue

        print("Student %d mark: " % (numstudents+1,), end="")
        mark = GetInt()
        csvwriter.writerow([name,mark])
        numstudents += 1

print("No. students = %d" % (numstudents,))

# Read back the CSV file printing every third record

print("%-20s %8s" % ("Student", "Mark"))

with open("Q19.csv", "r") as f:
    csvreader = csv.reader(f)

    numstudents = 0
    for row in csvreader:
        numstudents += 1
        if numstudents % 3 == 0:
            print("%-20s %8s" % (row[0], row[1]))
