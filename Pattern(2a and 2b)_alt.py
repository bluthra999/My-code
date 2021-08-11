varR = int(input("Enter number of rows  : "))
for i in range(1,varR+1):
    print("*"*i,end="\n")

rows = int(input("Please Enter the Total Number of Rows  : "))
columns = int(input("Please Enter the Total Number of Columns  : "))


def print_rectangle(n, m) : 
      
    for i in range(1, n+1) : 
        for j in range(1, m+1) : 
            if (i == 1 or i == n or
                j == 1 or j == m) : 
                print("$", end=" ")             
            else : 
                print(" ", end=" ")             
          
        print()
        
  # Driver 
rows = rows
columns = columns
print_rectangle(rows, columns) 
  
  
  

