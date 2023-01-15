class Family:
    family_name = ''
    family_founds = 0
    having_house = False

    def family_info(self):
        print(f'Название семьи: {self.family_name}\n'
              f'Сбережения семьи: {self.family_founds}\n'
              f'Наличие дома: {self.having_house}'
              )
    def get_money(self, summ):
        self.family_founds += summ
        print(f'Заработано денег: {summ}! Текущее количество денег: {self.family_founds}')

    def buy_house(self, price, discount=0):
        house_price = price - price * (discount / 100)
        if self.family_founds >= house_price:
            print(f'Дом куплен за {house_price}, остаток средств {self.family_founds}')
            self.having_house = True
        else:
            print('Денег пока не хватает')


my_family = Family()
my_family.family_info()
my_family.family_name = 'Ивановы'
my_family.family_founds = 900000
price = 1000000
my_family.buy_house(price)
my_family.get_money(price - my_family.family_founds)
my_family.buy_house(price)
my_family.family_info()
