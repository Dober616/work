import random
list_1 = [random.randint(0, 5) for _ in range(10)]
list_2 = [random.randint(-5, 0) for _ in range(10)]
list_1.extend(list_2)
tuple_3 = tuple(list_1)
print(tuple_3)
print('Количество нулей в получившемся списке: ', tuple_3.count(0))