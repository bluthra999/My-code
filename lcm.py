import math 

def compute_lcm(x,y):
    lcm_of_two_numbers = math.lcm(x,y)
    return (lcm_of_two_numbers)

x= int(input('Please enter a number'))
y = int(input('Please enter a number'))

print(compute_lcm(x,y))

