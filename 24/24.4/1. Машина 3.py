class Car:

    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print(f'{self.color}, {self.price}, {self.max_speed}, {self.current_speed}')

toyota = Car('red', 100000, 200, 0)
toyota.info()