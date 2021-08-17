class STUDENT:

    # On construction set the name and roll number and clear the marks list
    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum
        self.marks = [0, 0, 0]

    # On destruction clear the marks list
    def __del__(self):
        self.marks.clear()

    # Set the marks
    def SetMark(self, subject, mark):
        if subject == 0:
            self.marks[0] = mark;
        elif subject == 1:
            self.marks[1] = mark;
        elif subject == 2:
            self.marks[2] = mark;
        else:
            print("Unknown subject number: ", subject)

# Main program

# This is the list of students
students = [ ]

num = int(input("How many students?: "))
for i in range(num):
    name = input("input name of student " + str(i+1) + ": ")
    rollnum = input("input roll number of student " + name + ": ")
    s = STUDENT(name, rollnum)

    for j in range(3):
        mark = input("input mark for subject " + str(j+1) + ": ")
        s.SetMark(j, mark)

    students.append(s)

for i in range(num):
    print(students[i].name)
    print(students[i].rollnum)
    print(students[i].marks)