
# Fib Series using recurssion 

fib_series = []

# Prints the nth term 
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


# Calls the function 
x = int(input("Please enter a number \n"))
fib(x)


# Prints all n terms
for i in range(1,x+1):
    # This appends all the terms from fib(i) to the list fib_series
    fib_series.append(fib(i))
print(fib_series)




# Optimizing the recurssion using memoization


fib_series = []

def fib_efficient(n, d):

    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans

n = int(input("Please enter an int \n"))
# d can't be empty because this time we don't have any predeifined value for f0 and f1        
d = {0:1 , 1:1}
print(fib_efficient(n,d))

for i in range(1,n+1):
    # This appends all the terms from fib(i) to the list fib_series
    fib_series.append(fib_efficient(i,d))
print(fib_series)