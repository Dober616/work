string = input('Введите строку: ')
add_symbol = input('Введите дополнительный символ: ')

new_string =[symbol * 2 for symbol in string]
print('Список удвоенных символов: ', new_string)
new_string =[symbol * 2 + add_symbol for symbol in string]
print('Склейка с дополнительными символами: ', new_string)
