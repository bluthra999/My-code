# To understand the code one should be familiar with Linear Algebra
# To learn about the mathematics behind the code refer to the following link : # https://bit.ly/2VWlmFa 
 



import numpy as np

lmbd_1 = (1+np.sqrt(5))/2
lmbd_2 = (1-np.sqrt(5))/2

a       = np.matrix([[1,      1],      [1,  0]])
s       = np.matrix([[lmbd_1, lmbd_2], [1,  1]])
s_inv   = np.matrix([[1,     -lmbd_2], [-1, lmbd_1]]) * (1/np.sqrt(5))
eig_val = np.matrix([[lmbd_1, 0],      [0,  lmbd_2]])
u_0     = np.matrix([[1],              [0]])

def eig_k(k):
    return eig_val ** k

def u_k(k):
    return s * eig_k(k) * s_inv * u_0

def fib(n):
    f_n = u_k(n)[1,0]
    return int(round(f_n))

[fib(n) for n in range(15)]