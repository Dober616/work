import random


class Car:
    color = 'Красный'
    price = 1000000
    max_speed = random.randint(100, 250)
    current_speed = 0

    def info_print(self):
        print(f'Цвет машины: {Car.color}\n'
              f'цена: {Car.price}\n'
              f'Максимальная скорость: {Car.max_speed}\n'
              f'Текущая скорость: {Car.current_speed}')

    def speed_choose(self):
        Car.current_speed = int(input('Введите текущую скорость автомобиля: '))


toyota = Car()

toyota.speed_choose()
toyota.info_print()
