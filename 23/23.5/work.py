line_count = 1
sym_sum = 0
try:
    with open('people.txt', 'r') as people_file:
        for line in people_file:
            line_count += 1
            lenght = len(line)
            if line.endswith('\n'):
                lenght -= 1
            if lenght < 3:
                raise BaseException(f'Длина строки {line_count} должна быть не меньше 3 символов')
            sym_sum += lenght

except FileNotFoundError:
    print('Такой файл не найден')
finally:
    print(f'Сумма символов {sym_sum}')
    print(people_file.closed)