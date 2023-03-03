from datetime import datetime
import functools

def create_time(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'Время создания класса: {datetime.utcnow()}')
        for method in dir(cls):
            if not method.startswith('__'):
                print(method)
        return instance
    return wrapper


class Figure:
    def __init__(self, side, height=None):
        self.side = side
        self.height = height

@create_time
class Qube(Figure):
    def __init__(self, side):
        super().__init__(side)

    def surface(self):
        qube_surface = self.side**2 * 6
        return qube_surface
@create_time
class Pyramyd(Figure):
    def __init__(self, side, height):
        super().__init__(side, height)

    def surface(self):
        pyra_surface = self.side**2 + 4 * (self.side * self.height * 0.5)
        return pyra_surface

qqq = Qube(2)
print(qqq.surface())
ppp = Pyramyd(2, 3)
print(ppp.surface())