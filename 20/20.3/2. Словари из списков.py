import random


def ennumerate_dict(my_list):
    my_dict = dict()
    for number, litter in enumerate(my_list):
        my_dict[number + 1] = litter
    return my_dict


alfabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

list_1 = [alfabet[random.randint(0, len(alfabet))-1] for _ in range(10)]
list_2 = [alfabet[random.randint(0, len(alfabet))-1] for _ in range(10)]
print(f'Первый список: {list_1}')
print(f'Второй список: {list_2}')
print(f'Первый словарь: {ennumerate_dict(list_1)}')
print(f'Второй словарь: {ennumerate_dict(list_2)}')
