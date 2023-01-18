class Car():

    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = int(input('Сами введите текущую скорость: '))

    def info(self):
        print(f'Цвет: {self.color}\n'
              f'цена: {self.price}\n'
              f'макс.скор: {self.max_speed}\n'
              f'тек.скор: {self.current_speed}')

toyota = Car('red', 1000000, 200, 0)
toyota.info()

bmw = Car('black', 3000000, 250, 0)
bmw.info()


