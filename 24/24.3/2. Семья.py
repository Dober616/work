class Family:
    name = 'Simpsons'
    money = 10 ** 5
    house = False

    def info(self):
        print(f'Фамилия семьи: {self.name}\n'
              f'Текущее количество денег: {self.money}\n'
              f'Наличие дома: {self.house}')
    def buy_house(self, price):
        while self.house == False:
            if price <= self.money:

                self.house = True
                self.money -= price
                print('Поздравляем с покупкой!!!')
                self.info()
            else:
                print(f'На дом пока не хватает. Необходимо заработать еще {price - self.money}')
                self.earn_money()


    def earn_money(self):
        self.summ = int(input('Заработали денег: '))
        self.money += self.summ

griffins = Family()
griffins.name = 'Гриффины'
griffins.buy_house(10**6)

