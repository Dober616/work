def f1():
    print(f'Внутри f1 num = {number}')

def f2():
    number = 50 #Локальная переменная
    print(f'Внутри f2 num = {number}')

def f3():
    def f4():
        #global number
        nonlocal number
        number = 10
        print(f'Внутри f3/f4 num = {number}')
    number = 30
    print(f'Внутри f3 num = {number}')
    f4()
    print(f'Внутри f3 num = {number}')


number = 100 #Глобальная переменная
print(f'global num = {number}')
f1()
f2()
f3()
print(f'global num = {number}')

