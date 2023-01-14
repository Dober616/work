# nums_sum = 0
# nums_count = 0
# try:
#
#     numbers_file = open('numbers.txt', 'r')
#     for line in numbers_file:
#         nums_count += 1
#         nums_sum += int(line)
#     numbers_file.close()
#     print(f'Среднее арифметическое = {nums_sum/nums_count}')
# except FileNotFoundError:
#     print('Такой файл не найден')
# except ValueError:
#     print('Ошибка данных')


def divide(number):
    return 10 / number


def sum_of_divided(left, right):
    div_sum = 0
    for numm in range(left, right + 1):
        try:
            div_sum += divide(numm)
            print(div_sum)
        except ZeroDivisionError:
            print('На ноль же делить нельзя')
    return div_sum

total = 0
try:
    numbers_file = open('new_numbers.txt', 'r')
    for line in numbers_file:
        num_list = line.split()
        first_num = int(num_list[0])
        secnd_num = int(num_list[1])

        total += sum_of_divided(first_num, secnd_num)
    print(f'Общая сумма: {total}')
except ZeroDivisionError:
    print('На ноль делить нельзя!')