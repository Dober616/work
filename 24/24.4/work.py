class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f'Работника зовут {self.name}\n'
              f'Его зарплата {self.salary}')

worker_1 = Employee('Tom', 10000)
worker_2 = Employee('Bob', 12000)

worker_1.info()
worker_2.info()