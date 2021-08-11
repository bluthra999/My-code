
# The formal parameter needs to initialize before calling a function)
# A funtion can also be without any parameter 
def g():


    n = int(input("Please enter a number \n"))
    t= n*"$"
    s = "$" + " "*(n-2) + "$ \n"
    r= s*(n-2)

    print(f"{t}\n{r}{t}")
  
z = g()



def f():
    '''n = no. of rows of stars you want '''

    n = int(input("Please enter a number \n"))
    for i in range(1,n+1):
        x= "*"
        y = i*x
        print(y)
    return y
z = f()




