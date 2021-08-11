
def cube_fn(n):

    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3 
    return cube
  


n = int(input("Please enter a number"))
cube_fn(n)