class Square:

    def __init__(self, x):
        self.x = x
        self.s = None
        self.p = None
        self.__square()
        self.__perimeter()

    def __str__(self):
        return f"Square with {self.x}cmx{self.x}cm and S={self.s}cm^2"


    def __square(self):
        if self.s == None:
            self.s =self.x ** 2
    

    def __perimeter(self):
        if self.p == None:
            self.p = 4 * self.x
    
s1 = Square(12)
print(s1)