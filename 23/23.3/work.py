def divine(number):
    return 10 / number


def sum_of_divided(left, right):
    div_sum = 0
    for num in range(left, right + 1):
        try:
            div_sum += divine(num)
            print(div_sum)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
    return div_sum


total = 0
try:
    numbers_file = open('numbers.txt', 'r')
    for line in numbers_file:
        nums_list = line.split()
        first_num = int(nums_list[0])
        secnd_num = int(nums_list[1])

        total += sum_of_divided(first_num, secnd_num)
    print(f'Общая сумма {total}')

except ZeroDivisionError:
    print('На ноль делить нельзя!')

answer_file = open('answer.txt', 'w')
try:
    answer_file.write('The answer is: ')
    answer_file.write(str(total))
except TypeError:
    print('Ошибка записи в файл. Тип данных не строка!')
else:
    print('Теперь все норм')
finally:
    answer_file.close()
    print(answer_file.closed)