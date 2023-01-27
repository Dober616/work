class Family:
    surname = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(f'Фамилия: {self.surname}\n'
              f'Количество денег: {self.money}\n'
              f'Наличие дома: {self.have_a_house}')

    def earn_money(self, amount):
        self.money += amount
        print(f'Заработано {amount} денег! Текущее количество денег: {self.money}')

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.have_a_house = True
            self.money -= house_price
            print(f'Поздравляем, вы купили дом!!! Осталось денег {self.money}')
        else:
            print(f'Денег на дом пока не хватает. Нужно еще {house_price - self.money}')

my_family = Family()
print('Пробуем купить дом')
my_family.buy_house(10** 6, 0)
while not my_family.have_a_house:
    my_family.earn_money(130000)
    my_family.buy_house(10 ** 6, 10)
my_family.info()
