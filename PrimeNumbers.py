import math 

#Empty lists#
list_of_prime = []
list_of_non_prime = []

 
        
#Function to check if a given number is prime#

def prime_check(z):
    is_prime = True
    for i in range(3,z,2):
        if z % 2 == 0 or z % i == 0:
            is_prime = False
            break

    if is_prime:
        list_of_prime.append(z)
    else:
        list_of_non_prime.append(z)
#Loop for checking numbers less than equal to  n#
n = int(input("Pleease enter a number"))
for z in range(2,n+1):
    (prime_check(z))
#Remove the numbers from the prime if they are in non prime#
# Check the Duplicates and remove if any#
list_of_prime = list(dict.fromkeys(list_of_prime))
list_of_non_prime =  list(dict.fromkeys(list_of_non_prime))
print(list_of_prime)
print(list_of_non_prime)
         



