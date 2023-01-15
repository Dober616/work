class Employee:


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def employees_info(self):
        print(f'Чувака зовут: {self.name}, его зарплата: {self.salary}')

worker = Employee('Tom', 10000)
worker.employees_info()
worker_2 = Employee('Bob', 12000)
worker_2.employees_info()