






# Find out if all items are numbers or strings

def check_number(nums):
    '''nums is a list '''
    for i in nums: 
        if type(i) != int and type(i) != float:
            return False 
    return True 
l1 = [1,2,3,4,5]
print(check_number(l1))


# If the list is all numbers count the odd numbers

def count_odd(l2):
    '''l2 is a list'''
    oddnumbers = 0
    for x in l2:
        if x % 2 == 1:
            oddnumbers += 1
    return oddnumbers
l2 = [1,2,3,4,5]

print(count_odd(l2))


# If the list is all strings find the largest string


def largest_string(l3):
    x = max(l3 , key=  len)
    print(x)
    return None
l3 = ["B" , "jklm" ,"ghi" , "def" , "abc"]
z = largest_string(l3)



# If the list is all strings count the numeric and non-numeric strings


def count(l4):
    '''l4 is a list '''
    count_number = 0
    count_str = 0
    for i in l4:
    
        if  i.isdigit() == True:
            count_number  += 1 
        
        else: 
            count_str += 1 
    return print(f"number of strings : {count_str} , number of numbers : {count_number}" )
l4 = ["1","2", "lmno" ,"ghi" , "def" , "abc"]
print(count(l4))