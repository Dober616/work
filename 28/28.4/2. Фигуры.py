class Figure:
    def __init__(self, x, y, width, length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    def __str__(self):
        return f'{self.x}, {self.y}, {self.width}, {self.length}'

class Data_change(Figure):
    def __init__(self, x, y, width, length):
        super().__init__(x, y, width, length)

    def coordinates_change(self, x, y):
        self.x = x
        self.y = y

    def sides_change(self, width, length):
        self.width = width
        self.length = length



class Rectangle(Data_change):
    def __init__(self, x, y, width, length):
        super().__init__(x, y, width, length)

class Square(Data_change):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)


# my_Rectangle = Rectangle(1, 2, 3, 4)
# print(my_Rectangle)
# my_Rectangle.coordinates_change(2, 4)
# print(my_Rectangle)

my_square = Square(2, 2, 3)
print(my_square)
new_size = 5
my_square.width = new_size
my_square.length = new_size
print(my_square)

