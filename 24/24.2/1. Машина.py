import random

class Car:
    color = 'white'
    price = 0
    max_speed = random.randint(1, 200)
    current_speed = 0

    def print_info(self):
        print(f'{self.color}, {self.price}, {self.max_speed}, {self.current_speed}')

toyota = Car()
toyota.color = 'red'
toyota.price = 2000000
toyota.current_speed = 2

toyota.print_info()