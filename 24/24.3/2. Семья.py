class Family:
    name = 'Family name'
    family_money = 100000
    house = False

    def print_info(self):
        print(f'Имя семьи: {Family.name}\n'
              f'Количество денег: {Family.family_money}\n'
              f'Наличие дома: {Family.house}')


    def earn_money(self):
        money = int(input('Заработали денег: '))
        Family.family_money += money

    def buy_a_house(self):
        house_price = 500000
        while Family.house == False:
            if Family.family_money >= house_price:
                print(f'Дом куплен! Поздравляем! Да еще и осталось {Family.family_money - house_price}')
                Family.house = True
                Family.family_money -= house_price
            else:
                print(f'Пока купить дом не можем, не хватает {house_price - Family.family_money}')
                Family.earn_money(self)


sims = Family()
sims.print_info()
sims.buy_a_house()
