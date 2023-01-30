class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Имя: {self.__name}, фамилия: {self.__surname}, ' \
               f'возраст: {self.__age}'

    def get_name(self):
        return self.__name



class Emploee(Person):
    def __init__(self, name, surname, age, bet=0, percent=0, hour=0):
        super().__init__(name, surname, age)
        self.bet = bet
        self.percent = percent
        self.hour = hour
        self.set_salary()

    def set_salary(self):
        self.salary = self.bet + (self.percent * 5 / 100) + (self.hour * 100)

    def get_salary(self):
        return self.salary


class Manager(Emploee):
    def __init__(self, name, surname, age, bet=0):
        super().__init__(name, surname, age)
        self.set_bet(bet)

    def set_bet(self, bet):
        bet = int(input(f'Введите оклад {self.get_name()}: '))
        if bet > 0:
            self.bet = bet
        else:
            raise Exception('Оклад не может быть отрицательным')

    def get_bet(self):
        return self.bet

    def get_salary(self):
        return self.bet

    def __str__(self):
        info = super().__str__()
        info = f'{info}, зарплата: {self.get_salary()}'
        return info


class Agent(Emploee):
    def __init__(self, name, surname, age, bet=5000, percent=0):
        super().__init__(name, surname, age)
        self.bet = bet
        self.set_percent()



    def set_percent(self):
        percent = int(input(f'Какая выручка у {self.get_name()}?: '))
        self.percent = percent * 5 / 100

    def get_percent(self):
        return self.percent

    def get_salary(self):
        return self.bet + self.percent

    def __str__(self):
        info = super().__str__()
        info = f'{info}, зарплата: {self.get_salary()}'
        return info


class Worker(Emploee):
    def __init__(self, name, surname, age, hours=0):
        super().__init__(name, surname, age)
        self.set_hours()

    def set_hours(self):
        hours = int(input(f'Сколько часов отработал {self.get_name()}?: '))
        self.hour = hours

    def get_salary(self):
        return self.hour * 100

    def __str__(self):
        info = super().__str__()
        info = f'{info}, зарплата: {self.get_salary()}'
        return info


kirill = Manager('Кирилл', 'Друзьяк', 38)
print(kirill)

egor = Agent('Егор', 'Сергеев', 2)
print(egor)

jamshud = Worker('Джамшуд', 'Нуриев', 45)
print(jamshud)
