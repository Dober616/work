class Employee:


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary



    def info(self):
        print(f'Имя работника: {self.name}\n'
              f'Зарплата работника: {self.salary}'
        )

empl_1 = Employee('Tom', 10000)
empl_1.info()
empl_2 = Employee('Bob', 12000)
empl_2.info()
