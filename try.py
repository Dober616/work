import math

class MyMath:
    def __init__(self, length=0, radius=0):
        self.length = length
        self.radius = radius

    def circle(self):
        return 2 * math.pi * self.length

    def s(self):
        return math.pi * self.radius ** 2

res = MyMath(length=10)
print(res.circle())
res_2 = MyMath(radius=5)
print(res_2.s())

