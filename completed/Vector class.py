def checkLen(f):
    def wrapper(self, b):
        if self.size != b.size:
            raise ValueError()
        return f(self, b)

    return wrapper


class Vector:
    def __init__(self, a):
        self.arr = a
        self.size = len(a)

    def __str__(self):
        return str(tuple(self.arr))

    @checkLen
    def add(self, b):
        arrB = b.arr
        return Vector([self.arr[i] + arrB[i] for i in range(self.size)])

    @checkLen
    def subtract(self, b):
        arrB = b.arr
        return Vector([self.arr[i] - arrB[i] for i in range(self.size)])

    @checkLen
    def dot(self, b):
        arrB = b.arr
        return sum(self.arr[i] * arrB[i] for i in range(self.size))

    def norm(self):
        return sum(self.arr[i] ** 2 for i in range(self.size)) ** 0.5

    def equals(self, b):
        return b.size == self.size and all(self.arr[i] == b.arr[i] for i in range(self.size))


"""
a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)  
"""
