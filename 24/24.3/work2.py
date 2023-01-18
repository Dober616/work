class Family:
    surname = 'Common Family'
    money = 10000
    have_a_house = False

    def info(self):
        print(f'Family name: {self.surname};\n'
              f'Family founds: {self.money};\n'
              f'Family house: {self.have_a_house}'
              )

    def earn_money(self, amount):
        self.money += amount
        print(f'Зарабаотано {amount} денег! Текущее состояние: {self.money}.')

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print(f'Позравляем с покупкой дома, текущее количество денег = {self.money}')
        else:
            print('Денег на дом пока не хватает')


my_family = Family()
my_family.info()
print('Пробуем купить дом')
my_family.buy_house(100000)

while not my_family.have_a_house:
    my_family.earn_money(20000)
    print(f'Заработали еще 20000, теперь у нас {my_family.money}, пробуем опять купить дом')
    my_family.buy_house(100000, discount=0)

my_family.info()


