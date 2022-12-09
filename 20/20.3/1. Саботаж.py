text = input('Введите текст с тильдами: ')
for number, symbol in enumerate(text):
    if symbol == '~':
        print(number+1)