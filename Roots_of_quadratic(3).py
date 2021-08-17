


def roots():
    print("General form of Quadratic Equation : Ax²+bx+C")
    A=float(input("Coef of x² \n"))
    B=float(input("Coef of x \n"))
    C=float(input("Constant c\n"))

    D=B*B-4*A*C
    x_1=(-B-D**.5)/(2*A)
    x_2=(-B+D**.5)/(2*A)
    print('x_1=' , x_1)
    print('x_2=', x_2)
    return (x_1 , x_2)

# driver program 
z = roots()
