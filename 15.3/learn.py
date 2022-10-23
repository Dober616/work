text = input('Введите строку: ')
sym_numm = int(input('Номер символа: ')) -1
letters = list(text)
count = 0

for symbol in text:
    if symbol == text[sym_numm]:
        count += 1
print('Символ слева: \t', letters[sym_numm-1])
print('Символ справа: \t', letters[sym_numm+1])

if count == 0:
    print('Таких же символов нет')
elif count == 1:
    print('Есть ровно один такой же символ')
else:
    print('Таких символов: ', count)