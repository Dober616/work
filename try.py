class House:
    def __init__(self):
        self.money = 0
        self.food = 50


class Inhabitant():
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.house.food += 30

    # def work(self):
    #     self.satiety -= 10
    #
    # def play(self):
    #     self.satiety -= 10
    #
    # def shopping(self):

    def info(self):
        print(f'Сытость {self.name} = {self.satiety}\n'
              f'Еды осталось {self.house.food}')


my_home = House()
alina = Inhabitant('Алина', my_home)
egor = Inhabitant('Егор', 'CoolHome')


alina.info()
alina.eat()
alina.info()