class Coordinates:
    count = 0


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Coordinates.count += 1


    def info(self):
        print(self.x, self.y, self.count)

point_1 = Coordinates(1, 2)
point_2 = Coordinates(3, 4)
point_3 = Coordinates(5, 6)

point_3.info()