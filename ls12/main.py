# Mixin, Inheritance 

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def S(self):
        print("Re S")
        return self.a * self.b
    
    def P(self):
        return (self.a + self.b) * 2 

class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    def S(self):
        print("Sq S")
        return self.a ** 2

s = Square(9)
print(s.P())
print(s.S())