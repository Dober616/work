bruce_willis = 42

input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = bruce_willis * leeloo
    print(f'-Leeloo Dallas! Multi-pass №{result}!')
except IndexError:
    print('Строка короче чем наш индекс')
except ValueError:
    print('На буквы у нас умножить не получится')
except Exception:
    print('Еще какая-то хрень произошла')