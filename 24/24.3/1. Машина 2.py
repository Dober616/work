import random

class Car:
    color = 'red'
    price = 10 ** 6
    max_speed = random.randint(150, 300)
    current_speed = 0


    def speed(self):
        self.current_speed = int(input('Какая текущая скорость: '))

    def info(self):
        print(f'Цвет: {self.color}\n'
              f'Цена: {self.price}\n'
              f'Макс. скорость: {self.max_speed}\n'
              f'Тек. скорость: {self.current_speed}')



toyota = Car()
toyota.speed()
toyota.info()