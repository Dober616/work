class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.count += 1

    def __str__(self):
        return f'Координаты: X = {self.__x}, Y = {self.__y}'

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def check_value(self, value):
        if isinstance(value, str) and value.isdigit():
            value = float(value)
        if isinstance(value, (int, float)):
            return value
        return None

    def set_x(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__x = checker_value

    def set_y(self, value):
        checker_value = self.check_value(value)
        if checker_value:
            self.__y = checker_value

point_1 = Point(2, 3)
point_1.set_x(7.7)
print(point_1.get_x(), point_1.get_y())