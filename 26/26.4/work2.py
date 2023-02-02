# def Fibonacci(number):
#     result = list()
#     curent_value = 0
#     next_value = 1
#     for _ in range(number):
#         result.append(curent_value)
#         curent_value, next_value = next_value, curent_value + next_value
#     return result
#
# my_numm = Fibonacci(10)
# print(my_numm)

class Fibonacci:
    def __init__(self, number):
        self.number = number
        self.current_value = 0
        self.next_value = 1
        self.count = 0

    def __iter__(self):
        self.current_value = 0
        self.next_value = 1
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        if self.count > 1:
            if self.count > self.number:
                raise StopIteration('Дошли до нужного числа')
            self.current_value, self.next_value = self.next_value, self.current_value + self.next_value
        return self.current_value


fib_iterator = Fibonacci(10000000000)
print(8 in fib_iterator)