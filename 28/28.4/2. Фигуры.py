from abc import ABC, abstractmethod
class Figure(ABC):
    def __init__(self, x, y, side_1, side_2):
        self.x = x
        self.y = y
        self.side_1 = side_1
        self.side_2 = side_2

class ResizeMixin:
    def resize(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

class MoveMixin:
    def move(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Figure, ResizeMixin, MoveMixin):
    def __init__(self, side_1, side_2, x, y):
        super().__init__(side_1, side_2, x, y)

class Square(Figure, ResizeMixin, MoveMixin):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)




square = Square(4, 5, 6)
square.resize(9, 6)
print(square.side_1)
print(square.side_2)