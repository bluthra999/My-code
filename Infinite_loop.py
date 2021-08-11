#Loop that runs forever until 
#  a positive integer is entered#

n = float(input("Please enter a postiive number"))


if n <= 0:
    while  n <= 0:
        print("Please try again")
        n = float(input("Please enter a positive number"))
        
else: 
    print(f"Yay! {n} is Positive Number")