from abc import ABC, abstractmethod
class Figure(ABC):
    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width


class MovebleMixin:
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

class ResizebleMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Figure, MovebleMixin, ResizebleMixin):
    pass

class Square(Figure, MovebleMixin, ResizebleMixin):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)
        




rect_1 = Rectangle(10, 20, 5, 6)
rect_2 = Rectangle(30, 40, 10, 11)
square = Square(50, 70, 7)



for figure in [rect_1, rect_2, square]:
    new_size_x = figure.length * 3
    new_size_y = figure.width * 3
    figure.resize(new_size_x, new_size_y)
    print(figure.length, figure.width)



