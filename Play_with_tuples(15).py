t1 = (1,2,5,7,9,2,4,6,8,10)
t1len = len(t1)

# Part (a): print the first and second halves on two lines
halfway = int(t1len/2)
for i in range(halfway):
    print(t1[i], end="")
    print(" ", end="")
print("")

for i in range(halfway,t1len):
    print(t1[i], end="")
    print(" ", end="")
print("")

# Part (b): create and print a tuple containing the even values
evenlist = []
for i in range(t1len):
    if t1[i] % 2 == 0:
        evenlist.append(t1[i])
eventuple = tuple(evenlist)
print(eventuple)

# Part (c): concatenate t2 = (11,13,15) to t1
t2 = (11,13,15)
t3 = t1 + t2
print(t3)

# Part (d): find the min and max element of t3
t3min = t3[0]
t3max = t3[0]
for a in t3:
    if a < t3min:
        t3min = a
    if a > t3max:
        t3max = a
print("Min = ", t3min)
print("Max = ", t3max)