class Worker:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f'Работника зовут {self.name}\n'
              f'его зарплата: {self.salary}')

emp1 = Worker('Bob', 10000)
emp1.info()
emp2 = Worker('Tom', 12000)
emp2.info()
