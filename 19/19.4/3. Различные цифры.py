new_string = input('Введите строку: ')
temp_string = ('0123456789')
result = [digit for digit in set(new_string) if digit in set(temp_string)]
print(''.join(set(result)))