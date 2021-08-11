

def  Reverse(s):
    #Convert Strings to list of numbers#
    y = list(s) 
    #Reverse the list #
    new_lst = y[::-1]
    #Convert the list of strings  to list made up of integers# 
    z = list(map(int, str(s)))
    #Sum the digits#
    sum_lst = 0
    for i in z:
        sum_lst += i
    
    print(sum_lst)
    #Convert the inverted list to string#
    Reversed = "".join(new_lst)

    #Print the result #
    print(f"Original Number :{s}")
    print(f"Sum of digits  :{sum_lst}")  

    print(f"Reversed Number  :{Reversed}") 

s= input("Please enter a number")
print(Reverse(s))
