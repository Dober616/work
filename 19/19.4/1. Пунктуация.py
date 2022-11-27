text = 'Я! Есть. Грут!? Я, Грут и Есть.'  #  input('Введите текст: ')
symbols_set = set('.,:;!?')
print(symbols_set)
symbols_list = []
for each_symbol in text:
    if each_symbol in symbols_set:
        symbols_list.append(each_symbol)
print('Количество знаков пунктуации: ', len(symbols_list))
