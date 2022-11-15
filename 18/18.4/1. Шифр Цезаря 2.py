text = input('Введите исходный текст: ')
alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
step = int(input('Введите шаг замены: '))
encrypted_text = [alfabet.upper()[alfabet.upper().index(symbol.upper()) - len(alfabet) + step]
                  if symbol.upper() in alfabet.upper()
                  else symbol for symbol in text]
print(''.join(encrypted_text))
