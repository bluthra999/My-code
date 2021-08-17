def factorial(n):
    if n ==0 or n == 1:
        return 1 
    else: 
      return n*factorial(n-1)

n = int(input(""))
print(factorial(n))

sum = 0
for i in range(0,n+1):
     sum += ((-1)**i)/factorial(i)

print(sum)

# factorial through iteration
# n = int(input(""))

# fact = 1
# for i in range(n,0,-1):
#     fact = fact*i

# print(fact)   