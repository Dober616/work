my_list = [i for i in range(1, 19)]

my_iterator = iter(my_list)

while True:
    try:
        print(my_iterator.__next__())
    except BaseException('Список закончился'):
        break
