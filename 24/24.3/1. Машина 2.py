import random

class Toyota:
    color = 'red'
    price = 2000000
    max_speed = random.randint(1, 200)
    current_speed = 0



    def print_info(self):
        print('Цвет: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}\n'.
        format(
            self.color,
            self.price,
            self.max_speed,
            self.current_speed
            )
        )
    def change_speed(self, new_speed):
        self.current_speed = new_speed

my_car = Toyota()
my_car.print_info()
my_car.change_speed(100)
my_car.print_info()
