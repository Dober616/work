ages_file = None
result_file = None


try:
    ages_file = open('ages.txt', 'r')
    result_file = open('result.txt', 'w')
except (FileExistsError, PermissionError) as huy:
    print('Поймано исключение', huy, type(huy))
if ages_file and result_file:
    names = 'qwertyuiop'  #input('Введите 10 имен через пробел: ').split(' ')
    count = 0
    for line in ages_file:
        try:
            clear_line = line.rstrip()
            result_file.write(f'{names[count]}: {clear_line}\n')
            count += 1
        except (ValueError, TypeError) as huy:
            print('Поймано исключение: ', huy, type(huy))
