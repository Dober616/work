text = input('Введите строку: ')
sym_numm = int(input('Номер символа: ')) -1
letters = list(text)
count = 0
print('Длина текста', len(text))
for symbol in text:
    if symbol == text[sym_numm]:
        count += 1
if sym_numm == len(text)-1:
    print ('Справа символов не будет')
elif sym_numm >len(text)-1:
    print ('Вы вообще вышли за рамки')
else:
    print('Символ справа: \t', letters[sym_numm + 1])
if sym_numm == 0:
    print('Слева символов не будет')
elif sym_numm < 0:
    print ('Вы вообще вышли за рамки')
else:
    print('Символ слева: \t', letters[sym_numm-1])

if count == 0:
    print('Таких же символов нет')
elif count == 1:
    print('Есть ровно один такой символ')
else:
    print('Таких символов: ', count)
