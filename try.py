class Property:
    def __init__(self, worth=0, tax=0):
        self.set_worth(worth)
        self.set_tax(tax)

    def get_tax(self):
        return self.tax

    def set_tax(self, tax):
        self.tax = self.worth * tax / 100

    def get_worth(self):
        return self.worth

    def set_worth(self, worth):
        self.worth = int(input(f'Ввведите стоимость: '))

    def get_summ(self):
        return self.get_worth() + self.get_tax()


class Apartment(Property):
    def __init__(self):
        super().__init__()
        self.set_tax(0.1)


class Car(Property):
    def __init__(self):
        super().__init__()
        self.set_tax(0.5)


class CountryHouse(Property):
    def __init__(self):
        super().__init__()
        self.set_tax(0.2)

my_flat = Apartment()
my_car = Car()
my_house = CountryHouse()

general = my_flat.get_summ() + my_car.get_summ() + my_house.get_summ()
my_money = int(input('Сколько денег то у вас? '))
if my_money >= general:
    print('Поздравляем, вы можете все это купить')
else:
    print('Надо бы еще подкопить')