# simple class to represent fractions


class fractions(object):
    """A number represented as a fraction"""

    def __init__(self, num, denum):
        """num and denum are integers"""
        assert type(num) is int and type(denum) is int, "ints are not used"
        self.num = num
        self.denum = denum

    def __str__(self):
        return str(self.num) + "/" + str(self.denum)

    def __add__(self, other):
        addednum = self.num * other.denum + self.denum * other.num
        addeddenum = self.denum * other.denum
        return fractions(addednum, addeddenum)

    def __sub__(self, other):
        top = self.num * other.denum - self.denum * other.num
        bott = self.denum * other.denum
        return fractions(top, bott)

    def __float__(self):
        return self.num / self.denum

    def inverse(self):
        return fractions(self.denum, self.num)


a = fractions(14, 64)
b = fractions(35, 24)
c = a + b
print(c)
print(float(c))
print(fractions.__float__(c))
print(float(b.inverse()))
