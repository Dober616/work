import random

first_tuple = [random.randint(0, 5) for _ in range(10)]
second_tuple = [random.randint(-5, 0) for _ in range(10)]
print(first_tuple)
print(second_tuple)
first_tuple.extend(second_tuple)
print(f'Количество нулей в итоговом кортеже {first_tuple}: {first_tuple.count(0)}')
