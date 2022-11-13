import random
numbers_list = []
for i in range(4):
    number = random.randint(0,256)
    numbers_list.append(number)

ip_adress = f'{numbers_list[0]}.{numbers_list[1]}.{numbers_list[2]}.{numbers_list[3]}'
print('Вот такой ip-адрес получился: ', ip_adress)
