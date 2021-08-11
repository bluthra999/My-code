def circle():

   print("Chosen Circle")

   radius=int(input("Please enter the value of radius : "))

   print("Area of the circle with the radius of ",radius," units is", 3.14*            (radius**2),"square units.")

def square():

   print("Chosen Circle")

   side=int(input("Please enter the size of a side of a square : "))

   print("Area of the square with the a side of ",side," units is",side**2,"square units.")


def rectangle():

   print("Chosen Rectangle ")

   length=int(input("Please enter the length of the rectangle : "))

   breadth=int(input("Please enter the breadth of the rectangle : "))

   print("Area of the rectangle with length and breadth ",length, " ",breadth," units is",length*breadth,"square units.")

def triangle():

    print("Chosen Triangle")



    a = float(input('Please Enter first side: '))
    b = float(input('Please Enter second side: '))
    c = float(input('Please Enter third side: : '))

# Calculating  the semi-perimiter
    s=(a+b+c)/2

# Calculating  the area
    area=(s*(s-a)*(s-b)*(s-c)) ** 0.5

    print('Area of the triangle is ' ,area,'units.')


print("Menu-\n"

       "1. Circle\n"

       "2. Square\n"

       "3. Rectangle\n" 

       "4. Triangle \n")

x=int(input("Enter the corresponding number of a shape given in the menu, whose area you wants to calculate : "))

if x==1:

   circle()

elif x==2:

   square()

elif x==3:

   rectangle()

elif x==4 :

   triangle()

else:
    

   print("No Shape Defined for the chosen number.Please Try again.")





