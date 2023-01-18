class Employee:
    name = 'Tom'
    salary = 10000

    def info(self):
        print(f'Имя работника: {self.name}\n'
              f'Зарплата работника: {self.salary}'
        )

empl_1 = Employee()
empl_1.info()
empl_2 = Employee()
empl_2.name = 'Bob'
empl_2.salary = 12000
empl_2.info()
