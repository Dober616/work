sym_sum = 0
line_count = 0
try:
    people_file = open('people.txt', 'r')
    for line in people_file:
        line_count += 1
        lenght = len(line)

        if line.endswith('\n'):
            lenght -= 1
        if lenght < 3:
            raise BaseException(f'Длина {line_count} строки меньше 3 символов')
        sym_sum += lenght
    people_file.close()

except FileNotFoundError:
    print('Такого файла нет')
finally:
    print(f'Найденная сумма символов: {sym_sum}')