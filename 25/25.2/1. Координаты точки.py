class Point:
    __count = 0
    def __init__(self, name, x=2, y=2):
        self.name = name
        self.set_x(x)
        self.set_y(y)
        Point.__count += 1

    def set_x(self, x):
        if x in range(0, 10):
            self.__x = x
        else:
            raise Exception('Недопустимое значение')

    def set_y(self, y):
        if y in range(1, 10):
            self.__y = y
        else:
            raise Exception('Недопустимое значение')

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_count(self):
        return self.__count


    def __str__(self):
        return (f'Координаты точки: x = {self.__x}, y = {self.__y}')


#
#
my_dot = Point('Первая точка')
her_dot = Point('Вторая точка', 5, 4)
print(my_dot)
print(her_dot)
my_dot.get_count()

