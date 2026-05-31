# Python Fraction Class with Custom Arithmetic and Reduction

class fraction (object ):
    def __init__(self,num,denom):
        assert type(num)==int and      type(denom)==int, "ints not used"
        self.num=num
        self.denom=denom
    def __str__(self):
        return "<" + str(self.num)+"/"+str(self.denom)+">"
    def __add__(self,other):
        top=self.num*other.denom+ other.num*self.denom
        down=self.denom*other.denom
        return fraction (top,down)
    def __sub__(self,other):
        top=self.num*other.denom -  other.num*self.denom
        down=self.denom*other.denom
        return fraction (top,down)
    def __float__(self):
        return self.num/self.denom
    def inverse(self):
        return fraction (self.denom,self.num)
    def __mul__(self,other):
        top=self.num*other.num
        down=self.denom*other.denom
        return fraction (top, down)
    def __truediv__(self,other):
        top=self.num*other.denom
        down=self.denom*other.num
        return fraction (top,down)
    def reduce(self):
        def get_gcd(a,b):
            while b:
                a,b=b,a%b
            return abs(a)
        gcd=get_gcd(self.num,self.denom)
        top=self.num//gcd
        down=self.denom//gcd
        return fraction (top, down)

a = fraction(1, 4)
b = fraction(3, 4)
print("Fraction A:", a)
print("Fraction B:", b)
c = a + b
print("Addition (1/4 + 3/4):", c)
d = b - a
print("Subtraction (3/4 - 1/4):", d)
e = a * b
print("Multiplication (1/4 * 3/4):", e)
f = a / b
print("Division (1/4 / 3/4):", f)
print("Float value of B:", float(b))
print("Inverse of A:", a.inverse())
unreduced = fraction(4, 12)
print("Unreduced Fraction:", unreduced)
print("Reduced Fraction:", unreduced.reduce())
