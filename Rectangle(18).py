class Rectangle:

    def __init__(self,length=0, breadth = 0):
        self.length  = length 
        self.breadth  = breadth

    @property        
    def length(self):
        print('getting length')
        return self.__length
    @property
    def breadth(self):
        print('getting breadth')
        return self.__breadth
    @length.setter
    def length(self, newlength):
        print('setting length = ' , newlength)
        if newlength < 0:
            raise ValueError("The length cannot be negative")
        self.__length = newlength
    @breadth.setter
    def breadth(self, newbreadth=""):
        print('setting breadth = ' , newbreadth)
        if newbreadth < 0:
            raise ValueError("The length cannot be negative")
        self.__breadth = newbreadth

    def perimenter(self):
        per = 2*(self.__length + self.__breadth)
        return per
    def area(self):
        ar = (self.__length*self.__breadth)
        return ar
        
# Get the length
while True:
  
    try:
        l = float(input("Enter the length: "))
        myrec.length = l
        break
    except ValueError as ve:
        print("Oaf! That isn't a valid length")

# Get the breadth
while True:
   
    try:
        l = float(input("Enter the breadth: "))
        myrec.breadth = l
        break
    except ValueError as ve:
        print("Oaf! That isn't a valid breadth")

print(f"The area is {myrec.area()}")
print(f"The area is {myrec.perimeter()}")