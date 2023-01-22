class Family:
    surname = 'Иванов'
    money = 100000
    have_a_house = False

    def info(self):
        print(f'Фамилия: {self.surname}\n'
              f'Количество денег: {self.money}\n'
              f'Наличие дома: {self.have_a_house}')

    def earn_money(self, amount):
        self.money += amount
        print(f'Заработал {amount} денег.\n'
              f'Текущее количество денег {self.money}')

    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        if self.money >= price:
            self.have_a_house = True
            self.money -= price
            print(f'Поздравляем, дом куплен!\n{self.info()}')
        else:
            print(f'Денег пока не хватает. Необходимо еще {price - self.money}')


first = Family()
first.info()
first.buy_house(10 ** 6)
while not first.have_a_house:
    first.earn_money(160000)
    print('Заработали еще денег, пробуем опять купить дом')
    first.buy_house(10 ** 6)

