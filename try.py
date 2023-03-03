class Figure:
    def __init__(self, side, height=None):
        self.side = side
        self.height = height

class Tryangle(Figure):
    def __init__(self, side, height):
        super().__init__(side)
        self.height = height

    def area(self):
        return 0.5 * self.side * self.height

class Square(Figure):
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        return self.side ** 2

class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)
        return surface_area

class Cube(Square, SurfaceAreaMixin):
    def __init__(self, side):
        super().__init__(side)
        self.surfaces = [Square, Square, Square, Square, Square, Square]

class Pyramyd(Tryangle, Square, SurfaceAreaMixin):
    def __init__(self, side, height):
        super().__init__(side, height)
        self.surfaces = [Square, Tryangle, Tryangle, Tryangle, Tryangle]

my_cube = Cube(2)
print(my_cube.surface_area())

my_tryangle = Tryangle(2, 3)
print(my_tryangle.area())

my_pyramyd = Pyramyd(2, 3)
print(my_pyramyd.surface_area())

