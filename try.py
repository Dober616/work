class Figure:
    def __init__(self, length, width, height=None):
        self.length = length
        self.width = width
        self.height = height

class Tryangle(Figure):
    def __init__(self, length, height):
        super().__init__(length=length, width=None)
        self.height = height

    def area(self):
        return 0.5 * self.length * self.height

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.width * self.length

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length=length, width=length)

class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)
        return surface_area

class Cube(Square, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]

class Pyramyd(Tryangle, Square, SurfaceAreaMixin):
    def __init__(self, length, height):
        super().__init__(length, height)
        self.surfaces = [Square, Tryangle, Tryangle, Tryangle, Tryangle]

my_cube = Cube(2)
print(my_cube.surface_area())

my_tryangle = Tryangle(2, 3)
print(my_tryangle.area())

my_pyramyd = Pyramyd(2, 3)
print(my_pyramyd.surface_area())

